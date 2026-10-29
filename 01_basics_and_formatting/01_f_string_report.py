# 1. Мы declare (объявляем) переменные и initialize (инициализируем) их значениями
tester_name = "FedyaQA"
passed_tests = 45
total_tests = 50

# 2. Пишем expression (выражение) внутри placeholder {} для подсчета процента успеха
# Модификатор :.1f округлит результат до одного знака после запятой
report = f"Тестировщик: {tester_name}\nУспешный прогон: {(passed_tests / total_tests) * 100:.1f}%"

# 3. Выводим готовую отформатированную строку в консоль
print(report)
