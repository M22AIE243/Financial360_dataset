import os
from groq import Groq

# === CONFIGURATION ===
FOLDER_PATH = "financial_charts-dataset"
MODEL_ID = "llama-3.1-8b-instant"

# Initializing Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


for filename in os.listdir(FOLDER_PATH):
    if filename.endswith("_summary.txt"):
        file_path = os.path.join(FOLDER_PATH, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()


        messages = [
            {"role": "system", "content": "You are a financial analyst."},
            {
                "role": "user",
                "content": (
                    "Summarize the following stock trading data into 4–5 concise lines. "
                    "Highlight key trends, performance, volume changes, and price movements.\n\n"
                    f"{text}"
                )
            }
        ]

        try:
            # request to Groq API
            response = client.chat.completions.create(
                model=MODEL_ID,
                messages=messages,
                temperature=0.5,
                top_p=1,
                stream=False
            )

            summary = response.choices[0].message.content


            new_filename = filename.replace("_summary.txt", "_summary_updated.txt")
            new_path = os.path.join(FOLDER_PATH, new_filename)

            with open(new_path, "w", encoding="utf-8") as f:
                f.write(summary)

            print(f" Summarized: {filename} → {new_filename}")
        except Exception as e:
            print(f"Error with {filename}: {e}")
