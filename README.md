# AI Aptitude Question Generator

An AI-powered aptitude quiz generator built using **Python, Streamlit, Ollama, and Qwen 2.5 3B**. It dynamically generates multiple-choice aptitude questions with answer options, correct answers, and explanations based on the selected topic and difficulty level.

## Features

- **Dynamic Question Generation:** Generates questions using a locally running LLM.
- **Multiple Topics:** Percentages, Profit and Loss, Time and Work, Time Speed and Distance, Ratio and Proportion, Probability, Number Series, Logical Reasoning, Coding-Decoding, Blood Relations, and Permutations and Combinations.
- **Difficulty Levels:** Easy, Medium, and Hard.
- **Custom Question Count:** Generate between 1 and 10 questions.
- **Interactive Quiz:** Attempt questions through a Streamlit interface.
- **Solution Display:** View correct answers and explanations.
- **Score Calculation:** Submit answers and view your score and accuracy.
- **Quiz Reset:** Generate a fresh quiz whenever required.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Ollama | Local LLM execution |
| Qwen 2.5 3B | AI question generation |
| Streamlit | Web interface |
| Requests | API communication |
| JSON | Structured response processing |

## Project Structure

```text
Aptitude-Question-Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    ├── Screenshot 1
    ├── Screenshot 2
    ├── Screenshot 3
    └── ...
```

## Prerequisites

- Python 3.10 or above
- Ollama installed
- Git (optional, for cloning the repository)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Shaun018/Aptitude-Question-Generator.git
cd Aptitude-Question-Generator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```cmd
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Ollama model

Install Ollama from https://ollama.com/ and run:

```bash
ollama pull qwen2.5:3b
```

### 5. Start Ollama

Ensure the Ollama service is running. If necessary, open another terminal and execute:

```bash
ollama serve
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`

## How to Use

1. Open the application in your browser.
2. Select an aptitude topic.
3. Choose the difficulty level.
4. Select the number of questions.
5. Click **Generate Questions**.
6. Attempt the multiple-choice questions.
7. Use **Show Solution** to view explanations.
8. Click **Submit Quiz** to calculate your score and accuracy.
9. Generate a new quiz to continue practising.

## Testing

The application was tested with the following configurations:

| Test | Topic | Difficulty | Questions |
|---|---|---|---:|
| 1 | Percentages | Easy | 3 |
| 2 | Profit and Loss | Medium | 5 |
| 3 | Time and Work | Hard | 3 |
| 4 | Logical Reasoning | Medium | 5 |
| 5 | Number Series | Hard | 5 |

## Screenshots

Application screenshots are available in the `screenshots/` directory.

## Limitations

- Question generation speed depends on available system resources.
- Generated answers should be verified for correctness.
- Ollama must be running locally for the application to work.

## Future Enhancements

- User authentication and quiz history.
- Timed aptitude assessments.
- Performance analytics and progress tracking.
- More examination-specific question categories.
- Improved question and answer validation.

## Author

**Shaun Sasmeet Kalokhe**  
B.Tech – Computer Science and Engineering (AI & Analytics)

## GitHub Repository

https://github.com/Shaun018/Aptitude-Question-Generator
