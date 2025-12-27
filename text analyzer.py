from collections import Counter
import string

text = input("Enter a paragraph:\n")

# Clean text
clean_text = text.lower().translate(str.maketrans("", "", string.punctuation))
words = clean_text.split()

# Word count
word_count = len(words)

# Top 5 frequent words
common_words = Counter(words).most_common(5)

# Sentence count
sentences = text.split(".")
sentence_lengths = [len(s.split()) for s in sentences if s.strip()]

# Save result
with open("analysis.txt", "w") as f:
    f.write(f"Total Words: {word_count}\n")
    f.write("Top 5 Words:\n")
    for word, count in common_words:
        f.write(f"{word}: {count}\n")
    f.write(f"Sentence Lengths: {sentence_lengths}\n")

print("✅ Text analysis completed & saved to analysis.txt")
