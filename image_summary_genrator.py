import os
import base64
from groq import Groq

# === CONFIGURATION ===
FOLDER_PATH = "financial_charts-dataset"
MODEL_ID = "meta-llama/llama-4-scout-17b-16e-instruct"

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


for filename in os.listdir(FOLDER_PATH):
    if filename.lower().endswith(".png"):
        image_path = os.path.join(FOLDER_PATH, filename)
        base64_image = encode_image(image_path)


        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "You are a financial analyst. Analyze this stock price chart and summarize it in 4–5 lines. "
                            "Explain key trends and the relationship between X (time) and Y (stock price)."
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]

        try:
            # The API call
            response = client.chat.completions.create(
                model=MODEL_ID,
                messages=messages,
                temperature=0.7,
                top_p=1,
                stream=False
            )

            summary = response.choices[0].message.content.strip()

            # Writting summary to corresponding file
            out_filename = filename.replace(".png", "_summary.txt")
            out_path = os.path.join(FOLDER_PATH, out_filename)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(summary)

            print(f"Image summarized: {filename} → {out_filename}")
        except Exception as e:
            print(f" Failed to summarize {filename}: {e}")
