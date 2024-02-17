import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

# This script generates a classified ad in German from one or more images.


def generate_classified_ad(images: list[Part]):
    vertexai.init(project="rugged-sunbeam-414218", location="us-central1")
    model = GenerativeModel("gemini-pro-vision")
    responses = model.generate_content(
        [*images, """Ich möchte den Gegenstand auf diesen Bildern über Kleinanzeigen verkaufen. Erstelle den Text der Anzeige. Beschreibe den Gegenstand / die Gegenstände. Schätze den Verkaufspreis."""],
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.4,
            "top_p": 1,
            "top_k": 32
        },
        safety_settings={
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        },
        stream=True,
    )

    for response in responses:
        print(response.text, end="")


def get_mimetype(image_path: str) -> str:
    lowercase_image_path = image_path.lower()
    if lowercase_image_path.endswith(".png"):
        return "image/png"
    elif lowercase_image_path.endswith(".jpg") or lowercase_image_path.endswith(".jpeg"):
        return "image/jpeg"
    else:
        raise ValueError("Unsupported file type. Supported types are .png, .jpg, .jpeg.")


def get_images(user_input) -> list[Part]:
    images = []
    for image_path in user_input.split(","):
        file = open(image_path.strip(), "rb")
        mime_type = get_mimetype(image_path)
        image = Part.from_data(file.read(), mime_type)
        images.append(image)
    return images


print("Hier können Sie den Text einer Kleinanzeige aus einem oder mehreren Bildern generieren lassen.")

user_input = input("Welches Bild möchten Sie im Prompt nutzen? Mehrere Bilder können durch Kommas getrennt werden.\n")

images = get_images(user_input)

generate_classified_ad(images)
