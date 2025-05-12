def convert_to_int(value):
    try:
        value_int = int(value)
    except ValueError:
        print("Невозможно преобразовать переменную в int")
    except BaseException as be:
        print(f"Возникла ошибка: {type(be).__name__}")
    finally:
        print("Попытка преобразования завершена\n")

value_1 = "123"
value_2 = "abc"
value_3 = [1,2,3]

convert_to_int(value_1)
convert_to_int(value_2)
convert_to_int(value_3)