crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def crypto_chatbot():
    print("CryptoBuddy: Hey there! Let's find you a green and growing crypto! 🌱")
    print("CryptoBuddy: Ask me about sustainability, price trends, or investment advice. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").lower()
        if 'exit' in user_input:
            print("\nCryptoBuddy: Remember, crypto is risky - always do your own research! Goodbye! 👋")
            break
            
        response = None
        disclaimer = "\nNote: Crypto investments carry risk. Please research thoroughly."
        
        # Sustainability focus
        if any(word in user_input for word in ['sustainable', 'eco', 'green']):
            best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            response = f"{best} is our top green pick! 🌱 Sustainability score: {crypto_db[best]['sustainability_score']*10}/10"
        
        # Profitability focus
        elif any(word in user_input for word in ['profit', 'trend', 'rising']):
            profitable = [c for c in crypto_db 
                         if crypto_db[c]["price_trend"] == "rising"
                         and crypto_db[c]["market_cap"] == "high"]
            if profitable:
                best = max(profitable, key=lambda x: crypto_db[x]["sustainability_score"])
                response = f"{best} is trending up! 📈 Market cap: {crypto_db[best]['market_cap'].capitalize()}"
            else:
                response = "No high-market-cap coins currently trending up"
        
        # Long-term growth
        elif any(word in user_input for word in ['long-term', 'growth']):
            candidates = [c for c in crypto_db 
                         if crypto_db[c]["price_trend"] == "rising"
                         and crypto_db[c]["sustainability_score"] >= 0.7]
            if candidates:
                best = max(candidates, key=lambda x: crypto_db[x]["market_cap"])
                response = f"Long-term pick: {best} 🚀 Rising price + sustainability ({crypto_db[best]['sustainability_score']*10}/10)"
            else:
                response = "No coins currently meet both growth and sustainability criteria"
        
        # Default response
        else:
            response = "Ask me about:\n- Sustainable coins 🌱\n- Trending coins 📈\n- Long-term growth 🚀"
        
        print(f"\nCryptoBuddy: {response}{disclaimer}\n")

# Start the chatbot
if __name__ == "__main__":
    crypto_chatbot()