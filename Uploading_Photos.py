from openai import OpenAI
import os

# Import OpenAI key
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Directing the path to the directory
directory = r"C:\Users\tpade\Desktop\Problems"

count = 0
for filename in os.listdir(directory):
    if filename.startswith('S') and filename.endswith('.jpg'):

        file_path = os.path.join(directory, filename)
        file = client.files.create(
            file=open(file_path, "rb"),
            purpose="assistants"
        )

        file_id = file.id
        print(f"Uploaded file: {filename}, File ID: {file_id}")

    count += 1
    if count == 1:
        break
