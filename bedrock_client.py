import boto3
import json
import re
import os

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
)

def invoke_llm(prompt, temperature=0.3, max_tokens=400):
    response = client.invoke_model(
        modelId="google.gemma-3-4b-it",
        body=json.dumps({
            "messages": [{"role": "user", "content": prompt}],
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens
            }
        })
    )

    raw = json.loads(response["body"].read())
    text = raw["choices"][0]["message"]["content"]
    cleaned = re.sub(r"```json|```", "", text).strip()
    return json.loads(cleaned)
