import sys
from math_utils import decagonal_number
from fibonacci_module import calculate_fibonacci

MAX_N = 100_000

def print_usage():
    print("Использование: python main.py <команда> <число>")
    print("Доступные команды:")
    print("  fib <N>   - вычислить N-е число Фибоначчи")
    print("  dec <N>  - вычислить N-е Десятиугольное число")
    print(f"Ограничение: 0 <= N <= {MAX_N}")
    print("Примечание: буква 'e' в конце числа игнорируется (10e = 10)")

def parse_number(raw_input: str) -> int:
    
    cleaned = raw_input.strip()
    
    cleaned = cleaned.rstrip('eE')
    
    if not cleaned:
        raise ValueError("пустое значение")

    if not cleaned.replace('+', '').replace('-', '').isdigit():
        raise ValueError(f"'{raw_input}' не является числом (ожидаются только цифры 0-9)")
        
    n = int(cleaned)

    if n < 0:
        raise ValueError(f"'{raw_input}' — отрицательное число")

    if n > MAX_N:
        raise ValueError(f"'{raw_input}' слишком большое (максимум {MAX_N})")

    return n

def main():
    if len(sys.argv) != 3:
        print("Ошибка: Неверное количество аргументов.")
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()
    try:
        n = parse_number(sys.argv[2])
        if n < 0:
            raise ValueError
    except ValueError:
        print(f"Ошибка: Аргумент '{sys.argv[2]}' должен быть целым неотрицательным числом.")
        sys.exit(1)

    try:
        if command == 'fib':
            result = calculate_fibonacci(n)
            print(f"Число Фибоначчи для N={n}: {result}")
        elif command == 'dec':
            result = decagonal_number(n)
            print(f"Десятиугольное число для N={n}: {result}")
        else:
            print(f"Ошибка: Неизвестная команда '{command}'.")
            print_usage()
            sys.exit(1)
    except ValueError as e:
        print(f"Ошибка вычисления: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
