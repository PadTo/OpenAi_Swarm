from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

aassistant_1 = client.beta.assistants.create(
    name="Assistant for Analyzing and Solving Mathematical Problems from Photos",
    instructions="Analyze the provided images of mathematical problems, extract and interpret the text using OCR, and solve the problems. Provide detailed solutions in a clear and understandable format.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)


assistant_2 = client.beta.assistants.create(
    name="Assistant for Checking Solutions for Mistakes",
    instructions="Review the solutions provided for mathematical problems. Check for accuracy and correctness. Flag any errors or inconsistencies and provide feedback on what needs to be corrected.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

assistant_3 = client.beta.assistants.create(
    name="Assistant for Compiling Answers in LaTeX",
    instructions="Format the provided solutions to mathematical problems in LaTeX. Ensure that the solutions are well-structured, clear, and adhere to LaTeX formatting standards. Pay attention to the presentation of mathematical equations and text.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

assistant_4 = client.beta.assistants.create(
    name="Assistant for Translating Solutions to Lithuanian and Presenting in LaTeX",
    instructions="Translate the provided LaTeX document with mathematical solutions from English to Lithuanian. Maintain the integrity of the LaTeX formatting and ensure the mathematical content is accurately translated. Compile the final document in a clear and professional format.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)
