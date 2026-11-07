# AI Text Tools | MentisPrep Weeks 10 + 11

**Class:** Build a structured event extractor. **Homework:** Extend a document summarizer.
Both projects use **Python + Streamlit + Google Gemini**.

## Setup (do this before class if possible)
1. Install Python 3.11+ and VS Code.
2. Get your **own** free-tier Gemini API key at https://aistudio.google.com/apikey (follow instructor/guardian guidance for accounts).
3. Open a terminal at this repository's root.
4. Create and activate a virtual environment:
   - Mac/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows PowerShell: `py -m venv .venv; .venv\Scripts\Activate.ps1`
5. `python -m pip install -r requirements.txt`
6. Copy `.env.example` to `.env` and replace the placeholder with **your** API key. Never paste or commit your key in a public repository.
7. Confirm the configured `GEMINI_MODEL` is available on your free tier in Google AI Studio. The model in `.env.example` is a starting point, not a guarantee of availability.

## Run Week 10 in class
`python -m streamlit run week10_event_extractor/app.py`

- Checkpoint 1: Explain each `Event` schema field/type.
- Checkpoint 2: Finish `extract_event()` using Gemini's structured JSON output + Pydantic model.
- Checkpoint 3: Display fields and download validated JSON.
- Checkpoint 4: Test the three event announcements in `sample_data/events.txt`.
- Answer: Why should missing fields become `None` instead of guesses? Does valid JSON prove a fact is true?

## Run Week 11 homework
`python -m streamlit run week11_document_summarizer/app.py`

- Complete UTF-8 `.txt` upload decoding in `read_source()`.
- Implement a prompt that produces **five bullets** and one `Limitation:` sentence, grounded only in source text.
- Reject empty and overly long inputs (12,000-character maximum).
- Test **two** documents in `sample_data/`; record important omissions or unsupported claims.
- Check the output has exactly five bullets. Remember a prompt alone doesn't guarantee format.

## API syntax hints (Gemini)
- `from google import genai` and `from google.genai import types`
- `client = get_client()`
- `response = client.models.generate_content(model=get_model(), contents=prompt, config=types.GenerateContentConfig(response_mime_type="application/json", response_schema=Event))`
- `response.parsed` is the model-parsed response. Validate before downloading.

## Troubleshooting
- **Missing key**: check `.env` is in repo root and contains a real `GEMINI_API_KEY`.
- **Model not found**: check free-tier model access in AI Studio and update `GEMINI_MODEL`.
- **429 / quota exhausted**: slow requests or try again later; free-tier limits are shared per project.
- **ModuleNotFoundError**: activate your `.venv` and re-run `pip install -r requirements.txt`.
- **Unsafe data**: use only fictional/teacher-approved samples. Free-tier prompts may be used for product improvement.

Official docs: https://ai.google.dev/gemini-api/docs/structured-output and https://ai.google.dev/gemini-api/docs/pricing
