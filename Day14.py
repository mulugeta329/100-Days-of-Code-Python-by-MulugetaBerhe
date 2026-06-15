import random
import os

# --- GLOBAL DATA ASSETS ---
# Professional market metrics data bank
MARKET_DATA = [
    {"name": "Apple Inc. (AAPL)", "type": "Equity Stock", "description": "Consumer electronics and ecosystem giant"},
    {"name": "Bitcoin (BTC)", "type": "Cryptocurrency", "description": "The decentralized digital sovereign asset"},
    {"name": "Alphabet Inc. (GOOGL)", "type": "Equity Stock", "description": "Global internet search and AI infrastructure architecture"},
    {"name": "Ferrari NV (RACE)", "type": "Luxury Asset Stock", "description": "High-end performance automotive manufacturer"},
    {"name": "NVIDIA Corporation (NVDA)", "type": "Equity Stock", "description": "Advanced semiconductor chip and AI computational engine leader"},
    {"name": "Physical Gold Bullion", "type": "Precious Metal Commodity", "description": "The ancient global standard macroeconomic store of value"},
    {"name": "Ethereum (ETH)", "type": "Cryptocurrency", "description": "Decentralized smart-contract programmable network infrastructure"},
    {"name": "Microsoft Corp. (MSFT)", "type": "Equity Stock", "description": "Enterprise cloud processing software and operating system foundation"}
]

def clear_terminal():
    """Clears the console screen across platform environments."""
    os.system('cls' if os.name == 'nt' else 'clear')

def assign_mock_valuations(data_list):
    """Dynamically assigns localized baseline values to decouple volatile mock metrics."""
    # Instantiates absolute order logic for evaluations (Higher vs Lower tracking values)
    valuations = {
        "Physical Gold Bullion": 15000,
        "Microsoft Corp. (MSFT)": 3400,
        "Apple Inc. (AAPL)": 3300,
        "NVIDIA Corporation (NVDA)": 3100,
        "Alphabet Inc. (GOOGL)": 2200,
        "Bitcoin (BTC)": 1400,
        "Ethereum (ETH)": 400,
        "Ferrari NV (RACE)": 80
    }
    return [valuations[item["name"]] for item in data_list]

def format_asset_string(asset_dict):
    """Parses asset attributes into a structured string output."""
    return f"👉 {asset_dict['name']}, a {asset_dict['type']} ({asset_dict['description']})"

def evaluate_choice(guess, val_a, val_b):
    """Compares values and checks if the user's positional choice is valid."""
    if val_a > val_b:
        return guess == 'a'
    else:
        return guess == 'b'

def run_market_engine():
    """Main algorithmic game loop for the Market Valuation Comparison Engine."""
    clear_terminal()
    print("==================================================")
    print("      ENTERPRISE MARKET ASSET HIGHER-LOWER        ")
    print("==================================================")
    print("Evaluate asset metrics. Determine which has a HIGHER valuation.")
    print("==================================================")

    score = 0
    game_should_continue = True
    
    # Establish initial comparative coordinates
    asset_a = random.choice(MARKET_DATA)
    asset_b = random.choice(MARKET_DATA)

    while game_should_continue:
        # Guarantee asset B is never an identical match to asset A
        while asset_a == asset_b:
            asset_b = random.choice(MARKET_DATA)

        # Map current assets to their quantitative value array indices
        val_a, val_b = assign_mock_valuations([asset_a, asset_b])

        print(f"\n📊 [ASSET A]: {format_asset_string(asset_a)}")
        print("                        🆚 VS                        ")
        print(f"📊 [ASSET B]: {format_asset_string(asset_b)}")
        print("--------------------------------------------------")

        guess = input("Which asset holds a HIGHER valuation index? Type 'A' or 'B': ").lower().strip()
        
        if guess not in ['a', 'b']:
            print("⚠️ Invalid evaluation vector. Please enter 'A' or 'B'.")
            continue

        # Check metrics logic
        is_correct = evaluate_choice(guess, val_a, val_b)

        clear_terminal()
        print("==================================================")
        print("           MARKET ASSESSMENT ENGINE RUNNING       ")
        print("==================================================")

        if is_correct:
            score += 1
            print(f"✅ CORRECT ASSESSMENT! Active Tracker Score: {score}")
            # Structural transition: Current winner shifts down to become the new benchmark baseline A
            if guess == 'b':
                asset_a = asset_b
            asset_b = random.choice(MARKET_DATA)
        else:
            game_should_continue = False
            print(f"❌ INCORRECT ANALYSIS. System pipeline halted.")
            print(f"📊 Summary Data: {asset_a['name']} index was higher than {asset_b['name']}" if val_a > val_b else f"📊 Summary Data: {asset_b['name']} index was higher than {asset_a['name']}")
            print(f"🏆 Final Audited Score: {score}")
            print("==================================================")

if __name__ == "__main__":
    run_market_engine()