"""
AI STUDY COACH - PROJECT 1: Smart Calculator
This teaches functions, loops, and basic logic
"""

def smart_calculator():
    """Main calculator function with AI-like features"""
    
    print("🤖 AI Calculator Activated!")
    print("Commands: add, subtract, multiply, divide, stats, quit")
    
    history = []  # We'll use this to store calculations
    
    while True:
        command = input("\nEnter command: ").lower().strip()
        
        if command == 'quit':
            print(f"📊 Session Summary: {len(history)} calculations made")
            print("Goodbye! 👋")
            break
            
        elif command in ['add', 'subtract', 'multiply', 'divide']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if command == 'add':
                    result = num1 + num2
                    symbol = '+'
                elif command == 'subtract':
                    result = num1 - num2
                    symbol = '-'
                elif command == 'multiply':
                    result = num1 * num2
                    symbol = '*'
                else:  # divide
                    if num2 == 0:
                        print("⚠️ Error: Cannot divide by zero!")
                        continue
                    result = num1 / num2
                    symbol = '/'
                
                calculation = f"{num1} {symbol} {num2} = {result}"
                history.append(calculation)
                print(f"🧮 Result: {calculation}")
                
            except ValueError:
                print("⚠️ Please enter valid numbers!")
                
        elif command == 'stats':
            if not history:
                print("No calculations yet!")
            else:
                print("📈 Calculation History:")
                for i, calc in enumerate(history, 1):
                    print(f"  {i}. {calc}")
                print(f"\nTotal calculations: {len(history)}")
                
        else:
            print("❌ Unknown command. Try: add, subtract, multiply, divide, stats, quit")

# AI-Enhanced Feature: Learning from patterns
def find_patterns(numbers):
    """AI-like pattern detection (we'll expand this later)"""
    if len(numbers) < 2:
        return "Need more data for pattern detection"
    
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    
    if all(diff == differences[0] for diff in differences):
        return f"Linear pattern: Add {differences[0]} each time"
    elif all(numbers[i+1] / numbers[i] == numbers[1] / numbers[0] for i in range(len(numbers)-1)):
        ratio = numbers[1] / numbers[0]
        return f"Geometric pattern: Multiply by {ratio} each time"
    
    return "Complex pattern detected - need more AI training! 🧠"

# Run the calculator
if __name__ == "__main__":
    print("=" * 50)
    print("WELCOME TO YOUR FIRST AI PROJECT")
    print("=" * 50)
    
    # Test pattern detection (preview of AI concepts)
    test_pattern = [2, 4, 6, 8, 10]
    print(f"\n🔍 AI Pattern Detection Preview:")
    print(f"Sequence: {test_pattern}")
    print(f"Analysis: {find_patterns(test_pattern)}")
    
    print("\n" + "=" * 50)
    smart_calculator()