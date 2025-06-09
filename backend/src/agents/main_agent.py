from google.adk.agents import SequentialAgent
from .booking_agent import BookingAgent
from .support_agent  import SupportAgent

main_agent = SequentialAgent(
    name="ZapisMain",
    description="Top-level salon assistant: first understands intent, then delegates",
    sub_agents=[BookingAgent(), SupportAgent()],
)
