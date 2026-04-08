import asyncio
import time
from genai.ollama_client import call_ollama

async def run_model(model, prompt):
    try:
        start = time.perf_counter()

        response = await asyncio.wait_for(
            call_ollama(model, prompt),
            timeout=40
        )

        end = time.perf_counter()

        return {
            "model": model,
            "response": response,
            "time": round(end - start, 2)
        }

    except Exception:
        return {
            "model": model,
            "response": "Error",
            "time": 999
        }


async def run_all_models(prompt):
    models = ["llama3:instruct", "llama3", "mistral"]

    tasks = [run_model(m, prompt) for m in models]
    return await asyncio.gather(*tasks)