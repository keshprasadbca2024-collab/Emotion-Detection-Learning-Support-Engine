import csv
import os
from datetime import datetime

FILE_NAME = "logs/history.csv"


def save_to_csv(field, problem, emotion, confidence, response):

    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Date",
                "Field",
                "Problem",
                "Emotion",
                "Confidence",
                "AI Response"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            field,
            problem,
            emotion,
            confidence,
            response
        ])
