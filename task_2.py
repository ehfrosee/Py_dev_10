def validate_user_input(data):
    print("Проверка данных:")
    try:
        if not isinstance(data, dict):
            raise TypeError("Аргумент не является словарём")
    except TypeError:
        print("Аргумент не является словарём")
    else:
        try:
            if not isinstance(data['name'], str):
                raise ValueError("Имя должно быть строкой")
        except ValueError:
            print("Имя должно быть строкой")
        except KeyError:
            print("Ключа name в данном словаре нет")
        try:
            if int(data['age']) < 0:
                raise ValueError("Возраст не может быть меньше 0")
        except KeyError:
            print("Ключа age в данном словаре нет")
    finally:
        print(f"полученные данные: {data}")

data_1 = {"name": "Alice", "age": 30}
data_2 = {"age": 30}
data_3 = {"name": "Alice"}
data_4 = "name"

validate_user_input(data_1)
validate_user_input(data_2)
validate_user_input(data_3)
validate_user_input(data_4)