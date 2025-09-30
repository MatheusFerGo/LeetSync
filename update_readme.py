import os
from datetime import datetime

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
current_date = datetime.now().strftime("%Y-%m-%d")

# Dicionário para mapear marcadores para seus novos valores
replacements = {
    "EASY_COUNT": counts['Easy'],
    "MEDIUM_COUNT": counts['Medium'],
    "HARD_COUNT": counts['Hard'],
    "TOTAL_COUNT": total_solved,
    "DATE": current_date
}

new_readme_lines = []
readme_path = "README.md"

try:
    with open(readme_path, "r", encoding="utf-8") as f:
        # Lê o arquivo linha por linha
        for line in f:
            new_line = line
            # Verifica se algum de nossos marcadores está na linha
            for key, value in replacements.items():
                start_marker = f""
                end_marker = f""
                
                if start_marker in line and end_marker in line:
                    # Se encontrarmos os marcadores, reconstruímos a linha inteira
                    # Pegamos a parte da linha ANTES do marcador de início
                    prefix = line.split(start_marker)[0]
                    # Pegamos a parte da linha DEPOIS do marcador de fim
                    suffix = line.split(end_marker)[1]
                    
                    # Remontamos a linha com o novo valor no meio
                    new_line = prefix + start_marker + str(value) + end_marker + suffix
                    break # Vamos para a próxima linha do arquivo
            
            new_readme_lines.append(new_line)

except FileNotFoundError:
    print(f"Erro: {readme_path} não encontrado!")
    exit(1)

# Escreve o novo conteúdo (linha por linha) de volta no arquivo
with open(readme_path, "w", encoding="utf-8") as f:
    f.writelines(new_readme_lines)

print(f"README.md atualizado com sucesso: {total_solved} problemas no total.")
