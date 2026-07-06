 Emotion-Detection-Learning-Support-Engine

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

9. Prepare Project Folder Structure

Project folder structure is prepared.

Folders:
- data
- models
- src
- app
- notebooks

These folders are used to keep project files in the right place.

10. Kaggle Setup

### Enable GPU
- Open the Kaggle Notebook.
- Go to **Settings**.
- Select **GPU** as the Accelerator.
- Save the settings.

### Install Required Libraries
Install the required Python libraries before running the project.

Example:
```python
!pip install tensorflow opencv-python matplotlib numpy pandas

11. Data Preprocessing & Tokenization

- Loaded the dataset.
- Checked and removed missing values (if any).
- Cleaned the text by removing special characters and extra spaces.
- Converted all text to lowercase.
- Removed unnecessary words (stop words), if required.
- Performed tokenization to split text into individual words.
- Prepared the processed data for model training.

12. BiLSTM Model Training

- Created the BiLSTM model.
- Added all required layers.
- Compiled the model.
- Trained it using the training data.
- Checked the accuracy and loss after each epoch.
- Saved the trained model.

13. Domain-Adaptive Fine-Tuning

Is step mein model ko hamare project ke domain ke data par aur train kiya gaya. Isse model ko domain se related words aur sentence pattern ko samajhne mein madad mili.

- Domain-specific dataset ko prepare kiya.
- Data ko clean karke training ke liye use kiya.
- Pre-trained model ko is data par fine-tune kiya.
- Training ke baad model ko save kiya aur next step ke liye use kiya.

Is process se model ki performance aur prediction accuracy mein improvement dekhne ko mila.

14. BERT Model Fine-Tuning

- Loaded the pre-trained BERT model.
- Used the processed training and validation data.
- Fine-tuned the model using the training dataset.
- Monitored training and validation performance.
- Saved the trained model for testing and future use.

15. Model Export & Local Integration

Training complete hone ke baad model ko save kiya gaya taaki future me use kiya ja sake. Saved model ko local system me load karke testing aur prediction kiya gaya.

### Model Export  
Model ko trained weights ke saath save kiya gaya hai (jaise `.h5`, `.pkl` ya `.pt` format). Is file me model ki architecture aur learned parameters dono store hote hain.

### Local Integration  
Saved model ko local environment me integrate karke run kiya gaya.

**Steps:**
- Model file ko project folder me add kiya  
- Required libraries install ki  
- Model ko load karke sample input par test kiya  
- Output verify kiya ki model sahi kaam kar raha hai  

### Testing  
Model ko local system par run karke predictions check kiye gaye taaki ensure ho sake ki model properly work kar raha hai  

16. Text Preprocessing & Keyword Enhancement

Is step me raw text ko clean kiya gaya hai. Text ko lowercase me convert karke punctuation, stopwords aur unnecessary words remove kiye gaye. Uske baad tokenization ki help se text ko split kiya gaya.

Important keywords ko identify karke TF-IDF ke through highlight kiya gaya taaki model ko useful information mil sake.


17.BiLSTM Classifier (5-Class Softmax)

A BiLSTM model was used to classify text into five emotion categories. The final layer uses Softmax activation to predict the most suitable emotion label for each input.

18. BERT Classifier with Class Weighting & Keyword Adjustments

A BERT classifier was used for emotion detection. Class weighting was applied to handle imbalanced data, and keyword adjustments were added to improve prediction accuracy.

19. Mixed-Emotion Detection (≥15% Secondary Scores)
The system can detect multiple emotions in a single text. If a secondary emotion has a confidence score of 15% or more, it is also included in the prediction.

20. Unified Prediction Schema
The project uses a unified prediction schema to keep the output format consistent for all emotion detection models. The prediction includes the primary emotion, confidence score, and secondary emotions (if available). This common structure makes the results easy to understand and helps integrate different models into a single system.