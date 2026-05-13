import json
import urllib.request
import urllib.parse
from pathlib import Path
import os

params = urllib.parse.urlencode({
    "latitude": 33.64054,
    "longitude": -117.83891,
    "current": "apparent_temperature,precipitation_probability,relative_humidity_2m",
})
endpoint = f"https://api.open-meteo.com/v1/forecast?{params}"

with urllib.request.urlopen(endpoint) as resp:
    data = json.loads(resp.read().decode("utf-8"))

# print(data['current']['apparent_temperature'])
print(data['current']['relative_humidity_2m'])


def load_api_key(key_file: Path) -> str:
    env_key = os.environ.get("GEMINI_API_KEY","").strip()
    if env_key:
        return env_key
    if key_file.is_file():
        return json.loads(key_file.read_text())["GEMINI_API_KEY"]
    else:
        raise FileNotFoundError(f"Key file not found: {key_file}")
    raise ValueError("GEMINI_API_KEY is not set and key file not found.") 



url = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent"
)

body = {
    "contents": [
        {"parts": [{"text": "Explain diffusion models in cognitive science in one sentence."}]}
    ]
}
body_bytes = json.dumps(body).encode("utf-8")

req = urllib.request.Request(
    url,
    data=body_bytes,
    headers={
        "Content-Type": "application/json",
        "x-goog-api-key": load_api_key(Path('../../workspace/secrets/.gitignore')),
    },
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    response_data = json.loads(resp.read().decode("utf-8"))

text = response_data["candidates"][0]["content"]["parts"][0]["text"]
print(text)