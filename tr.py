from summarizer import Summarizer

with open("text.txt", "r") as f:
    text = f.read()

model = Summarizer()

result = model(text, min_length=20, max_length=200, use_first=False, ratio=0.6)

summary = "".join(result)

with open("summary.txt", "w") as summary_file:
    summary_file.write(summary)

original_size = len(text)
summary_size = len(summary)

print(f"Original Text Size: {original_size} characters")
print(f"Summarized Text Size: {summary_size} characters")
print("Summary written to 'summary.txt':")
print(summary)


