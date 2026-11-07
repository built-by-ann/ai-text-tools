"""Week 10 student starter: Build a structured event extractor."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import streamlit as st
from google.genai import types
from pydantic import BaseModel, Field
from common import get_client, get_model

# CHECKPOINT 1: Read the types. What happens when the announcement omits a location?
class Event(BaseModel):
    title: str
    date: str | None = None
    time: str | None = None
    location: str | None = None
    notes: list[str] = Field(default_factory=list)


def extract_event(raw_text: str) -> Event:
    """CHECKPOINT 2: Ask Gemini for an Event object using a response schema."""
    if not raw_text.strip():
        raise ValueError("Paste an event announcement first.")
    client = get_client()
    # TODO: Use client.models.generate_content(...)
    # Add contents with instructions: extract only stated facts; don't guess.
    # Set config=types.GenerateContentConfig(
    #     response_mime_type="application/json", response_schema=Event
    # )
    # Convert response.parsed into an Event and return it.
    raise NotImplementedError("Complete CHECKPOINT 2 in extract_event().")


st.title("📅 Event Extractor")
st.caption("Week 10 | Use fictional event announcements only.")
raw = st.text_area("Paste an event announcement", height=130)

if st.button("Extract"):
    if not raw.strip():
        st.warning("Paste an announcement first.")
    else:
        try:
            event = extract_event(raw)
            st.subheader(event.title)
            st.write("Date:", event.date or "Not provided")
            st.write("Time:", event.time or "Not provided")
            st.write("Location:", event.location or "Not provided")
            st.write("Notes:", event.notes)
            # CHECKPOINT 3: Export validated JSON instead of the raw model text.
            st.download_button("Download JSON", event.model_dump_json(indent=2),
                               "event.json", "application/json")
        except NotImplementedError as e:
            st.info(str(e))
        except Exception as e:
            st.error(f"Extraction failed: {e}")
