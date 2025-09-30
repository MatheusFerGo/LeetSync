import os
from datetime import datetime

# --- NOVA FUNÇÃO AUXILIAR, MAIS ROBUSTA ---
def replace_between_robust(content, start_tag, end_tag, new_value):
    """
    Usa split() para substituir o conteúdo de forma segura, sem quebrar a formatação.
    """
    try:
        # Divide o conteúdo em duas partes, antes e depois da tag de início
        before, after = content.split(start_tag)
        # Divide a segunda parte para isolar o conteúdo antigo
        _, after = after.split(end_tag)
        # Remonta a string com o novo valor
        return before + start_tag + str(new_value) + end_tag + after
    except ValueError:
        print(f"Aviso: Não foi possível encontrar os marcadores '{start_tag}' e '{end_tag}'. Pulando esta substituição.")
        return content

# --------------------------------------------------------------------

# A lógica de contagem de arquivos permanece a mesma
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

# Lê o conteúdo do README.md
try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
except FileNotFoundError:
    print("Erro: README.md não encontrado!")
    exit(1)

# Usa a nova função robusta para substituir os valores
readme_content = replace_between_robust(readme_content, "", "", counts['Easy'])
readme_content = replace_between_robust(readme_content, "", "", counts['Medium'])
readme_content = replace_between_robust(readme_content, "", "", counts['Hard'])
readme_content = replace_between_robust(readme_content, "", "", total_solved)

# Atualiza a data para um formato universal e seguro
current_date = datetime.now().strftime("%Y-%m-%d")
readme_content = replace_between_robust(readme_content, "", "", current_date)

# Escreve o novo conteúdo de volta no README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"README.md atualizado com sucesso: {total_solved} problemas no total.")
