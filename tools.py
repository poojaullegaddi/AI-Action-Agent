from ddgs import DDGS
from datetime import datetime
import os


def search_web(query: str):
    try:
        results_text = ""

        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return None

        for r in results:
            results_text += f"""
Title: {r.get('title', '')}
Snippet: {r.get('body', '')}
URL: {r.get('href', '')}

"""

        return results_text

    except Exception as e:
        return f"SEARCH_ERROR: {str(e)}"


def save_report(content: str):
    try:
        os.makedirs("reports", exist_ok=True)

        filename = datetime.now().strftime(
            "report_%Y%m%d_%H%M%S.txt"
        )

        path = os.path.join("reports", filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Report saved at {path}"

    except Exception as e:
        return f"SAVE_ERROR: {str(e)}"