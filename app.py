import streamlit as st

from agent import llm
from tools import search_web, save_report

st.set_page_config(
    page_title="AI Action Agent",
    page_icon="🤖"
)

st.title("🤖 AI Action Agent")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask something...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    query = user_input.lower()

    is_research = any(
        keyword in query
        for keyword in [
            "research",
            "latest",
            "news",
            "competitor",
            "competitors",
            "trend",
            "market",
            "analysis",
            "analyze"
        ]
    )

    should_save = any(
        keyword in query
        for keyword in [
            "save",
            "export",
            "write to file",
            "report file"
        ]
    )

    try:

        # NORMAL CHAT
        if not is_research:

            response = llm.invoke(user_input).content

        # RESEARCH FLOW
        else:

            search_results = search_web(user_input)

            if search_results is None:

                response = (
                    "I couldn't find any search results "
                    "for that query."
                )

            elif search_results.startswith("SEARCH_ERROR"):

                response = search_results

            else:

                prompt = f"""
You are an expert research analyst.

User Request:
{user_input}

Search Results:
{search_results}

Create a report with:

1. Executive Summary
2. Key Findings
3. Important Companies
4. Conclusion
"""

                response = llm.invoke(prompt).content

                if should_save:

                    saved_path = save_report(response)

                    if saved_path.startswith("SAVE_ERROR"):
                        response += (
                            f"\n\n❌ Failed to save report:\n{saved_path}"
                        )
                    else:
                        response += (
                            f"\n\n✅ Report saved at:\n{saved_path}"
                        )

    except Exception as e:

        response = f"Error: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# Sidebar
with st.sidebar:

    st.header("Controls")

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()