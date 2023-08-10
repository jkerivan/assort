# from typing import Generator, Optional
# from vocode.streaming.agent.gpt4all_agent import TurnBasedGPT4AllAgent

# class BrokenRecordAgentConfig(AgentConfig, type="agent_broken_record"):
#     message: str


# class BrokenRecordAgent(RespondAgent[BrokenRecordAgentConfig]):

#     # is_interrupt is True when the human has just interrupted the bot's last response
#     def respond(
#         self, human_input, is_interrupt: bool = False
#     ) -> tuple[Optional[str], bool]:
#         return self.agent_config.message

#     def generate_response(
#         self, human_input, is_interrupt: bool = False
#     ) -> Generator[str, None, None]:
#         """Returns a generator that yields the agent's response one sentence at a time."""
#         yield self.agent_config.message