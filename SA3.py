import streamlit as st
from groq import Groq

client = Groq(
    api_key="YOUR_API_KEY"
)

st.set_page_config(
    page_title="AI Prompt Engineering Lab",
    page_icon="🧠"
)

st.title("🧠 AI Prompt Engineering Lab")

st.write("Explore how different prompting techniques affect AI responses")

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

if generate:

    if topic.strip() == "":

        st.warning("Please enter a topic")

    else:

        if prompt_type == "Zero-Shot Prompting":

            prompt = f"""
            Explain {topic}.
            """

        elif prompt_type == "Role Prompting":

            prompt = f"""
            You are an expert teacher.

            Explain {topic}.
            """

        elif prompt_type == "Audience Prompting":

            prompt = f"""
            Explain {topic} to a Grade 5 student using simple language.
            """

        elif prompt_type == "Few-Shot Prompting":

            prompt = f"""
            Example:

            Topic: Gravity

            Explanation:
            Gravity is the force that pulls objects towards the Earth.

            Now explain:

            Topic: {topic}
            """

        elif prompt_type == "Chain-of-Thought Prompting":

            prompt = f"""
            Explain {topic} step-by-step.

            Show your reasoning process clearly.
            """

        elif prompt_type == "Structured Prompting":

            prompt = f"""
            Explain {topic} using the following format:

            1. Definition
            2. Key Features
            3. Examples
            4. Applications
            5. Summary
            """

        elif prompt_type == "Constraint Prompting":

            prompt = f"""
            Explain {topic} in exactly 50 words.
            """

        else:

            prompt = f"""
            Compare {topic} with a similar concept.

            Show similarities and differences in a table.
            """

        with st.spinner("Generating Response..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )

            output = response.choices[0].message.content

        st.success("Response Generated Successfully")

        st.subheader("Prompt Used")

        st.text_area(
            "Generated Prompt",
            prompt,
            height=200
        )

        st.subheader("AI Response")

        st.text_area(
            "Generated Response",
            output,
            height=350
        )