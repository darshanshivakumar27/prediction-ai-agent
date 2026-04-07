# agent.py

from scraper import research_event
from rag import store_knowledge, retrieve_knowledge
from traders import simulate_traders
from decision import make_decision
from config import EVENT_QUERY


def run_agent():

    print("🚀 Starting Prediction AI Agent")

    # Step 1: research event
    data = research_event(EVENT_QUERY)

    # Step 2: store knowledge
    store_knowledge(data)

    # Step 3: retrieve knowledge
    knowledge = retrieve_knowledge()

    # Step 4: traders analyze
    opinions = simulate_traders(knowledge)

    # Step 5: final decision
    prediction = make_decision(opinions)

    print("\n✅ FINAL RESULT")
    print(prediction)