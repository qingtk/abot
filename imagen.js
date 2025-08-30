import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const response = await ai.models.generateImages({
    model: 'imagen-4.0-generate-001',
    prompt: 'Robot holding a red apple and dancing',
    config: {
      numberOfImages: 4,
    },
  });

  let idx = 1;
  for (const generatedImage of response.generatedImages) {
    let imgBytes = generatedImage.image.imageBytes;
    const buffer = Buffer.from(imgBytes, "base64");
    fs.writeFileSync(`imagen-${idx}.png`, buffer);
    idx++;
  }
}

main();

/* ApiError: {"error":{"code":400,"message":"Imagen API is only accessible to billed users at this time.","status":"INVALID_ARGUMENT"}} */