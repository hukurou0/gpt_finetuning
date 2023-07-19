import requests
import secret
from requests import Response

response:Response = requests.get(
    'https://api.openai.com/v1/fine-tunes', headers={'Authorization': f"Bearer {secret.api_key}"})

print(response.json())