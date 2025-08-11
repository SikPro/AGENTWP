from agent.theme_modifier import modify_theme

original_theme = "/* Codice esempio di tema WordPress */"
modified = modify_theme(original_theme, "Aggiungi una sezione contatti in homepage")
print(modified)