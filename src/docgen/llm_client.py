import subprocess

def prompt_ollama(code: str, model="mistral"):
    prompt = f"""
    Analyze the following code and explain:
    1. What this file does
    2. Its main functions or classes
    3. Its purpose in a larger system
    4. Return Mermaid flowchart if possible

    ```ts
    {code}
    ```
    """
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()
