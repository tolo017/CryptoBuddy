# 🌱 CryptoBuddy: Sustainable Crypto Advisor 🤖


CryptoBuddy is a rule-based chatbot that provides cryptocurrency investment advice by analyzing **profitability** (price trends) and **sustainability** (energy efficiency). Built with Python, it demonstrates basic AI decision-making principles through conversational logic.

## Features
- 💬 Interactive chat interface
- 📊 Analyzes predefined crypto database
- ⚖️ Balances profit potential vs sustainability
- ⚠️ Includes risk disclaimer
- 🚫 No external dependencies

## Dataset Structure
```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": { ... },
    "Cardano": { ... }
}

How to Run
Clone repository:

bash
git clone https://github.com/tolo017/CryptoBuddy.git
Execute script:

bash
python crypto_buddy.py

Ask questions like:

"Which crypto is most sustainable?"

"What should I buy for long-term growth?"

"Show trending coins"

Sample Conversation:

You: What's a good eco-friendly crypto?
CryptoBuddy: Cardano is our top green pick! 🌱 
Sustainability score: 8/10

Note: Crypto investments carry risk. Please research thoroughly.

Key AI Concepts Demonstrated:
Rule-based decision trees

Pattern matching in user queries

Priority-based ranking algorithms

Basic conversational state management

⚠️ Disclaimer: Not financial advice. Educational project only.