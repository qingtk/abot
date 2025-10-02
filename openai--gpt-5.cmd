curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer Your-API-Key" \
  -d '{
    "model": "gpt-5-nano",
    "input": "write a haiku about ai",
    "store": true
  }'
