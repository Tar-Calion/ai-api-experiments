from vertexai.preview.generative_models import GenerativeModel, Part
# import Content
from vertexai.preview.generative_models import Content


def multiturn_generate_content(user_input):
    config = {
        "max_output_tokens": 200,
        "temperature": 0.9,
        "top_p": 1
    }

    response = chat.send_message(user_input, generation_config=config)

    print(chat.history)
    print(response.candidates[0].content.parts[0].text)


model = GenerativeModel("gemini-pro")
chat = model.start_chat(
    history=[Content(role="user", parts=[Part.from_text("This is your assignment for this conversation: You say \"foo\" instead of three and \"bar\" instead of five")]),
             Content(role="model", parts=[Part.from_text(
                 "Understood. I will say \"foo\" instead of three and \"bar\" instead of five. For example instead of saying 3 + five is eight, I will say foo + bar is eight.")]),
             Content(role="user", parts=[Part.from_text("Count to ten")]),
             Content(role="model", parts=[Part.from_text("one, two, foo, four, bar, six, seven, eight, nine, ten")]),
             ],
)

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    multiturn_generate_content(user_input)
