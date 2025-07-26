"""
Create a program that analyzes text and provides:

Word count
Most frequent character
Longest word
Text reversed

"""
def main():
    text = input("Enter some text: ")
    
    # Word count
    words = text.split()
    word_count = len(words)
    
    # Most frequent character
    char_count = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    most_frequent_char = max(char_count, key=char_count.get, default=None)
    
    # Longest word
    longest_word = max(words, key=len, default="")
    
    # Text reversed
    reversed_text = text[::-1]
    
    # Output results
    print(f"Word count: {words}")
    print(f"Word count: {word_count}")
    print(f"Most frequent character: '{most_frequent_char}'")
    print(f"Longest word: '{longest_word}'")
    print(f"Reversed text: '{reversed_text}'")

main()