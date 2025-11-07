def caching_fibonacci():
    # створюємо словник для кешування обчислених значень
    cache = {}

    def fibonacci(n):
        # базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # перевіряємо чи значення вже в кеші
        if n in cache:
            return cache[n]
        
        # рекурсивно обчіслюємо значення fibonacci та зберігаємо його в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

# уникнення небажаного виконання при імпорті
if __name__ == "__main__":
    # отримуємо функцію fibonacci з кешуванням у змінну
    fib = caching_fibonacci()

    # використовуємо  функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  
    print(fib(15))  
    print(fib(10)) 