import datetime
import re
import subprocess

birth_date = datetime.date(2003, 10, 20)


today = datetime.date.today()

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1 

readme_path = 'README.md'

with open(readme_path, 'r') as file:
    readme_content = file.read()

new_readme_content = re.sub(r'<h3>☼ \d+ Anos</h3>', f'<h3>☼ {age} Anos</h3>', readme_content)

with open(readme_path, 'w') as file:
    file.write(new_readme_content)

subprocess.run(['git', 'add', readme_path])
subprocess.run(['git', 'commit', '-m', f'Atualizando idade para {age} anos'])
subprocess.run(['git', 'push'])
