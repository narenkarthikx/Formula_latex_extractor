import os
import json
import re
from dotenv import load_dotenv
from pix2tex.cli import LatexOCR
import google.generativeai as genai
from PIL import Image

# 1. Load API key from .env

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Initialize LaTeX OCR model

ocr_model = LatexOCR()


# 3. Path to input image

image_path = "C:/Users/Naren/Downloads/latex_ocr_project/images/image2.png"


# 4. Extract LaTeX from image

print("🔍 Extracting formula from image...")
img = Image.open(image_path)
latex_code = ocr_model(img)
print(" Extracted LaTeX:", latex_code)


# 5. Ask Gemini to identify formula info

model = genai.GenerativeModel("models/gemini-2.5-flash")

prompt = f"""
You are an AI that classifies mathematical formulas.
Given this LaTeX expression:
{latex_code}

Return a JSON with:
- subject (e.g. Mathematics, Physics, Chemistry)
- topic (e.g. Coordinate Geometry, Mechanics, Algebra)
- formula_name (e.g. Distance Formula, Newton’s Second Law)
Only return valid JSON (no markdown formatting, no extra text).
"""

print(" Mapping formula details using Gemini...")
response = model.generate_content(prompt)


# 6. Clean Gemini response and parse JSON

raw_text = response.text.strip()

# Remove code fences like ```json ... ```
raw_text = re.sub(r"^```(?:json)?", "", raw_text, flags=re.MULTILINE)
raw_text = re.sub(r"```$", "", raw_text, flags=re.MULTILINE)
raw_text = raw_text.strip()

try:
    parsed = json.loads(raw_text)
except Exception as e:
    print(" Could not parse Gemini response:", e)
    print("Raw cleaned text:", raw_text)
    parsed = {
        "subject": "Unknown",
        "topic": "Unknown",
        "formula_name": "Unknown"
    }


# 7. Build final structured JSON

final_output = {
    "file": os.path.basename(image_path),
    "latex": latex_code,
    **parsed
}


# 8. Save the results

output_path = os.path.join(
    os.path.dirname(image_path),
    "final_output.json"
)

with open(output_path, "w") as f:
    json.dump([final_output], f, indent=4)

print(f" Done! Output saved to {output_path}")
