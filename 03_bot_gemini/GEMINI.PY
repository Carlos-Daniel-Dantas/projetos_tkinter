from google import genai


# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyCxGjJu3TILNzi5EkJIkmp-6sR2uQxZd-E")

pergunta = input("Pergunte alguma coisa")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents= input("faça uma pergunta: "))

print(response.text)
