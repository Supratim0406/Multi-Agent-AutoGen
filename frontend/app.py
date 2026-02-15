import streamlit as st
import requests

st.set_page_config(
    page_title="AI Job Search Agent",
    page_icon="🤖",
    layout="wide"
)

# ------------------------
# Header
# ------------------------
st.title("🤖 Multi-Agent Job Search AI")
st.markdown("Find jobs, optimize resume, and generate tailored cover letters using AI agents.")

# ------------------------
# Sidebar
# ------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    backend_url = st.text_input(
        "Backend URL",
        value="http://localhost:8000/search"
    )
    st.markdown("---")
    st.markdown("Built with AutoGen + FastAPI + Streamlit")

# ------------------------
# Main Input
# ------------------------
st.subheader("📝 Describe Your Profile")

query = st.text_area(
    "Example: I am a Python ML engineer with 2 years experience looking for remote jobs.",
    height=150
)

col1, col2 = st.columns([1, 4])

with col1:
    find_button = st.button("🚀 Find Jobs")

# ------------------------
# Action
# ------------------------
if find_button:

    if not query.strip():
        st.warning("Please enter your profile description.")
    else:
        with st.spinner("🤖 AI agents are analyzing and searching jobs..."):

            try:
                r = requests.post(
                    backend_url,
                    json={"query": query},
                    timeout=1800
                )

                if r.status_code != 200:
                    st.error(f"Backend Error: {r.status_code}")
                    st.text(r.text)

                else:
                    response = r.json()

                    if "error" in response:
                        st.error("❌ AI Error")
                        st.write(response["error"])

                    elif "result" in response:
                        st.success("✅ Jobs Found!")
                        st.markdown("### 📊 AI Recommendation")
                        st.markdown(response["result"])

                    else:
                        st.info("ℹ️ Raw Response")
                        st.json(response)

            except requests.exceptions.ConnectionError:
                st.error("🚨 Cannot connect to backend. Is FastAPI running?")

            except requests.exceptions.Timeout:
                st.error("⏳ Request timed out. Try again.")

            except Exception as e:
                st.error("Unexpected error occurred")
                st.write(str(e))

# ------------------------
# Footer
# ------------------------
st.markdown("---")
st.caption("© 2026 Multi-Agent Job Search System")
