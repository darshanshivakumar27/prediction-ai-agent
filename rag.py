# rag.py

knowledge_base = []


def store_knowledge(data):

    print("📚 Storing knowledge")

    for d in data:
        knowledge_base.append(d)


def retrieve_knowledge():

    print("📖 Retrieving knowledge")

    return knowledge_base