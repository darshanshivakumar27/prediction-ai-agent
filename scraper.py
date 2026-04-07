from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)


def research_event(event):

    print("🔎 Researching event:", event)

    run = client.actor("apify/google-search-scraper").call(
        run_input={
            "queries": event,
            "maxPagesPerQuery": 1
        }
    )

    dataset_id = run["defaultDatasetId"]

    results = []

    for item in client.dataset(dataset_id).iterate_items():
        text = item.get("title", "") + " " + item.get("description", "")
        results.append(text)

    return results


# testing scraper
if __name__ == "__main__":

    data = research_event("AI startup funding news")

    for d in data[:5]:
        print(d)