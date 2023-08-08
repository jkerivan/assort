from fastapi import APIRouter, Form, Response, Request
from twilio.twiml.voice_response import Gather, VoiceResponse, Pause

router = APIRouter()

# should be db models to make more dynamic
questions = [
    ("first and last name"),
    ("date of birth"),
    ("insurance information"),
    ("referral information"),
    ("chief medical complaint"),
    ("contact information")
]

@router.post("")
def call():
    return handle_question(0)

@router.post("/completed")
async def completed(request: Request):
    form_data = await request.form()
    speech_result = form_data.get('SpeechResult', '').strip().lower()
    print("User input:", speech_result)
    
    step = int(request.query_params.get('step', 0))
    next_step = step + 1 if step < len(questions) - 1 else None
    
    return handle_question(next_step)

def handle_question(step):
    if step is None:
        response = VoiceResponse()
        response.say("Thank you for providing your information. Goodbye!")
        xml_response = str(response)
        return Response(content=xml_response, media_type="application/xml")
    
    question = questions[step]
    
    response = VoiceResponse()
    gather = Gather(input='speech', action=f'/calls/completed?step={step}', method='POST')
    gather.say(f"May I please have your {question}?")
    response.append(gather)
    
    xml_response = str(response)
    return Response(content=xml_response, media_type="application/xml")