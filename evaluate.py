"""Week 13 Student Starter: Prompt A/B Improvement.

Run from the repository root:
    python weeks/week13_prompt_ab/evaluate.py

Before running: use your existing Week 10-12 environment and Gemini .env setup.
"""

import sys
from pathlib import Path

# Reuse common.py whether it lives at the repo root or in weeks/.
for folder in (Path(__file__).resolve().parents[2], Path(__file__).resolve().parents[1]):
    sys.path.insert(0, str(folder))
from common import get_client, get_model


# ============================================================
# CHECKPOINT 1: BASELINE VS. IMPROVED PROMPT
# ============================================================
# DISCUSS: What is a baseline? Why should we test both versions
# using the same examples?

BASELINE = "Summarize this text:\n\n{source}"

# STUDENT TASK 1: Change only the instructions below.
# Start by replacing THREE with a number (example: 3).
# STUDENT TASK 2: Replace AUDIENCE with your target reader
# (example: ninth-grade students).
# STUDENT TASK 3: Complete the accuracy rule after "Do not".
# Keep {source} exactly as written: Python inserts each test text.

IMPROVED = """Summarize only the SOURCE for AUDIENCE.
Return exactly THREE concise bullet points.
Do not ____________________.

SOURCE:
{source}"""


# ============================================================
# CHECKPOINT 2: THE FIXED TEST SET
# ============================================================
# These five cases are the same for Prompt A and Prompt B.
# Don't edit them while running the A/B comparison.

CASES = [
    {"name": "Water cycle", "source": "Evaporation turns liquid water into water vapor. Condensation forms clouds.", "required_terms": ["evaporation", "condensation"]},
    {"name": "Short input", "source": "Plants need light to grow.", "required_terms": ["plants", "light"]},
    {"name": "Two claims", "source": "Mars is a rocky planet. Mars has two small moons.", "required_terms": ["rocky", "moons"]},
    {"name": "Numbers", "source": "The experiment used 20 plants over 14 days.", "required_terms": ["20", "14"]},
    {"name": "Uncertainty", "source": "Scientists observed a change, but the cause is not yet known.", "required_terms": ["cause", "not yet known"]},
]


# ============================================================
# CHECKPOINT 3: HOW THE COMPARISON WORKS
# ============================================================
# The API calls are provided. Students don't need to memorize
# them. Both prompts use the same model and generation settings.


def ask_gemini(client, template, source):
    prompt = template.format(source=source)
    response = client.models.generate_content(
        model=get_model(),
        contents=prompt,
    )
    if not response.text:
        raise ValueError("Gemini returned an empty response.")
    return response.text.strip()


def keyword_score(output, required_terms):
    """Count required terms appearing in output (a rough check only)."""
    found = sum(term.lower() in output.lower() for term in required_terms)
    return found, len(required_terms)


def show_result(label, output, required_terms):
    found, total = keyword_score(output, required_terms)
    print(f"\n{label} | required terms found: {found}/{total}")
    print(output)
    # IMPORTANT: Keyword matching does NOT prove a claim is accurate.
    # Read the summary and check for invented or reversed facts.
    return found, total


# ============================================================
# CHECKPOINT 4: RUN BOTH PROMPTS ON THE SAME FIVE CASES
# ============================================================

def main():
    if "THREE" in IMPROVED or "AUDIENCE" in IMPROVED or "____________________" in IMPROVED:
        print("Complete the three student tasks in IMPROVED before running.")
        return

    client = get_client()
    results = []

    for case in CASES:
        print("\n" + "=" * 60)
        print("TEST CASE:", case["name"])
        print("SOURCE:", case["source"])
        try:
            a_output = ask_gemini(client, BASELINE, case["source"])
            b_output = ask_gemini(client, IMPROVED, case["source"])
        except Exception as error:
            print("Gemini request failed:", error)
            print("Check your .env, dependencies, model, and API access.")
            return

        a_found, total = show_result("PROMPT A (baseline)", a_output, case["required_terms"])
        b_found, _ = show_result("PROMPT B (improved)", b_output, case["required_terms"])
        results.append((case["name"], a_found, b_found, total))

    print("\n" + "=" * 60)
    print("KEYWORD COVERAGE SUMMARY (NOT AN ACCURACY GRADE)")
    for name, a, b, total in results:
        print(f"{name:15} A: {a}/{total}    B: {b}/{total}")

    print("\nCHECKPOINT 5: DISCUSS AND RECORD YOUR FINDINGS")
    print("1. Did B preserve the main facts better than A?")
    print("2. Did either output invent, reverse, or omit an important claim?")
    print("3. Did B follow its own requested bullet-point format?")
    print("4. Was there a regression (something B did worse than A)?")
    print("5. KEEP, REVISE, or REJECT B? Explain using evidence.")


if __name__ == "__main__":
    main()
