# AI Text Tools | MentisPrep Weeks 10 + 11

In this project, we'll build two AI-powered applications using **Python, Streamlit, and Google Gemini**.

- **Week 10 (In Class):** Structured Event Extractor
- **Week 11 (Homework):** Five-Bullet Document Summarizer

You'll learn how to extract structured information from text, work with JSON, validate AI outputs, and summarize documents.

No coding or setup is required before class. We'll complete the setup together!

---

## Part 1: Project Setup (In Class)

### Step 1: Clone the GitHub Repository

Open VS Code and open a new terminal.

Clone the repository using:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate into the project:

```bash
cd ai-text-tools
```

Open the project folder in VS Code.

### Step 2: Create a Virtual Environment

A virtual environment keeps the Python packages for this project separate from other Python projects on your computer.

**Mac:**
```bash
python3 -m venv .venv
```

**Windows:**
```powershell
py -m venv .venv
```

### Step 3: Activate Your Virtual Environment

**Mac:**
```bash
source .venv/bin/activate
```

**Windows PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

After activation, you should see `(.venv)` at the beginning of your terminal prompt.

**Important:** Make sure your virtual environment is activated whenever you're working on this project.

If VS Code asks you to select a Python interpreter, choose the Python interpreter inside `.venv`.

### Step 4: Install Dependencies

With your virtual environment activated, run:

```bash
python -m pip install -r requirements.txt
```

This installs the packages needed for our applications:

- `streamlit`: Creates our web application interfaces.
- `google-genai`: Connects Python to the Gemini API.
- `pydantic`: Defines and validates structured data.
- `python-dotenv`: Loads environment variables from our `.env` file.

### Step 5: Get Your Gemini API Key

We'll use the Google Gemini API to power our applications.

1. Visit https://aistudio.google.com/apikey
2. Sign in to your Google account.
3. Follow your instructor's guidance to create an API key using a free-tier project.
4. Copy your new API key.

You will use your own API key for this project.

Do not enable paid billing for this class.

**Important:** Never share your API key, paste it into a public GitHub repository, or include it in screenshots.

### Step 6: Set Up Your `.env` File

Inside your project folder, find the file named:

`.env.example`

Create a new file in the same folder named:

`.env`

Copy the contents of `.env.example` into `.env`.

Your file should look like this:

```dotenv
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-3.1-flash-lite
```

Replace `your_actual_api_key_here` with your own key.

Keep the model specified in the class starter unless your instructor provides a different free-tier model.

**Why are we using a `.env` file?**

A `.env` file lets us store configuration and sensitive information separately from our Python code.

Our `.gitignore` prevents `.env` from being committed to Git.

### Step 7: Run Your First Application

From the project root, run:

```bash
python -m streamlit run week10_event_extractor/app.py
```

Streamlit should open a browser tab showing the Event Extractor.

The application interface is provided, but the extraction functionality is not finished yet. We'll implement that together during class.

---

## Part 2: Week 10 - Structured Event Extractor (In Class)

### Our Goal

Build an AI application that takes a messy event announcement and extracts specific information into a structured format.

For example:

**Input:**

"Hey everyone! The robotics club is hosting a competition on Friday at 3 PM in the school gym. Bring your laptops!"

**Expected information:**

```json
{
  "title": "Robotics Competition",
  "date": "Friday",
  "time": "3 PM",
  "location": "School gym",
  "notes": ["Bring your laptops"]
}
```

### What We'll Learn

- What JSON is and why programmers use it
- What schemas are
- How to define data using Pydantic
- How to generate structured output using Gemini
- How to handle missing information using `None` and `null`
- How to validate AI-generated information

### Class Coding Checkpoints

Open:

`week10_event_extractor/app.py`

**Checkpoint 1: Understand the Schema**

Review the `Event` class and identify each field and its data type.

**Checkpoint 2: Implement the Gemini API Call**

Complete the `extract_event()` function so Gemini returns structured data using our `Event` schema.

**Checkpoint 3: Display and Download JSON**

Display the extracted event details in Streamlit and download the validated output as a JSON file.

**Checkpoint 4: Test Your Extractor**

Use the examples in:

`sample_data/events.txt`

Test three types of announcements:

1. An announcement containing all expected information.
2. An announcement missing important information.
3. An announcement containing confusing or incomplete details.

Remember: AI should not invent information that wasn't provided.

---

## Part 3: Week 11 - Five-Bullet Document Summarizer (Homework)

### Our Goal

Build a second AI application that reads documents and summarizes the most important information.

Instead of extracting specific fields, we'll ask Gemini to identify the main ideas.

The application should return:

- Exactly five concise bullet points
