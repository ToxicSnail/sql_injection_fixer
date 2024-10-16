# sql_injection_fixer/main.py

from analyzer import find_sql_injections
from fixers import fix_sql_injections

def main():
    target_path = '.'  # Текущая директория

    # Шаг 1: Анализ кода на наличие SQL-инъекций
    vulnerabilities = find_sql_injections(target_path)

    if vulnerabilities:
        print("Найдены потенциальные уязвимости:")
        for vuln in vulnerabilities:
            print(f"Файл: {vuln['file']}, Строка: {vuln['lineno']}")
        # Шаг 2: Автофиксация уязвимостей
        fix_sql_injections(vulnerabilities)
        print("Уязвимости исправлены.")
    else:
        print("Уязвимости не обнаружены.")

if __name__ == "__main__":
    main()