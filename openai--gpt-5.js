import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "Your-API-Key",
});

const response = openai.responses.create({
  model: "gpt-5-nano",
  input: "write a haiku about ai",
  store: true,
});

response.then((result) => console.log(result.output_text));