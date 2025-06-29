def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else None

sentence = "The quick brown fox jumps over the lazy dog"
result = longest_word(sentence)
print(f"The longest word is: '{result}'") if result else print("Empty sentence!")