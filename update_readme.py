import os
from datetime import datetime

def replace_between_robust(content, start_tag, end_tag, new_value):
    """Usa split() para substituir o conteúdo de forma segura, sem quebrar a formatação."""
    try:
        before, after = content.split(start_tag, 1)
        _, after = after.split(end_tag, 1)
        return before + start_tag + str(new_value) + end_tag + after
    except ValueError:
        print(f"Aviso: Marcadores '{start_tag}' e '{end_tag}' não encontrados. Pulando substituição.")
        return content

# --- Lógica Principal ---

language_dirs = ["Python", "SQL", "CSharp"]
difficulties = ["Easy", "Medium", "Hard"]
counts = {diff: 0 for diff in difficulties}

for lang_dir in language_dirs:
    if os.path.isdir(lang_dir):
        for difficulty in difficulties:
            path = os.path.join(lang_dir, difficulty)
            if os.path.isdir(path):
                num_files = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
                counts[difficulty] += num_files

total_solved = sum(counts.values())

try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
except FileNotFoundError:
    print("Erro: README.md não encontrado!")
    exit(1)

# Usa a função robusta com os marcadores de comentário HTML
readme_content = replace_between_robust(readme_content, "", "", counts['Easy'])
readme_content = replace_between_robust(readme_content, "", "", counts['Medium'])
readme_content = replace_between_robust(readme_content, "", "", counts['Hard'])
readme_content = replace_between_robust(readme_content, "", "", total_solved)

# Atualiza a data para um formato universal e seguro
current_date = datetime.now().strftime("%Y-%m-%d")
readme_content = replace_between_robust(readme_content, "", "", current_date)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"README.md atualizado com sucesso: {total_solved} problemas no total.")
