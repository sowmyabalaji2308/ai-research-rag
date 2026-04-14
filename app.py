
import streamlit as st
import requests

st.set_page_config(page_title="AI Research RAG", page_icon="📄")

st.title("📄 AI Research Papers Q&A")
st.caption("Ask anything about Transformers, LoRA, and RAG")

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Ask a question:", placeholder="What is LoRA?")

if st.button("Ask") and question:
    with st.spinner("Searching papers..."):
        response = requests.post(
            "http://localhost:8000/ask",
            json={"query": question}
        )
        result = response.json()

    st.session_state.history.append(result)

for item in reversed(st.session_state.history):
    st.markdown("**Q: " + item["question"] + "**")
    st.success(item["answer"])
    
    with st.expander("View Sources"):
        seen = set()
        for s in item["sources"]:
            key = f"{s['file']} page {s['page']}"
            if key not in seen:
                seen.add(key)
                st.write(f"📄 {s['file']} — page {s['page']}")
    
    st.divider()
