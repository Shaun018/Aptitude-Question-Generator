
import streamlit as st
import requests
import json

# ---------------- CONFIGURATION ----------------

st.set_page_config(
    page_title="Aptitude AI Generator",
    page_icon="🧠",
    layout="centered"
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"

# ---------------- HEADER ----------------

st.title("🧠 Aptitude AI Generator")
st.caption("AI-powered placement preparation and practice")
st.divider()

# ---------------- USER INPUT ----------------

topic = st.selectbox(
    "Choose Aptitude Topic",
    [
        "Percentages",
        "Profit and Loss",
        "Time and Work",
        "Time Speed and Distance",
        "Ratio and Proportion",
        "Probability",
        "Number Series",
        "Logical Reasoning",
        "Coding-Decoding",
        "Blood Relations",
        "Permutations and Combinations"
    ]
)

difficulty = st.selectbox(
    "Choose Difficulty",
    ["Easy", "Medium", "Hard"]
)

number = st.slider(
    "Number of Questions",
    1, 10, 2
)

# ---------------- GENERATE QUIZ ----------------

if st.button(
    "🚀 Generate Questions",
    use_container_width=True,
    key="generate_quiz"
):

    prompt = f"""
You are an expert aptitude question generator.

Generate exactly {number} original MCQ questions.

Topic: {topic}
Difficulty: {difficulty}

Rules:
1. Each question must have exactly four options.
2. Only one option must be correct.
3. Answer must be A, B, C or D.
4. Give a clear step-by-step solution.
5. Match the selected difficulty.
6. Avoid duplicate questions.
7. Return only valid JSON.

Required structure:

{{
  "questions": [
    {{
      "question": "Question text",
      "options": {{
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D"
      }},
      "answer": "A",
      "solution": "Step-by-step explanation"
    }}
  ]
}}
"""

    with st.spinner("Generating questions using Qwen AI..."):

        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL,
                    "prompt": prompt,
                    "format": "json",
                    "stream": False,
                    "options": {
                        "temperature": 0.3,
                        "num_predict": 2500,
                        "num_ctx": 4096,
                        "num_thread": 4
                    }
                },
                timeout=300
            )

            response.raise_for_status()

            result = response.json()["response"]
            quiz = json.loads(result)

            questions = quiz.get("questions", [])

            if len(questions) != number:
                raise ValueError(
                    f"Expected {number} questions, "
                    f"received {len(questions)}."
                )

            # Validate generated questions
            for q in questions:

                if not all(
                    key in q for key in
                    ["question", "options", "answer", "solution"]
                ):
                    raise ValueError("Incomplete question structure.")

                if set(q["options"].keys()) != {"A", "B", "C", "D"}:
                    raise ValueError("Invalid options.")

                if q["answer"] not in ["A", "B", "C", "D"]:
                    raise ValueError("Invalid correct answer.")

            # Reset previous quiz answers
            for key in list(st.session_state.keys()):
                if key.startswith("answer_"):
                    del st.session_state[key]

            st.session_state.questions = questions
            st.session_state.topic = topic
            st.session_state.difficulty = difficulty
            st.session_state.submitted = False

            st.success("Questions generated successfully!")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to Ollama. Check whether it is running.")

        except requests.exceptions.Timeout:
            st.error("Generation timed out. Please try again.")

        except json.JSONDecodeError:
            st.error("The AI returned incomplete JSON. Please generate again.")

        except Exception as e:
            st.error(f"Generation error: {e}")


# ---------------- DISPLAY QUIZ ----------------

if "questions" in st.session_state:

    questions = st.session_state.questions

    st.divider()

    st.subheader(
        f"📚 {st.session_state.topic} - "
        f"{st.session_state.difficulty}"
    )

    for i, q in enumerate(questions):

        st.markdown(f"### Question {i + 1}")

        st.write(q["question"])

        selected = st.radio(
            "Select your answer:",
            ["A", "B", "C", "D"],
            index=None,
            format_func=lambda x, opts=q["options"]:
                f"{x}. {opts[x]}",
            key=f"answer_{i}"
        )

        if st.button(
            "Show Solution",
            key=f"solution_{i}"
        ):

            correct = q["answer"]

            if selected is None:
                st.warning("Please select an answer first.")

            elif selected == correct:
                st.success("Correct Answer! 🎉")

            else:
                st.error(f"Incorrect! Correct answer: {correct}")

            st.markdown(
                f"**Correct Answer:** "
                f"{correct}. {q['options'][correct]}"
            )

            st.info(q["solution"])

        st.divider()

    # ---------------- SUBMIT QUIZ ----------------

    if st.button(
        "📊 Submit Quiz",
        use_container_width=True,
        key="submit_quiz"
    ):

        unanswered = [
            i for i in range(len(questions))
            if st.session_state.get(f"answer_{i}") is None
        ]

        if unanswered:
            st.warning(
                f"Please answer all questions. "
                f"{len(unanswered)} remaining."
            )

        else:

            score = sum(
                1 for i, q in enumerate(questions)
                if st.session_state.get(f"answer_{i}") == q["answer"]
            )

            total = len(questions)
            percentage = (score / total) * 100

            st.session_state.submitted = True
            st.session_state.final_score = score
            st.session_state.final_percentage = percentage

    # ---------------- RESULTS DASHBOARD ----------------

    if st.session_state.get("submitted", False):

        score = st.session_state.final_score
        percentage = st.session_state.final_percentage
        total = len(questions)

        st.divider()
        st.header("🏆 Quiz Results")

        col1, col2 = st.columns(2)

        col1.metric("Your Score", f"{score}/{total}")
        col2.metric("Accuracy", f"{percentage:.1f}%")

        st.progress(percentage / 100)

        if percentage >= 80:
            st.success("Excellent Performance! 🎉")
        elif percentage >= 50:
            st.info("Good effort! Keep practicing.")
        else:
            st.warning("Keep learning and try again!")

        st.subheader("Answer Summary")

        for i, q in enumerate(questions):

            user_answer = st.session_state.get(f"answer_{i}")
            correct = q["answer"]

            if user_answer == correct:
                st.success(f"Question {i+1}: Correct")
            else:
                st.error(
                    f"Question {i+1}: Incorrect | "
                    f"Your answer: {user_answer} | "
                    f"Correct answer: {correct}"
                )

    # ---------------- NEW QUIZ ----------------

    if st.button(
        "🔄 Generate New Quiz",
        use_container_width=True,
        key="new_quiz"
    ):

        for key in list(st.session_state.keys()):
            if key.startswith("answer_"):
                del st.session_state[key]

        del st.session_state.questions

        st.session_state.submitted = False

        st.rerun()
