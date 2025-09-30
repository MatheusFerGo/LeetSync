# generate_readme.py
import os
import re
from datetime import datetime

# --- Configuração ---
LANGUAGES = {
    "Python": "🐍",
    "CSharp": "💻",
    "SQL": "🗄️"
}
DIFFICULTIES = ["Easy", "Medium", "Hard"]

# --- Funções Auxiliares ---
def get_link_from_readme(path):
    """Extrai o primeiro link do LeetCode de um arquivo README.md."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                match = re.search(r'href="([^"]+leetcode.com[^"]+)"', line)
                if match:
                    return match.group(1)
    except FileNotFoundError:
        return None
    return None

# --- Lógica Principal ---
def main():
    solutions = []
    # 1. Coletar dados de todas as soluções
    for lang, emoji in LANGUAGES.items():
        for diff in DIFFICULTIES:
            path = os.path.join(lang, diff)
            if os.path.isdir(path):
                for problem_folder in sorted(os.listdir(path)):
                    problem_path = os.path.join(path, problem_folder)
                    readme_path = os.path.join(problem_path, "README.md")
                    
                    solutions.append({
                        "name": problem_folder.replace('-', ' ').title(),
                        "lang_name": lang,
                        "lang_emoji": emoji,
                        "diff": diff,
                        "link": get_link_from_readme(readme_path) or "#"
                    })

    # 2. Calcular estatísticas
    stats = {diff: 0 for diff in DIFFICULTIES}
    for s in solutions:
        stats[s['diff']] += 1
    total_solved = len(solutions)

    # 3. Construir o conteúdo do README
    readme_content = f"""# 🧩 Soluções de Exercícios - LeetCode

Este repositório contém minhas soluções para diversos problemas da plataforma LeetCode, servindo como um registro do meu progresso e aprendizado contínuo em algoritmos e estruturas de dados.

---

### 📊 Progresso Atual

| Categoria | Problemas Resolvidos |
| :--- | :---: |
| <g-emoji>🟢</g-emoji> **Fácil** | {stats['Easy']} |
| <g-emoji>🟠</g-emoji> **Médio** | {stats['Medium']} |
| <g-emoji>🔴</g-emoji> **Difícil** | {stats['Hard']} |
| **Total** | **{total_solved}** |

*(Atualizado pela última vez em: {datetime.now().strftime('%Y-%m-%d')})*

---

### 📚 Lista de Soluções\n\n"""

    # Agrupar soluções por linguagem
    solutions_by_lang = {lang: [] for lang in LANGUAGES}
    for s in solutions:
        solutions_by_lang[s['lang_name']].append(s)

    for lang, lang_solutions in solutions_by_lang.items():
        if lang_solutions:
            readme_content += f"### {LANGUAGES[lang]} {lang}\n"
            for s in lang_solutions:
                readme_content += f"- [{s['name']} `({s['diff']})`]({s['link']})\n"
            readme_content += "\n"

    # 4. Escrever o novo README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"✅ README.md gerado com sucesso com {total_solved} soluções.")

if __name__ == "__main__":
    main()
