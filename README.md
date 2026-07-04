 Emotion-Detection-Learning-Support-Engine
Skill wallet group project Emotion Detection &amp; Learning Support Engine

1. Entity-Relationship (ER) diagram for the AI# Entity-Relationship (ER) Diagram for AI Learning Management System

## Entities
- Student
- Course
- Instructor
- Lesson
- Quiz
- Certificate

## Relationships
- Student enrolls in Course
- Instructor teaches Course
- Course contains Lesson
- Course contains Quiz
- Student receives Certificate

2. Links

- GitHub Repository: https://github.com/keshprasadbca2024-collab/Emotion-Detection-Learning-Support-Engine https://aistudio.google.com/app/apikey
- Python: https://www.python.org/downloads/

3. Project Workflow

1. Start the AI Learning Management System.
2. User signs up or logs in.
3. User selects a course.
4. User studies lessons and learning materials.
5. User attempts quizzes.
6. AI analyzes the user's performance.
7. AI provides personalized feedback and learning recommendations.
8. User completes the course.
9. The system generates a certificate.

4. Obtain Gemini API Key

1. Open Google AI Studio.
2. Sign in with your Google account.
3. Click on "Create API Key".
4. Copy the generated API Key.
5. Store the API Key securely and do not share it publicly.


5.  Install Python & Create Virtual Environment

### Install Python
1. Download Python from https://www.python.org/downloads/
2. Install Python and enable "Add Python to PATH".

### Create Virtual Environment
1. Open Terminal or Command Prompt.
2. Run:
   python -m venv venv
3. Activate the virtual environment.
4. Install the required packages using:
   pip install -r requirements.txt


6. Install Project Dependencies

After creating and activating the virtual environment, install all required project packages using the following command:

```bash
pip install -r requirements.txt
```

This command installs all the libraries required to run the project successfully.


7. Create the .env Configuration File

Create a file named `.env` in the project folder.

Add the following line:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

Do not share your API key publicly.


8. Verify Model and Data Directories

The project structure has been verified.

Required directories:
- data/
- models/
- notebooks/
- src/
- app/

These directories will be used for dataset storage, trained models, source code, notebooks, and the application.