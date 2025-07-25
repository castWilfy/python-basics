"""
# 3. Word Counter
Write a program that counts vowels, consonants, and total characters in a word.

Output: 
Enter a word: Python
Vowels: 1
Consonants: 5
Total characters: 6
"""

def main():
    word = input("Enter a word: ")
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in word:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    total_characters = len(word)
    
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Total characters: {total_characters}")

main()