
import streamlit as st
from groq import Groq

# -----------------------------
# GROQ API
# -----------------------------
client = Groq(
    api_key="Your API Key Here")

st.set_page_config(
    page_title="Prompt Engineering Arena",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Prompt Engineering Arena")

st.write(
    "Enter a topic and compare how different prompting techniques influence AI responses."
)

topic = st.text_input(
    "Enter a Topic",
    placeholder="Artificial Intelligence"
)

generate = st.button("Generate Responses")

if generate:

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        prompts = {
            "👨‍🏫 Teacher Prompt":
            f"""
            You are an expert teacher.

            Explain {topic} clearly with examples.
            """,

            "🧒 Grade 5 Prompt":
            f"""
            Explain {topic} to a Grade 5 student using simple language.
            """,

            "🔬 Scientist Prompt":
            f"""
            You are a scientist.

            Explain {topic} with technical details.
            """,

            "📖 Storytelling Prompt":
            f"""
            Explain {topic} through an interesting story.
            """,

            "🎤 Interview Prompt":
            f"""
            Explain {topic} in a question-answer interview format.
            """
        }

        responses = {}

        with st.spinner("Generating Responses..."):

            for prompt_name, prompt in prompts.items():

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=500
                )

                responses[prompt_name] = response.choices[0].message.content

        st.success("Responses Generated Successfully!")

        for prompt_name, response_text in responses.items():

            st.subheader(prompt_name)

            st.text_area(
                label="Response",
                value=response_text,
                height=250,
                key=prompt_name
            )

        st.info(
            "Observe how the same topic generates different responses when different prompting techniques are used."
        )