import os
from datetime import datetime
import locale

# --- FUNÇÃO AUXILIAR PARA SUBSTITUIR TEXTO ---
def replace_between(content, start_tag, end_tag, new_value):
    """
    Encontra o texto entre duas tags e o substitui por um novo valor.
    """
    try:
        start_index = content.index(start_tag) + len(start_tag)
        end_index = content.index(end_tag)

        # Constrói a nova string
        new_content = content[:start_index] + str(new_value) + content[end_index:]
        return new_content
    except ValueError:
        print(f"Aviso: As tags '{start_tag}' ou '{end_tag}' não foram encontradas. Pulando esta substituição.")
        return content

# --------------------------------------------------------------------

# Garante que o mês seja escrito em português
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    print("Locale pt_BR.UTF-8 não suportado, usando o padrão.")

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

# Usa a nova função para substituir os valores
readme_content = replace_between(readme_content, "", "", counts['Easy'])
readme_content = replace_between(readme_content, "", "", counts['Medium'])
readme_content = replace_between(readme_content, "", "", counts['Hard'])
readme_content = replace_between(readme_content, "", "", total_solved)

# Atualiza a data
current_date = datetime.now().strftime("%d de %B de %Y")
readme_content = replace_between(readme_content, "", "", current_date)

# Escreve o novo conteúdo de volta no README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"README.md atualizado com sucesso: {total_solved} problemas no total.")
