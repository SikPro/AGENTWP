from agent.theme_generator import generate_theme
from agent.theme_modifier import modify_theme

if __name__ == "__main__":
    # Esempio di generazione di un tema
    theme_code = generate_theme("Tema minimalista per blog")
    print(theme_code)
    # Esempio di modifica di un tema
    modified_code = modify_theme(theme_code, "Aggiungi footer personalizzato")
    print(modified_code)