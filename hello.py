def greet_user(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))


def calculate_square(num):
    return f"The square of {num} is {num ** 2}"


if __name__ == "__main__":
    user_num = float(input("Enter a number: "))
    print(calculate_square(user_num))
