import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генератор, який знаходить у тексті всі дійсні числа
    та повертає їх як послідовність значень.
    """
    pattern = r'\s(-?\d+\.\d+)\s'  # Регулярний вираз для знаходження чисел
    for match in re.finditer(pattern, f' {text} '):  # Додаємо пробіли для коректного знаходження чисел
        yield float(match.group(1))

def sum_profit(text: str, func: Callable):
    """
    Функція підсумовує всі числа, знайдені генератором.
    """
    return sum(func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

