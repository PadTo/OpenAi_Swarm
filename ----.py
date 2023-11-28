from openai import OpenAI
import os
import time
import pytesseract
from PIL import Image


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Directing the path to the directory
directory = r"C:\Users\tpade\Desktop\Problems"


# Import the AI assistant by their ID's
Math_Solver_Assistant_id = "asst_idxuBlMCpCpExTOlOyoIrkA0"
Math_Solution_Checker_Assistant_id = "asst_L0lVBlRPNOjTozC9BZg6WauR"
Latex_Converter_Assistant_id = "asst_dcQ7IlaiF89KtrakuKusFeh9"
Latex_Translation_Assistant_id = "asst_OFxelfshR3LDCYsIUCMcSc9H"

# file_ids = {}
# file_names = []

# files = client.files.list()

# for file in files.data:
#    file_ids[file.filename] = file.id
#    file_names.append(file.filename)


file_names = os.listdir(directory)

for filename in file_names:
    if filename.endswith(".jpg"):
        file_path = os.path.join(directory, filename)

        with Image.open(file_path) as img:
            text = pytesseract.image_to_string(img)

        thread = client.beta.threads.create()
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=text.strip()
        )

        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=Math_Solver_Assistant_id,
            instructions="Please do as the user asks, the user has a premium account"
        )

        status = False
        while not status:
            time.sleep(5)

            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )

            if run_status.status == "completed":
                status = True

        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )

        # Retrieve and print the messages from the assistant
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        for msg in messages.data:
            if msg.role == "assistant":
                print(
                    f"Assistant's response to {filename}: {msg.content[0]['text']['value']}")
