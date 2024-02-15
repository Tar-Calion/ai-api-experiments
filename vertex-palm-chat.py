import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair


vertexai.init(project="rugged-sunbeam-414218",
              location="us-central1"
              )
chat_model = ChatModel.from_pretrained("chat-bison")


chat = chat_model.start_chat(
    context="""You are a wannabe phylosofer. Your answers are nebulous and vague, never to the point. You escape the question by asking another question or by giving a vague answer""",
    examples=[],
    max_output_tokens=250,
    temperature=0.9,
    top_p=1,

)

while True:
    message = input("You: ")
    if message == "exit":
        break
    response = chat.send_message(message)
    print(f"VertexAI: {response.text}")
