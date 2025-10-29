# LaTeX OCR Formula Mapper with Gemini Pro

An intelligent tool that extracts mathematical formulas from images using LaTeX-OCR and automatically classifies them using Google's Gemini Pro Vision API.

## 📋 Overview

This project combines state-of-the-art OCR technology with Google's Gemini Pro AI to:
1. Extract LaTeX code from mathematical formula images using `pix2tex` (LaTeX-OCR)
2. Automatically identify the subject, topic, and formula name using Gemini Pro
3. Generate structured JSON output with complete formula metadata

## 🚀 Features

- **Advanced LaTeX OCR**: Extracts complex LaTeX expressions from images using the `pix2tex` library
- **AI-Powered Classification**: Uses Google Gemini Pro to categorize formulas by subject, topic, and name
- **Structured Output**: Generates clean JSON files with all formula information
- **GPU Support**: Optional CUDA acceleration for faster OCR inference
- **Automatic Cleanup**: Handles and sanitizes AI responses to ensure valid JSON

## 📁 Project Structure

```
latex_ocr_project/
│
├── images/                     # Image assets
│   ├── image1.png             # Input formula images
│   ├── image2.png             # Example: Fourier Series
│   └── final_output.json      # Generated JSON output
│
├── formula_mapper.py          # Main processing script
├── .env                       # API keys (DO NOT COMMIT)
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

### File Descriptions

- **`formula_mapper.py`**: Core script that handles OCR extraction and Gemini AI classification
- **`images/`**: Directory containing input images and output JSON
- **`.env`**: Environment variables including Google API key
- **`final_output.json`**: Generated output with LaTeX code and metadata
- **`requirements.txt`**: List of all Python package dependencies

## 🛠️ Installation

### Prerequisites

- **Python 3.9+** (recommended: Python 3.10 or 3.11)
- **pip** (latest version)
- **Google API Key** for Gemini Pro
- **Optional**: CUDA 11.8+ for GPU acceleration

### Step 1: Clone the Repository

```bash
cd latex_ocr_project
```

### Step 2: Install Dependencies

#### ✅ Option A: CPU-Only Installation (Slower)

```bash
# Install PyTorch (CPU version)
pip install torch

# Install LaTeX-OCR from GitHub
pip install git+https://github.com/lukas-blecher/LaTeX-OCR.git@main

# Install other dependencies
pip install google-generativeai pillow python-dotenv
```

#### ⚡ Option B: GPU Installation (CUDA 11.8+ - Recommended for Speed)

```bash
# Install PyTorch with CUDA 11.8 support
pip install torch --index-url https://download.pytorch.org/whl/cu118

# Install LaTeX-OCR from GitHub
pip install git+https://github.com/lukas-blecher/LaTeX-OCR.git@main

# Install other dependencies
pip install google-generativeai pillow python-dotenv
```

#### 📋 Option C: Using requirements.txt

Create a `requirements.txt` file:

```txt
torch>=2.0.0
git+https://github.com/lukas-blecher/LaTeX-OCR.git@main
google-generativeai>=0.3.0
pillow>=10.0.0
python-dotenv>=1.0.0
```

Then install:

```bash
pip install -r requirements.txt
```

For GPU support, first install PyTorch with CUDA:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

1. Get a Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

2. Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_actual_api_key_here
```


## 💻 Usage

### Basic Usage

1. **Place your formula images** in the `images/` directory

2. **Update the image path** in `formula_mapper.py`:
   ```python
   image_path = "images/your_image.png"
   ```

3. **Run the script**:
   ```bash
   python formula_mapper.py
   ```

4. **Check the output** in `images/final_output.json`

### Processing Multiple Images

Modify `formula_mapper.py` to loop through images:

```python
import os

image_folder = "images/"
results = []

for filename in os.listdir(image_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(image_folder, filename)
        # Process image...
        results.append(result)
```

## 📊 Output Format

The script generates a JSON file with the following structure:

```json
[
    {
        "file": "image2.png",
        "latex": "f(\\stackrel{\\leftarrow}{x})=\\frac{a_{e}}{2}+...",
        "subject": "Mathematics",
        "topic": "Fourier Analysis",
        "formula_name": "Fourier Series"
    }
]
```

## 🔧 How It Works

1. **OCR Extraction**: The `LatexOCR` model processes the input image and extracts LaTeX code
2. **AI Classification**: Google Gemini AI analyzes the LaTeX expression and identifies:
   - Subject (e.g., Mathematics, Physics, Chemistry)
   - Topic (e.g., Fourier Analysis, Mechanics, Algebra)
   - Formula Name (e.g., Fourier Series, Newton's Second Law)
3. **JSON Generation**: Results are saved to `final_output.json`

## 📝 Example

**Input**: An image of the Fourier Series formula

**Output**:
- **LaTeX**: `f(\stackrel{\leftarrow}{x})=\frac{a_{e}}{2}+\sum_{n=1}^{\infty}a_{n}\cos n x+...`
- **Subject**: Mathematics
- **Topic**: Fourier Analysis
- **Formula Name**: Fourier Series

## ⚙️ Configuration

You can modify the following in `formula_mapper.py`:

- **Image path**: Update the `image_path` variable
- **AI model**: Change the Gemini model version in the `GenerativeModel` call
- **Prompt**: Customize the classification prompt for different categorization needs


## 📦 Dependencies

- `pix2tex` - LaTeX OCR engine
- `google-generativeai` - Google Gemini AI SDK
- `python-dotenv` - Environment variable management
- `Pillow` - Image processing

## 🤝 Contributing

Feel free to submit issues or pull requests to improve this project!

## 📄 License

This project is open source and available for educational purposes.