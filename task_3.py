class NegativeNumberError(Exception):
    def __init__(self, value, message="Число отрицательное"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.value}"


def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)


for number in [10, -10]:
    try:
        print(f'проверка числа {number}')
        check_positive_number(number)
    except NegativeNumberError as nne:
        print(f"Возникла ошибка: {type(nne).__name__}")
        print(nne)
