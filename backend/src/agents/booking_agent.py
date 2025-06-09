BookingAgent = Agent(
    name="BookingAgent",
    description="Booking agent: searches for salons, selects one, and books an appointment",
    tools=[HairSalonSearchTool()],
    goal_function=BookingGoalFunction(),
)

