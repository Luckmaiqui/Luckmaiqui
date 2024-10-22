import datetime
import re
import subprocess

# Data de nascimento completa (ano, mês, dia)
birth_date = datetime.date(1995, 10, 22)  # Exemplo: 22 de outubro de 1995

# Data atual
today = datetime.date.today()

# Cálculo da idade: verificar se já fez aniversário este ano
age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1  # Ainda não fez aniversário este ano

# Caminho para o arquivo README
readme_path = 'README.md'

# Abrir o arquivo README
with open(readme_path, 'r') as file:
    readme_content = file.read()

# Substituir a idade antiga pela nova (buscando por uma linha "Idade: <número>")
new_readme_content = re.sub(r'Idade: \d+', f'Idade: {age}', readme_content)

# Escrever as alterações no README
with open(readme_path, 'w') as file:
    file.write(new_readme_content)

# Comandos Git para fazer commit e enviar as alterações
subprocess.run(['git', 'add', readme_path])
subprocess.run(['git', 'commit', '-m', f'Atualizando idade para {age}'])
subprocess.run(['git', 'push'])
