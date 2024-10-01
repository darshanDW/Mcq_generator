from summarizer import Summarizer

# Open and read the input text file
with open("text.txt", "r") as f:
    text = f.read()

# Initialize the BERT summarizer model
model = Summarizer()

# Generate the summary
result = model(text, min_length=20, max_length=200, use_first=False, ratio=0.6)

# Join the result into a single string
summary = "".join(result)

# Write the summarized text to a new file
with open("summary.txt", "w") as summary_file:
    summary_file.write(summary)

# Print the size of the original and summarized texts
original_size = len(text)
summary_size = len(summary)

print(f"Original Text Size: {original_size} characters")
print(f"Summarized Text Size: {summary_size} characters")
print("Summary written to 'summary.txt':")
print(summary)


