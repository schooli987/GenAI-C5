import streamlit as st

st.set_page_config(
    page_title="AI Prompt Engineering Lab",
    page_icon="🧠"
)

st.title("🧠 AI Prompt Engineering Lab")

st.write(
    "Explore how different prompting techniques affect AI responses"
)

topic = st.text_area(
    "Enter a Topic",
    placeholder="Photosynthesis"
)

prompt_type = st.selectbox(
    "Choose Prompting Technique",
    [
        "Zero-Shot Prompting",
        "Role Prompting",
        "Audience Prompting",
        "Few-Shot Prompting",
        "Chain-of-Thought Prompting",
        "Structured Prompting",
        "Constraint Prompting",
        "Comparative Prompting"
    ]
)

temperature = st.slider(
    "Creativity Level",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

max_tokens = st.slider(
    "Response Length",
    min_value=100,
    max_value=1000,
    value=500,
    step=100
)

generate = st.button("Generate Response")