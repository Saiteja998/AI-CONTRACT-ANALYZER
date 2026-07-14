import json
import streamlit as st

from src.pipeline.query import ContractQueryPipeline

# -----------------------------
# Initialize Pipeline
# -----------------------------
pipeline = ContractQueryPipeline()

st.set_page_config(
    page_title="AI Contract Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("📄 AI Contract Analyzer")

st.markdown("""
Analyze legal contracts using **Retrieval-Augmented Generation (RAG)**,
**Sentence Transformers**, **ChromaDB**, and **Groq LLM**.
""")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("📌 Project Information")

st.sidebar.markdown("""
### Features

- 📄 Contract Retrieval
- 🔎 Semantic Search
- 🤖 Clause Extraction
- 📑 Contract Summarization
- 📊 Confidence Scoring
- 📚 Source Tracking
- 📦 JSON Output

---

### Tech Stack

- Groq (Llama 3.3 70B)
- ChromaDB
- Sentence Transformers
- Streamlit
""")

st.sidebar.markdown("---")
st.sidebar.write("**Indexed Contracts:** 52")
st.sidebar.write("**Indexed Chunks:** 4033")
st.sidebar.write("**Embedding Model:** all-MiniLM-L6-v2")
st.sidebar.write("**Vector Database:** ChromaDB")

# -----------------------------
# Suggested Questions
# -----------------------------
st.markdown("### 💡 Example Questions")

col1, col2 = st.columns(2)

with col1:
    st.markdown("- What are the termination clauses?")
    st.markdown("- Explain confidentiality clauses.")
    st.markdown("- What are the payment terms?")

with col2:
    st.markdown("- Explain liability clauses.")
    st.markdown("- Explain indemnification.")
    st.markdown("- Summarize this contract.")

# -----------------------------
# Input
# -----------------------------
question = st.text_input(
    "💬 Ask a legal question",
    placeholder="Example: What are the termination clauses?"
)

# -----------------------------
# Analyze
# -----------------------------
if st.button("🔍 Analyze Contract"):

    if not question.strip():
        st.warning("⚠ Please enter a question.")
        st.stop()

    with st.spinner("Analyzing Contract..."):

        result = pipeline.ask(question)
    st.subheader("🐞 Debug Result")
    st.write(result)

    

    response = result.get("response", {})

    if not isinstance(response, dict):
        st.error("Invalid response returned from the LLM.")
        st.stop()

    st.success("Analysis Completed Successfully ✅")

    # -----------------------------
    # Clause Type
    # -----------------------------
    st.subheader("📋 Clause Type")

    st.info(
        response.get(
            "clause_type",
            "Not Available"
        )
    )

    # -----------------------------
    # Clause Summary
    # -----------------------------
    st.subheader("📝 Clause Summary")

    st.write(
        response.get(
            "summary",
            "No summary available."
        )
    )

    # -----------------------------
    # Contract Summary
    # -----------------------------
    

    # -----------------------------
    # Clause Text
    # -----------------------------
    st.subheader("📄 Extracted Clause")

    st.text_area(
        "",
        response.get(
            "clause_text",
            "Clause not found."
        ),
        height=250
    )

    # -----------------------------
    # Important Points
    # -----------------------------
    st.subheader("✅ Important Points")

    points = response.get("important_points", [])

    if points:
        for point in points:
            st.markdown(f"- {point}")
    else:
        st.info("No important points available.")

    # -----------------------------
    # Confidence
    # -----------------------------
    st.subheader("📊 Confidence")

    confidence = result.get("confidence", 0.0)

    if confidence >= 0.90:
        level = "🟢 High"
    elif confidence >= 0.75:
        level = "🟡 Medium"
    else:
        level = "🔴 Low"

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Score",
            f"{confidence:.2f}"
        )

    with col2:
        st.metric(
            "Level",
            level
        )

    # -----------------------------
    # Sources
    # -----------------------------
    st.subheader("📚 Retrieved Sources")

    with st.expander("View Source Contracts"):

        for idx, source in enumerate(result.get("sources", []), start=1):

            st.markdown(f"""
**{idx}. Contract:** {source['contract']}

**Chunk:** {source['chunk']}

---
""")

    # -----------------------------
    # JSON Response
    # -----------------------------
    st.subheader("📦 JSON Response")

    with st.expander("View Raw JSON"):

        st.json(response)

    st.download_button(
        label="⬇ Download JSON",
        data=json.dumps(response, indent=4),
        file_name="contract_analysis.json",
        mime="application/json"
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "Developed by Sai Teja | AI Contract Analyzer | RAG • Groq • ChromaDB • Streamlit"
)