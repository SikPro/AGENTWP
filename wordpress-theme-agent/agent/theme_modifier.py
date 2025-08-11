import openai

def modify_theme(theme_code: str, modification_prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sei un esperto sviluppatore di temi WordPress."},
            {"role": "user", "content": f"Questo è il codice di un tema WordPress:\n{{theme_code}}\n\nModifica in questo modo: {{modification_prompt}}"}
        ]
    )
    return response['choices'][0]['message']['content']
