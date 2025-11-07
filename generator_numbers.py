import re
from typing import Callable, Generator

# функція-генератор для вилучення дійсних чисел з тексту
def generator_numbers(text: str) -> Generator[float, None, None]:
  
    # регулярний вираз для пошуку дійсних чисел , які можуть мати десяткову точку
    pattern = r'\s+(\d+\.?\d*)\s+'
    
    # шукаємо всі відповідності в тексті циклом 
    for match in re.finditer(pattern, text):
        number_str = match.group(1)
        try:
            # конвертуємо знайдене число у тип float та повертаємо його
            number = float(number_str)
            yield number
        except ValueError:
            # пропускаємо некоректні значення
            continue
# функія для обчислення загальної суми чисел у тексті
def sum_profit(text: str, func: Callable) -> float:

    total_amount = 0.0
    # використовуємо генератор для отримання чисел та підсумовуємо їх
    for number in func(text):
        total_amount += number
    return total_amount

# використовуємо з урахування уникнення небажаного виконання при імпорті
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")