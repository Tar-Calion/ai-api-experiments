import openai
import dotenv
import os
import wikipedia

max_length = 2000


def get_random_wikipedia_page():
    for i in range(5):

        wikipedia.set_lang("de")
        random_title = wikipedia.random(pages=1)
        page = wikipedia.page(random_title)
        if len(page.content) > 1000:
            return page
    raise ValueError("No page found with more than 1000 characters")


# load the wikipedia page
page = get_random_wikipedia_page()
print(page.title)
print(page.content[:max_length])

# summarize the page
dotenv.load_dotenv(override=True)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_message = "Your goal is to summarize and simplify the wikipedia article in German. The summary should be 5 sentences long."
user_message = page.content[:max_length]

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ],
    max_tokens=1000
)

# reason of the completion
print(completion.choices[0].finish_reason)

# print the summary
print("Summary:")
print(completion.choices[0].message.content)
