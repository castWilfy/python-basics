#*********************************************************************************
# *********************Functions: Parameters vs Arguments*************************
"""Functions:
Think of a function as a trading strategy template that you can reuse.

def calculate_profit(buy_price, sell_price, quantity):  --# These are PARAMETERS
    profit = (sell_price - buy_price) * quantity
    return profit

Function Call:
my_profit = calculate_profit(100, 120, 50) -- # These values (100, 120, 50) are ARGUMENTS

Stock Market Analogy:
Parameters = The blank fields in a trading form template
"Buy Price: ____"
"Sell Price: ____"
"Quantity: ____"

Arguments = The actual values you fill in when placing a real trade
"Buy Price: $100"
"Sell Price: $120"
"Quantity: 50 shares"

Visual Workflow:
1. Create Function Template (with parameters)
   ↓
2. Call Function with Real Values (arguments)
   ↓
3. Function Processes the Arguments
   ↓
4. Returns Result

Practical Example:

# Function definition - like creating a trading calculator
def analyze_stock(symbol, current_price, target_price):  # Parameters
    potential_return = ((target_price - current_price) / current_price) * 100
    recommendation = "BUY" if potential_return > 10 else "HOLD"
    return potential_return, recommendation

# Function calls - like using the calculator for real stocks
apple_return, apple_rec = analyze_stock("AAPL", 150, 180)      # Arguments
tesla_return, tesla_rec = analyze_stock("TSLA", 200, 250)      # Arguments
"""
#*********************************************************************************

#*********************************************************************************
# Function Definition
#*********************************************************************************

def hello(name):
    print(f"Hello, {name}!")

name = input("What's your name? ")
hello(name)

#********************************************************************************
# Function with default parameter
#********************************************************************************

def helloTest(to = "World"):
    print(f"Hello, {to}!")

helloTest()
lastName = input("What's your name? ")
helloTest(lastName)