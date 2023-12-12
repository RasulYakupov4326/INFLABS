import components.museum.service as museum
import components.museum_departments.service as museum_departments
import components.workers.service as workers
import components.exhibits.service as exhibits


def check(userInput, usl1, usl2):
    if userInput.isdigit() and (int(userInput) in range(usl1, usl2 + 1)):
        return True
    else:
        return False


entities = [museum, museum_departments, workers, exhibits]


def get_entity(user_type):
    return entities[user_type - 1]


def get_id(obj):
    return int(input("Введите id: "))


def get_create_data(obj):
    return get_create_data_for_dict(obj.form)


def get_create_data_for_dict(obj):
    res = {}
    for i in obj.keys():
        if bool(obj[i]) and isinstance(obj[i], dict):
            res[i] = get_create_data_for_dict(obj[i])
        else:
            res[i] = input("Введите значение " + i + ": ")
    return res


arguments_extractors = [[(get_create_data, "create_data")],
                        [(get_id, "id")],
                        [(get_id, "id"), (get_create_data, "update_data")],
                        [(get_id, "id")],
                        [(None, "")],
                        ]


def get_arguments(obj, operation_index):
    res = {}
    for arg in arguments_extractors[operation_index - 1]:
        res[arg[1]] = arg[0](obj)
    return res


def apply_create(obj, args):
    obj.create_one(args["create_data"])


def apply_info(obj, args):
    return obj.get_one_by_id(args["id"])


def apply_delete(obj, args):
    return obj.delete_one_by_id(args["id"])


def apply_update(obj, args):
    return obj.update_one_by_id(args["id"], args["update_data"])


operations = [apply_create, apply_info, apply_update, apply_delete, None]


def apply_operation(obj, op, args):
    return op(obj, args)


def get_operation(number):
    return operations[number - 1]


condition = True

while condition:
    condition2 = False
    tip = False
    top = False
    operation_index = input("Введите действие:"
                            "\n1) Создать новый обьект"
                            "\n2) Узнать информацию о существующем объекте"
                            "\n3) Обновить информацию о существующем объекте"
                            "\n4) Удалить объект"
                            "\n5) Добавить несколько новых объектов"
                            "\n6) Закончить редактирование"
                            "\n")
    if check(operation_index, 1, 5):
        tip = True
        condition2 = True
        while condition2:
            object_number = input("Введите интересующий отдел:"
                                  "\n1) Музеи"
                                  "\n2) Отделы"
                                  "\n3) Работники"
                                  "\n4) Экспонаты"
                                  "\n5) Вернутся назад"
                                  "\n"
                                  )
            if check(object_number, 1, 4):
                top = True
                condition2 = False
            elif check(object_number, 5, 5):
                condition2 = False
            else:
                print("Неверный ввод")
    elif check(operation_index, 6, 6):
        condition = False
    else:
        print("Невверный ввод")

    if tip and top:
        operation_index = int(operation_index)
        entity_index = int(object_number)

        entity = get_entity(entity_index)
        arguments = get_arguments(entity, operation_index)
        operation = get_operation(operation_index)

        print(
            apply_operation(
                entity,
                operation,
                arguments
            )
        )

# {"form":general_form[accurateUserInput-1]}

general_form = [
    {
        "name": {},
        "address": {}
    },
    {
        "title": {},
        "exhibits_id": {},
        "workers_id": {},
        "museum_departments_id": {}
    },
    {
        "name": {},
        "age": {},
        "profession": {},
        "museum_departments_id": {},
        "contacts": {
            "email": {},
            "phone": {}
        }
    },
    {
        "designation": {}
    }

]
