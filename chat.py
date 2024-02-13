import openai
import dotenv
import os

dotenv.load_dotenv(override=True)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "Your answers are one word long"},
        {"role": "user", "content": "What are most important logical fallacies?"},
    ],
    max_tokens=15,
    n=15,
    temperature=1

)

print(completion)

# print all answers
print("Answers:")
for choice in completion.choices:
    print(choice.message.content)
