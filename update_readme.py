import os
import re
from datetime import datetime
import locale

# Garante que o mês seja escrito em português
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    print("Locale pt_BR.UTF-8 not supported, using default.")

# Diretórios das linguagens a serem escaneadas
language_dirs = ["Python", "SQL", "CSharp"]
difficulties = ["Easy", "Medium", "Hard"]
counts = {diff: 0 for diff in difficulties}

# Loop para contar os arquivos em cada subdiretório de dificuldade
for lang_dir in language_dirs:
    if os.path.isdir(lang_dir):
        for difficulty in difficulties:
            path = os.path.join(lang_dir, difficulty)
            if os.path.isdir(path):
                # Conta apenas arquivos, ignorando subdiretórios se houver
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


# Substitui os valores de contagem usando os marcadores
readme_content = re.sub(r"()(.*)()", f"\\1{counts['Easy']}\\3", readme_content)
readme_content = re.sub(r"()(.*)()", f"\\1{counts['Medium']}\\3", readme_content)
readme_content = re.sub(r"()(.*)()", f"\\1{counts['Hard']}\\3", readme_content)
readme_content = re.sub(r"()(.*)()", f"\\1{total_solved}\\3", readme_content)

# Atualiza a data da última execução
current_date = datetime.now().strftime("%d de %B de %Y")
readme_content = re.sub(r"()(.*)()", f"\\1{current_date}\\3", readme_content)

# Escreve o novo conteúdo de volta no README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"README.md atualizado com sucesso: {total_solved} problemas no total.")