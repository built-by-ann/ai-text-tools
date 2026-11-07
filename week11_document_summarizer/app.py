"""Week 11 student starter: Document summarizer homework."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import streamlit as st
from common import get_client, get_model

MAX_CHARACTERS = 12_000


def read_source(pasted: str, upload) -> str:
    # HOMEWORK 1: If upload exists, decode its bytes as UTF-8.
    # Otherwise return the pasted text.
    return pasted


def summarize(source: str) -> str:
    # HOMEWORK 2: Call Gemini using get_client() and get_model().
    # Ask for exactly five concise bullet points and a sentence that starts
    # with "Limitation:". Use ONLY the source; do not invent facts.
    raise NotImplementedError("Implement the summarize() function.")


st.title("📝 Five-Bullet Document Summarizer")
st.caption("Week 11 homework | Teacher-approved, non-sensitive text only.")
pasted = st.text_area("Paste document text", height=180)
upload = st.file_uploader("Or upload a .txt file", type=["txt"])

if st.button("Summarize"):
    try:
        source = read_source(pasted, upload).strip()
        # HOMEWORK 3: Add friendly errors for invalid UTF-8,
        # empty source, and inputs longer than MAX_CHARACTERS.
        if not source:
            st.warning("Add text first.")
        elif len(source) > MAX_CHARACTERS:
            st.warning(f"Please shorten text to {MAX_CHARACTERS:,} characters.")
        else:
            st.write(summarize(source))
    except UnicodeDecodeError:
        st.error("This file must be UTF-8 text.")
    except NotImplementedError as e:
        st.info(str(e))
    except Exception as e:
        st.error(f"Summarization failed: {e}")
