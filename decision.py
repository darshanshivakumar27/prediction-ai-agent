# decision.py


def make_decision(opinions):

    print("🤖 AI making prediction")

    positive = 0
    negative = 0

    for op in opinions:

        if op["sentiment"] == "positive":
            positive += 1

        elif op["sentiment"] == "negative":
            negative += 1

    if positive > negative:
        return "Prediction: Market likely to grow 📈"

    elif negative > positive:
        return "Prediction: Market likely to decline 📉"

    else:
        return "Prediction: Market uncertain ⚖️"