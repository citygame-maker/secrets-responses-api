import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY_RESPONSES_API"),
)

file = client.files.create(
    file=open("data/general_game_creation_guide.pdf", "rb"),
    purpose="user_data"
)

response = client.responses.create(
    model="gpt-5-nano",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": "How many phases are there in building a game?",
                }
            ]
        }
    ]
)

print(response.output_text)