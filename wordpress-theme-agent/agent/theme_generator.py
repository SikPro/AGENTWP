import openai

def generate_theme(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sei un esperto sviluppatore di temi WordPress."},
            {"role": "user", "content": f"Crea un tema WordPress: {prompt}"}
        ]
    )
    return response['choices'][0]['message']['content']
