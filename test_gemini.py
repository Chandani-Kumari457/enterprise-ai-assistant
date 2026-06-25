
print("Program Started")

from config.gemini_config import model

print("Gemini Imported")

response = model.generate_content("Say hello to Chandani")

print("Response Received")

print(response.text)