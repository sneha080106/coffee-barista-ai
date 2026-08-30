import json
from google.adk.agents.llm_agent import Agent

with open("menu.json", "r") as f:
    MENU = json.load(f)

def get_menu() -> str:
    """Returns the coffee shop menu. Use this to find available drinks and food."""
    return json.dumps(MENU)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="coffee_barista",
    description="A friendly AI coffee shop assistant that recommends menu items.",
    instruction="""
You are a friendly and personalized coffee shop barista.

Always use the get_menu tool before recommending or discussing menu items.
Never invent products, prices, ingredients, or allergens.

Ask about the customer's preferences when useful, such as:
- hot or cold
- strong or mild
- sweet or less sweet
- dairy or dairy-free
- vegan preferences

Then recommend one or more suitable items from the menu.
Explain briefly why each recommendation fits.

Keep responses friendly, concise, and conversational.
""",
    tools=[get_menu],
)
