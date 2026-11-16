import sys
from math_utils import decagonal_number
from fibonacci_module import calculate_fibonacci

MAX_N = 100_000

def print_usage():
    print("Использование: python3 main.py <команда>")
    print("Доступные команды:")
    print("  fib   - вычислить число Фибоначчи")
    print("  dec   - вычислить десятиугольное число")
    print(f"Ограничение: 0 <= N <= {MAX_N}")
    print("После запуска введите число N и нажмите Enter.")
    print("Допускаются только цифры 0-9, без букв и других символов.")

def parse_number(raw_input: str) -> int:
    # Разрешаем только цифры. Пробелы по краям — не ошибка.
    cleaned = raw_input.strip()

    if not cleaned:
        raise ValueError("пустая строка (введите число)")

    if not cleaned.isdigit():
        raise ValueError(f"'{raw_input}' содержит недопустимые символы (разрешены только цифры 0-9)")

    n = int(cleaned)

    if n > MAX_N:
        raise ValueError(f"Число {n} слишком большое (максимум {MAX_N})")

    return n

def main():
    if len(sys.argv) != 2:
        print("Ошибка: Неверное количество аргументов.")
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command not in ('fib', 'dec'):
        print(f"Ошибка: Неизвестная команда '{command}'.")
        print_usage()
        sys.exit(1)

    try:
        raw_input = input("Введите число N: ")
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван.")
        sys.exit(1)

    try:
        n = parse_number(raw_input)
    except ValueError as e:
        print(f"Ошибка ввода: {e}.")
        sys.exit(1)

    try:
        if command == 'fib':
            result = calculate_fibonacci(n)
            print(f"Число Фибоначчи для N={n}: {result}")
        else:  # command == 'dec'
            result = decagonal_number(n)
            print(f"Десятиугольное число для N={n}: {result}")
    except ValueError as e:
        print(f"Ошибка вычисления: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
