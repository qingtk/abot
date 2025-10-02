from openai import OpenAI

client = OpenAI(
  api_key="Your-API-Key"
)

response = client.responses.create(
  model="gpt-5-nano",
  input=" ",
  store=True,
)

print(response.output_text);
