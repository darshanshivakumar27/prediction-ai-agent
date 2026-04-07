# traders.py

import random


def simulate_traders(knowledge):

    print("👨‍💼 Traders analyzing knowledge")

    opinions = []

    for k in knowledge:

        sentiment = random.choice(["positive", "negative", "neutral"])

        opinions.append({
            "event": k,
            "sentiment": sentiment
        })

    return opinions