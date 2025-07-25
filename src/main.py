import os
import json
from extractor import extract_text_from_pdfs
from analyzer import analyze_text

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "challenge1b_output.json")

# Example keywords (modify as needed)
KEYWORDS = ["machine learning", "python", "cloud", "docker", "api"]

# Step 1: Extract
text_data = extract_text_from_pdfs(INPUT_DIR)

# Step 2: Analyze
result = analyze_text(text_data, KEYWORDS)

# Step 3: Save
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(OUTPUT_FILE, "w") as f:
    json.dump(result, f, indent=4)

print("✅ Analysis complete. Output saved to", OUTPUT_FILE)
