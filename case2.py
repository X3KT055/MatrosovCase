import math

def calculate_factorial(n: int) -> int:
    return math.factorial(n)


def main() -> None:
    print("Программа вычисления факториала положительного целого числа.")

    while True:
        try:
            # Ввод числа
            user_input = input("Введите положительное целое число: ")
            number = int(user_input)

            # Проверка числа
            if number <= 0:
                print("Ошибка: число должно быть положительным (больше нуля). Попробуйте ещё раз.")
                continue

            # Вычисление
            result = calculate_factorial(number)

            # Вывод результата
            print(f"Факториал числа {number} равен {result}")
            break

        except ValueError:
            # Обработка ошибок
            print("Ошибка: введено нечисловое значение. Пожалуйста, введите целое число.")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}. Попробуйте снова.")


if __name__ == "__main__":
    main()