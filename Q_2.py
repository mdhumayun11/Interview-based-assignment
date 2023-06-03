from collections import Counter

def is_valid_string(s):
    # Count the frequency of each character in the string
    frequencies = Counter(s)

    # Count the frequencies of the frequencies
    freq_counts = Counter(frequencies.values())

    # If all frequencies are the same, the string is valid
    if len(freq_counts) == 1:
        return "YES"

    # If there are exactly two different frequencies
    elif len(freq_counts) == 2:
        # Check if removing one character can make the string valid
        if freq_counts[1] == 1 or (abs(freq_counts.most_common()[0][0] - freq_counts.most_common()[1][0]) == 1 and freq_counts[min(freq_counts)] == 1):
            return "YES"

    # Otherwise, the string is not valid
    return "NO"



# Example usage
input_str = "abc"
output = is_valid_string(input_str)
print(output)

# Additional Test 1
input_str = "aabbcc"
output = is_valid_string(input_str)
print(output)

# Additional Test 2
input_str = "aabbccddde"
output = is_valid_string(input_str)
print(output)
