# Adobe-round-1b

## Persona Document Intelligence

This project is a document intelligence pipeline designed for Adobe Round 1B. It extracts and analyzes persona information from scanned identity documents (such as PAN, Aadhar, Driving License, etc.) using OCR and NLP techniques.

---

## 🚀 Project Structure

persona-doc-intelligence/
├── input/ # Folder to place input images (e.g., scanned documents)
├── output/ # Folder where output JSONs will be saved
├── src/
│ ├── main.py # Main orchestrator script
│ ├── extractor.py # Extracts text using OCR
│ ├── analyzer.py # Applies logic to extract persona info
│ └── utils.py # Helper functions
├── challenge1b_output.json # Final combined output
├── Dockerfile # For containerization (optional)
├── approach_explanation.md # Approach and thought process
└── README.md # This file

yaml
Copy
Edit

---

## 📌 Problem Statement

Given a folder of scanned ID documents, extract key persona information such as:

- Name  
- Date of Birth  
- Gender  
- Document Type  
- Document Number  

Output should be structured as a JSON for each document.

---

## 🧠 Approach

1. **OCR (Tesseract):** Use `pytesseract` to extract text from the image.  
2. **Text Cleaning:** Normalize and clean OCR output to reduce noise.  
3. **Regex/NLP Parsing:** Apply rules and regular expressions to extract key fields.  
4. **Document Classification:** Identify type of ID based on keywords (e.g., “Govt of India”, “DL No”, etc.)  
5. **JSON Output:** Save extracted details to a structured output.  

Refer to `approach_explanation.md` for a detailed explanation.

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Ramachandra-Pydi-18/Adobe-round-1b.git
cd Adobe-round-1b
2. Create and activate a virtual environment
python -m venv venv
For Windows:

venv\Scripts\activate
For Unix/Mac:

source venv/bin/activate
3. Install dependencies

pip install -r requirements.txt
Note: You must have Tesseract OCR installed on your system and added to PATH.
👉 Download Tesseract OCR

▶️ Run the Project
Place your document images in the input/ folder and run:

python src/main.py
📁 Output
The extracted persona data will be saved to:

lua

output/
└── <image_name>.json
📦 Docker (Optional)
Build the Docker image:

docker build -t persona-doc-intelligence .
Run the Docker container:

docker run -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" persona-doc-intelligence
📄 Sample Output (JSON)
json
Copy
Edit
{
  "Name": "Ram Chandra",
  "DOB": "01-01-2000",
  "Gender": "Male",
  "Document Type": "Aadhar Card",
  "Document Number": "XXXX-XXXX-XXXX"
}
📚 Requirements
Python 3.8+

pytesseract

OpenCV (cv2)

Pillow

re (Regex)

os, json (Built-in)

Tesseract OCR installed and configured

🤝 Contributions
This project was developed by Ramachandra Pydi as part of a Machine Learning round for Adobe.

Feel free to fork and contribute!

📬 Contact
📧 Email: ramachandrapydi18@gmail.com
🌐 GitHub: Ramachandra-Pydi-18

vbnet
Copy
Edit

Let me know if you'd like to auto-generate a PDF or if you want badges (like build,
