from app.models.contact_information import ContactInformation
from app.db.session import get_db
from typing import OrderedDict

from sqlalchemy.orm import Session
from app.api.twilio_sms_client import TwilioMessageClient
from fastapi import APIRouter, Form, Response, Request, Depends
from twilio.twiml.voice_response import Gather, Redirect, VoiceResponse, Pause
import openai
from twilio.twiml.messaging_response import MessagingResponse
import os
import re
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY", "")

account_sid = os.environ.get("TWILIO_SID", "")
auth_token = os.environ.get("TWILIO_AUTH", "")
twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER", "")


def find_phone_numbers(text):
    # Define a regex pattern for a simple phone number with digits and optional separators
    pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    
    # Find all matches in the input text
    phone_numbers = re.findall(pattern, text)
    return phone_numbers


# Create an instance of TwilioMessageClient
message_client = TwilioMessageClient(account_sid, auth_token, twilio_phone_number)
router = APIRouter()

# Should be modeled out and exist in DB
questions = [
    # description, required, confirm_spelling
    ("first and last name", True, True),
    ("date of birth", True, False),
    ("What is your insurance information Payer name?", True, False),
    ("What is your insurance id?", True, True),
    ("Do you have a referral for todays visit?", False, False),
    ("What is your reason for coming in", False, False),
    ("What is the best number to reach you at?", True, True)
]

number_to_message = ""

class CallContext:
    def __init__(self):
        self.step = 0
        self.answers = OrderedDict

def get_call_context(request: Request) -> CallContext:
    context = CallContext()
    request.state.call_context = context
    return context


def get_latest_phone_number(db: Session):
    latest_phone_data = db.query(ContactInformation).order_by(ContactInformation.created_at.desc()).first()
    if latest_phone_data:
        return latest_phone_data.phone_number
    return None  



@router.post("/complete")
async def completed(request: Request):
    form_data = await request.form()
    speech_result = form_data.get('SpeechResult', '').strip().lower()
    step = int(request.query_params.get('step', 0))
    res = VoiceResponse()
    #custom responses in db
    if "yes" in speech_result.lower() or "yeah" in speech_result.lower():
        step += 1
        
        
    res.redirect(f"/calls/handle-question?step={step}")
    xml_response = str(res)
    return Response(content=xml_response, media_type="application/xml")


@router.post("/confirm")
async def confirm(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    speech_result = form_data.get('SpeechResult', '').strip().lower()

    vresponse = VoiceResponse()
    step = int(request.query_params.get('step', 0))


    prompt = f"You just gathered information regarding {questions[step][0]}Confirm the {speech_result} spelling by repeating the letters/numbers that match/mkae sense {questions[step][0]}. Then ask if it is correct. "
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            temperature=0.7
        )
    
    body = MessagingResponse().message(response["choices"][0])
    text = body.value['text'].strip()

    if step == len(questions)-1:
        pass
        # number_to_message = find_phone_numbers(text)[0]
        # phone_data = ContactInformation(phone_number=number_to_message)
        # db.add(phone_data)
        # db.commit()
    
    
    with vresponse.gather(speechTimeout="auto", speech_model="phone_call", input='speech', enhanced="true", action=f'/calls/complete?step={step}', method='POST') as gather:
        gather.say(text)
        vresponse.append(gather)
    
    xml_response = str(vresponse)
    return Response(content=xml_response, media_type="application/xml")

@router.post("/handle-question")
def handle_question(request: Request, db: Session = Depends(get_db)):
    step = int(request.query_params.get('step', 0))

    if step >= len(questions):
        response = VoiceResponse()
        response.say("Thank you for providing your information. Goodbye!")
        xml_response = str(response)

        message = "Thank you for providing your information. Your appointment is confirmed with Doctor Who on October 25th, 2024."
        # to_number = get_latest_phone_number()
        # print(to_number)
        # message_client.send_sms(to_number, message)
        return Response(content=xml_response, media_type="application/xml")
    
    question = questions[step][0]

    prompt = f"You want to get information regarding the following: {question} \
               Create a question to get the data politely"

    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            temperature=0.7
        )

    body = MessagingResponse().message(response["choices"][0])
    text = body.value['text'].strip()
    
    vresponse = VoiceResponse()
    with vresponse.gather(speechTimeout="auto", speech_model="phone_call", input='speech', enhanced="true", action=f'/calls/confirm?step={step}', method='POST') as gather:
        gather.say(text)
        vresponse.append(gather)
    
    xml_response = str(vresponse)
    return Response(content=xml_response, media_type="application/xml")

@router.post("")
def call():
    res = VoiceResponse()
    res.say("Welcome to Demo, I am going to ask you some questions regarding your information.")
    
    res.redirect("/calls/handle-question")

    xml_response = str(res)
    return Response(content=xml_response, media_type="application/xml")

