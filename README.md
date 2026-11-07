# AI Text Tools | MentisPrep Weeks 10 + 11

Welcome to AI Text Tools!

In this project, we'll build two AI-powered applications using **Python, Streamlit, Pydantic, and the Google Gemini API**.

- **Week 10: Structured Event Extractor (In Class)**
- **Week 11: Five-Bullet Document Summarizer (Homework)**

You'll learn how to extract information from text, structure AI responses using JSON, validate data, and summarize longer documents.

---

## Part 1: Fork and Clone the Repository

### Step 1: Fork the Repository

We'll use forks so everyone can work independently and save their own code.

1. Open the GitHub repository link provided. https://github.com/built-by-ann/ai-text-tools
2. Sign in to your GitHub account.
3. Click **Fork** in the upper-right corner.
4. Under **Owner**, select your personal GitHub account.
5. Keep the repository name as `ai-text-tools`.
6. Click **Create fork**.

You should now see the repository under your own GitHub account.

### Step 2: Clone Your Fork

Cloning downloads your GitHub repository onto your computer so you can work on it in VS Code.

1. Open your forked repository on GitHub.
2. Click the green **Code** button.
3. Select **HTTPS**.
4. Copy the repository URL.
5. Open VS Code and open a terminal using **Terminal → New Terminal**.

Run:

```bash
git clone YOUR_FORK_URL
```

Replace `YOUR_FORK_URL` with the URL you copied.

For example:

```bash
git clone https://github.com/your-username/ai-text-tools.git
```

**Important:** Clone your own fork, not the original repository.

### Step 3: Open the Project

Navigate into your project folder:

Select **File → Open Folder** in VS Code and open the `ai-text-tools` folder.

---

## Part 2: Set Up Your Python Environment

### Step 4: Create a Virtual Environment

A virtual environment keeps the packages for this project separate from other Python projects on your computer.

Open the terminal in VS Code.

**Mac:**

```bash
python3 -m venv .venv
```

**Windows:**

```powershell
py -m venv .venv
```

This creates a folder named `.venv` inside your project.

### Step 5: Activate Your Virtual Environment

**Mac:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

After activation, you should see something similar to:

```text
(.venv) your-computer ai-text-tools %
```

The `(.venv)` indicates that your virtual environment is active.

**Important:** Activate your virtual environment whenever you return to this project.

If VS Code asks you to select a Python interpreter, select the one inside `.venv`.

### Step 6: Install Dependencies

A dependency is an external Python package that our project needs to work.

Instead of installing every package individually, we'll install everything from `requirements.txt`.

Run:

```bash
python -m pip install -r requirements.txt
```

Our project uses:

| Package | Purpose |
|---|---|
| `streamlit` | Build interactive web applications |
| `google-genai` | Connect Python to the Gemini API |
| `pydantic` | Define and validate structured data |
| `python-dotenv` | Load environment variables from a `.env` file |

Once installation finishes, we're ready to configure Gemini.

---

## Part 3: Set Up the Gemini API

### Step 7: Get Your Gemini API Key

An API key allows your Python application to send requests to Gemini.

Each student will use their **own API key**.

1. Visit https://aistudio.google.com/apikey
2. Sign in with your Google account.
3. Follow your instructor's directions to create an API key in an eligible free-tier project.
4. Copy your API key.

**Do not enable paid billing for this class.**

The Gemini API has free-tier usage limits, so avoid sending unnecessary repeated requests.

Never share your API key with classmates or upload it to GitHub.

### Step 8: Create Your `.env` File

An `.env` file stores configuration values, including API keys, separately from our Python code.

In VS Code:

1. Find `.env.example` in the main project folder.
2. Create a new file named `.env` in the same folder.
3. Copy the contents of `.env.example` into `.env`.
4. Replace the placeholder API key with your own.

Your `.env` file should look like this:

```dotenv
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
```

Use the model specified in `.env.example` unless your instructor tells you otherwise.

**Important:** Your `.env` file contains a secret. Do not share it.

The project's `.gitignore` should exclude both `.env` and `.venv` so neither gets uploaded to GitHub.

### Step 9: Run the Week 10 Application

Make sure your virtual environment is activated.

From the main project folder, run:

```bash
python -m streamlit run week10_event_extractor/app.py
```

Streamlit should open the application in your browser.

You should see the Event Extractor interface.

The starter application is intentionally incomplete. We'll implement the extraction functionality together during class.

---

## Part 4: Week 10 | Structured Event Extractor

### Project Goal

Build an AI application that takes a messy event announcement and extracts important details into structured JSON.

For example:

**Input:**

"Hey everyone! The robotics club is hosting a competition on Friday at 3 PM in the school gym. Bring your laptops!"

**Expected output:**

```json
{
  "title": "Robotics Competition",
  "date": "Friday",
  "time": "3 PM",
  "location": "School gym",
  "notes": [
    "Bring your laptops"
  ]
}
```

### What We'll Learn

- What JSON is and why programmers use it
- What a schema is
- How to define data using Pydantic
- How to get structured responses from Gemini
- How to handle missing information using `None` and `null`
- How to validate AI-generated information
- Why valid JSON doesn't necessarily mean the information is correct

### Checkpoint 1: Understand the Event Schema

Open:

`week10_event_extractor/app.py`

Find the `Event` model.

Our event schema contains:

| Field | Type | Description |
|---|---|---|
| `title` | `str` | Name of the event |
| `date` | `str \| None` | Date, if provided |
| `time` | `str \| None` | Time, if provided |
| `location` | `str \| None` | Location, if provided |
| `notes` | `list[str]` | Additional information |

Discuss:

- Why is `title` required?
- Why can `location` be `None`?
- Why might `notes` be a list instead of a single string?

### Checkpoint 2: Implement Structured Extraction

Complete the `extract_event()` function.

Your function should:

1. Accept an event announcement as a string.
2. Send the text to Gemini.
3. Request a response following the `Event` schema.
4. Validate the resulting data using Pydantic.
5. Return the validated event.

The AI should only extract information explicitly supported by the announcement.

If a date, time, or location is missing, it should remain missing.

**Do not invent missing information.**

### Checkpoint 3: Display the Results

Use Streamlit to display:

- Event title
- Date
- Time
- Location
- Additional notes

If a field is missing, display `Not provided`.

Add a button to download the validated event as a JSON file.

### Checkpoint 4: Test the Extractor

Open:

`sample_data/events.txt`

Test your application with three types of inputs.

**Test 1: Complete information**

An announcement that contains a title, date, time, and location.

**Test 2: Missing information**

An announcement that does not include a location or date.

**Test 3: Confusing information**

An announcement with vague details or incomplete information.

For each test, ask yourself:

- Did Gemini extract the correct information?
- Did it invent anything?
- Were missing fields represented correctly?
- Did the output follow our schema?

### Week 10 Completion Checklist

- [ ] My Streamlit application runs.
- [ ] My Gemini API connection works.
- [ ] I understand the Event schema.
- [ ] My extractor returns validated structured data.
- [ ] Missing information is handled correctly.
- [ ] I can download the output as JSON.
- [ ] I tested three announcements.

---

## Part 5: Week 11 | Five-Bullet Document Summarizer

**Homework Assignment**

### Project Goal

Build an AI application that reads text from a document and produces a short, useful summary.

Instead of extracting specific fields, we'll ask Gemini to identify and summarize the most important ideas.

Your application should return:

- Exactly five concise bullet points
- One additional sentence beginning with `Limitation:`

The limitation sentence should explain what the short summary may leave out.

### Example

**Input:**

"The school announced a new recycling initiative starting next Monday. Students will find recycling bins in classrooms, hallways, and the cafeteria. The environmental club will help educate students about which materials can be recycled. Teachers will receive information about the program during their weekly meeting. The school hopes to reduce waste and encourage more environmentally responsible habits."

**Possible output:**

- The school is launching a recycling initiative next Monday.
- Recycling bins will be placed in classrooms, hallways, and the cafeteria.
- The environmental club will teach students about recyclable materials.
- Teachers will receive information during their weekly meeting.
- The goal is to reduce waste and encourage environmentally responsible habits.

**Limitation:** This summary does not include specific details about accepted recyclable materials because the source does not provide them.

### Step 1: Open the Homework Application

Open:

`week11_document_summarizer/app.py`

Make sure your virtual environment is activated.

Run:

```bash
python -m streamlit run week11_document_summarizer/app.py
```

### Checkpoint 1: Accept Text Input

Your application should allow users to:

- Paste text into a Streamlit text area.
- Upload a `.txt` file.

Complete the `read_source()` function.

For uploaded files, decode the file contents using UTF-8.

### Checkpoint 2: Implement Summarization

Complete the `summarize()` function using Gemini.

Your prompt should instruct Gemini to:

1. Read only the provided source text.
2. Identify the most important information.
3. Return exactly five concise bullet points.
4. Include one limitation sentence.
5. Avoid inventing information.

### Checkpoint 3: Validate the Input

Your application should reject:

- Empty inputs
- Inputs longer than 12,000 characters
- Uploaded files that cannot be decoded as UTF-8

Display a helpful error message when invalid input is provided.

### Checkpoint 4: Test Your Summarizer

Use the documents in:

`sample_data/document_one.txt`

`sample_data/document_two.txt`

Run your application on both documents.

For each result, check:

- Are there exactly five bullet points?
- Is there a limitation sentence?
- Are the main ideas represented?
- Did Gemini add any unsupported information?
- Did the summary leave out something important?

### Checkpoint 5: Evaluate the Results

For each document, write a short evaluation answering:

1. What important information did the summary preserve?
2. Did it leave out any important details?
3. Did Gemini include any information that wasn't in the source?

Remember that a summary can look correct while still containing inaccurate information.

### Week 11 Completion Checklist

- [ ] My application accepts pasted text.
- [ ] My application supports `.txt` uploads.
- [ ] Uploaded files are decoded using UTF-8.
- [ ] Empty inputs are rejected.
- [ ] Inputs longer than 12,000 characters are rejected.
- [ ] Gemini generates five bullet points.
- [ ] The output includes a limitation sentence.
- [ ] I tested two documents.
- [ ] I evaluated the accuracy of both summaries.

---

## Part 6: Save Your Work to GitHub

As you complete your projects, you'll save your progress to your personal fork.

### Step 1: Check Your Changes

In the VS Code terminal, run:

```bash
git status
```

This shows which files you've changed.

Before committing, make sure your `.env` file and `.venv` folder are not being tracked.

### Step 2: Stage Your Changes

```bash
git add .
```

### Step 3: Commit Your Work

For Week 10:

```bash
git commit -m "Complete Week 10 event extractor"
```

For Week 11:

```bash
git commit -m "Complete Week 11 document summarizer"
```

A commit saves a snapshot of your changes in Git.

### Step 4: Push to GitHub

```bash
git push origin main
```

This uploads your committed changes to your own GitHub fork.

### Step 5: Submit Your Assignment

1. Open your fork on GitHub.
2. Confirm that your latest changes appear.
3. Copy your repository URL.
4. Submit the URL using your instructor's directions.

You do not need to create a pull request unless your instructor specifically asks you to.

---

## Troubleshooting

### My virtual environment isn't activated

Activate it again.

**Mac:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### I get `ModuleNotFoundError`

Make sure the virtual environment is active and reinstall dependencies:

```bash
python -m pip install -r requirements.txt
```

### Gemini says my API key is missing

Check that:

- Your `.env` file exists in the root project folder.
- The variable is spelled `GEMINI_API_KEY`.
- You've replaced the placeholder with your actual key.
- You saved the `.env` file.

### I get a Gemini model error

Make sure your `GEMINI_MODEL` matches the model provided by your instructor.

Not all Gemini models are available in every API project or free tier.

### I get a quota or rate-limit error

The Gemini API has usage limits.

Avoid rapidly repeating requests. If the problem continues, let your instructor know.

### Streamlit won't start

Make sure you're in the main project folder, your virtual environment is activated, and all dependencies are installed.

### GitHub won't let me push

Check that you're pushing to your own fork:

```bash
git remote -v
```

The `origin` URL should contain your GitHub username, not your instructor's.

---

## Important Reminders

- Never share your Gemini API key.
- Never commit your `.env` file.
- Do not upload your `.venv` folder.
- Use only fictional or instructor-approved, non-sensitive data.
- Check AI-generated responses for accuracy.
- Save and push your work regularly.
- Ask questions when you're stuck!

---

## Helpful Resources

- [Google AI Studio](https://aistudio.google.com/apikey)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [GitHub Forking Guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

---

## What You'll Have Built

By the end of these projects, you'll have two working AI applications.

**Week 10: Event Extractor**

An application that takes messy event announcements and turns them into validated, structured JSON.

**Week 11: Document Summarizer**

An application that reads text documents, identifies important information, and generates concise summaries.

Both projects demonstrate how we can use AI to transform unstructured text into useful information for real applications.