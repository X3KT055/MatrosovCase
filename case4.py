import random

def main() -> None:
    print("Добро пожаловать в игру Угадай число!")
    print("Я загадал целое число от 1 до 100. Попробуйте его отгадать.")

    MAX_ATTEMPTS = 7    # Количество попыток
    secret = random.randint(1, 100)
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        remaining = MAX_ATTEMPTS - attempts
        print(f"\nОсталось попыток: {remaining}")

        # Запрос числа
        try:
            guess = int(input("Ваш вариант: "))
        except ValueError:
            print("Ошибка: нужно ввести целое число. Попробуйте еще раз.")
            continue

        # Проверка
        if guess < 1 or guess > 100:
            print("Число должно быть от 1 до 100. Попробуйте еще раз.")
            continue

        attempts += 1

        if guess == secret:
            print(f"\n🎉 Поздравляю! Вы угадали число {secret} за {attempts} попыток!")
            break
        elif guess < secret:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
    else:
        print(f"\nК сожалению, вы исчерпали все {MAX_ATTEMPTS} попыток.")
        print(f"Загаданное число: {secret}. Повезет в другой раз!")


if __name__ == "__main__":
    main()