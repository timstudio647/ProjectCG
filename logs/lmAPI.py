from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
)

models = client.models.list()
model_id = "google/gemma-4-12b-qat"

stream = client.chat.completions.create(
    model=model_id,
    messages=[
        {"role": "user", "content": "hey! hows your day"}
    ],
    temperature=0.75,
    stream=True,
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)





***
Current issues:
  1. The model takes way too long to start responding
  2. The model in this api does not have memory available
***
