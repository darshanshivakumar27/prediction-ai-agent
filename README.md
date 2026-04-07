# CrowdWisdomTrading Prediction Market AI Agent

## Project Overview

This project implements a **multi-agent AI system** designed to research events and generate predictions related to prediction markets.

The system collects real-world information from the web, stores contextual knowledge, simulates trader analysis, and generates a final prediction.

The architecture is designed to mimic how traders analyze news events before making market decisions.

---

## Architecture

The system is composed of multiple agents working together:

1. **Scraper Agent**
   - Collects event information from the web using **Apify Google Search Scraper**.
   - Extracts titles and descriptions of relevant events.

2. **RAG Memory Layer**
   - Stores collected event information.
   - Retrieves knowledge for downstream analysis.

3. **Trader Agents**
   - Simulate market traders analyzing event information.
   - Generate sentiment signals (positive / negative / neutral).

4. **Decision Agent**
   - Aggregates trader signals.
   - Produces a final prediction about market direction.

---

## System Workflow

Web Events
↓
Scraper Agent (Apify)
↓
RAG Knowledge Memory
↓
Trader Sentiment Analysis
↓
Decision Agent
↓
Market Prediction

---

## Tech Stack

- Python
- Apify (Web scraping)
- Modular multi-agent architecture
- Simple RAG memory system

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/prediction-ai-agent.git

Navigate into the project folder:

cd prediction-ai-agent

Create virtual environment:

python -m venv venv

Activate environment:

Mac / Linux:
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

## Configuration

Create a file named **config.py** and add your Apify API token:

APIFY_TOKEN = "your_apify_token"

EVENT_QUERY = "AI startup funding news"

---

## Run the Project

Run the AI agent:

python main.py

---

## Example Output

Starting AI Prediction Agent...

Starting Prediction Agent
Researching event: AI startup funding news

Storing knowledge
Retrieving knowledge
Traders analyzing knowledge

FINAL RESULT
Prediction: Market uncertain

---

## Possible Improvements

Future improvements may include:

- Integration with real prediction market APIs (Polymarket / Kalshi)
- LLM-based reasoning using OpenRouter
- Improved RAG with vector databases
- Real trader wallet analysis
- Market category classification (sports / politics / weather)

---

## Author

Darshan S
BE Computer Science & Data Science
PES College of Engineering
