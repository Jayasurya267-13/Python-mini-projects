import string

def is_palindrome(text):
    cleaned_text = "".join(
        char.lower() for char in text if char.isalnum()
    )
    return cleaned_text == cleaned_text[::-1]

print("Palindrome Checker (type 'exit' to quit)")

while True:
    user_input = input("Enter a word or phrase: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    if is_palindrome(user_input):
        print("It's a palindrome! ✅")
    else:
        print("Not a palindrome. ❌")
