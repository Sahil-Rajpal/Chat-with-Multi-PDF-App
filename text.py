from google.generativeai import list_models

print("Available models:")
for model in list_models():
    print(model.name)
