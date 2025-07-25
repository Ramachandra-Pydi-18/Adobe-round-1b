# Approach Explanation

## Objective
To extract relevant information from uploaded resumes and rank them based on given keywords or skills.

## Steps
1. Parse all PDFs from the `input` directory using `PyPDF2`.
2. Extract raw text from each page of each document.
3. Match given keywords (e.g., Python, ML) to text using simple string matching.
4. Rank documents based on keyword match count.
5. Store results in `output/challenge1b_output.json`.

## Tools Used
- Python
- PyPDF2
- JSON for result storage
- Docker for containerization

