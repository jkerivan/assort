import os

from vocode.streaming.models.agent import ChatGPTAgentConfig
from vocode.streaming.models.message import BaseMessage
from vocode.streaming.models.telephony import TwilioConfig
from vocode.streaming.telephony.conversation.outbound_call import OutboundCall
from vocode.streaming.telephony.conversation.zoom_dial_in import ZoomDialIn
from vocode.streaming.telephony.server.base import InboundCallConfig, TelephonyServer
from vocode.streaming.models.synthesizer import ElevenLabsSynthesizerConfig, StreamElementsSynthesizerConfig
from vocode.streaming.telephony.config_manager.in_memory_config_manager import InMemoryConfigManager

import logging
from app.api import routers 

logging.basicConfig()
logger = logging.getLogger(__name__)

config_manager = InMemoryConfigManager()
import sys
BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
  from pyngrok import ngrok
  ngrok_auth = os.environ.get("NGROK_AUTH_TOKEN")
  if ngrok_auth is not None:
    ngrok.set_auth_token(ngrok_auth)
  port = sys.argv[sys.argv.index("--port") +
                  1] if "--port" in sys.argv else 3000

  # Open a ngrok tunnel to the dev server
  BASE_URL = ngrok.connect(port).public_url.replace("https://", "")
  logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(
    BASE_URL, port))

print(BASE_URL)

TWILIO_CONFIG = TwilioConfig(
  account_sid=os.getenv("TWILIO_SID"),
  auth_token=os.getenv("TWILIO_AUTH"),
)

CONFIG_MANAGER = config_manager  #RedisConfigManager()

AGENT_CONFIG = ChatGPTAgentConfig(
  initial_message=BaseMessage(text="Hello?"),
  prompt_preamble="Have a pleasant conversation about life",
  generate_responses=True,
)

SYNTH_CONFIG = StreamElementsSynthesizerConfig.from_telephone_output_device()

