# =====================================================================
# ТЕМА: РАБОТА СО СТРОКАМИ И СТРОКОВЫЕ МЕТОДЫ В QA AUTOMATION
# =====================================================================

# 1. Escape Characters (Экранирование и сырые строки)
# Используем r"" для путей к файлам, чтобы избежать конфликтов с \n, \t
windows_path = r"C:\new_folder\tests"
log_message = "Элемент \"Вход\" не найден на странице."

print("--- 1. Экранирование ---")
print(f"Путь к файлу: {windows_path}")
print(f"Лог ошибки: {log_message}\n")


# 2. Методы очистки данных (Снятие пробелов и изменение регистра)
raw_username = "\n  feDYa_QA   "
# Применяем цепочку методов (Method Chaining)
clean_username = raw_username.strip().lower()

print("--- 2. Очистка данных ---")
print(f"Очищенный юзернейм: {clean_username}\n")


# 3. Методы верификации / проверок (Assertions)
file_name = "test_report.pdf"
logs = "ERROR: status 500. ERROR: status 404. WARNING: slow down."

is_pdf = file_name.endswith(".pdf")  # Проверка расширения
error_count = logs.count("ERROR")    # Подсчет критических ошибок

print("--- 3. Верификация ---")
print(f"Файл является PDF?: {is_pdf}")
print(f"Количество ошибок в логах: {error_count}")
