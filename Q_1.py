def find_highest_frequency_word_length(input_string):
    # Split the input string into individual words
    words = input_string.split()

    # Count the frequency of each word
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # Find the highest frequency
    max_frequency = max(word_frequency.values())

    # Find the length of the highest-frequency word
    highest_frequency_words = [word for word, freq in word_frequency.items() if freq == max_frequency]
    highest_frequency_word_length = max(len(word) for word in highest_frequency_words)

    return highest_frequency_word_length


# Additional Test 1
input_str = "The quick brown fox jumps over the lazy dog"
result = find_highest_frequency_word_length(input_str)
print("Length of the highest-frequency word:", result)
# output Length of the highest-frequency word: 5


# Additional Test 2
input_str = "apple apple orange orange banana"
result = find_highest_frequency_word_length(input_str)
print("Length of the highest-frequency word:", result)
# output Length of the highest-frequency word: 6