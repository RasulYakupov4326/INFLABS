import components.museum.service as museum
import components.museum_departments.service as museum_department
import components.workers.service as worker
import components.exhibits.service as exhibit


def check(userInput, usl1, usl2):
    if userInput.isdigit() and (int(userInput) in range(usl1, usl2+1)):
        return True
    else:
        return False

entities = [museum, museum_department, worker, exhibit]
def entity(user_type):
    return entities[user_type - 1]

def apply_info(obj):
    print(obj.get_one_by_id(int(input("введите id интересуемого объекта\n"))))
    return None

def apply_delete(obj):
    return obj.delete_one_by_id(int(input("введите id удаляемого объекта\n")))

operations = [None, apply_info, None, apply_delete, None]
def apply_operation(obj, number):
    operations[number - 1](obj)


eachComponent = {"museum": ["название", "адрес"],
                 "museum_departments": ["название", "id экспонатов", "id сотрудников", "id проходов"],
                 "workers": ["имя и отчество", "возраст", "профессия", "отдел", "email", "мобильный телефон"],
                 "exhibits": ["название"]
                 }

condition = True

while condition:
    condition2 = False
    tip = False
    top = False
    userInput = input("Введите действие:"
                      "\n1) Создать новый обьект"
                      "\n2) Узнать информацию о существующем объекте"
                      "\n3) Обновить информацию о существующем объекте"
                      "\n4) Удалить объект"
                      "\n5) Добавить несколько новых объектов"
                      "\n6) Закончить редактирование"
                      "\n")
    if check(userInput, 1, 5):
        tip = True
        condition2 = True
        while condition2:
            accurateUserInput = input("Введите интересующий отдел:"
                                      "\n1) Музеи"
                                      "\n2) Отделы"
                                      "\n3) Работники"
                                      "\n4) Экспонаты"
                                      "\n5) Вернутся назад"
                                      "\n"
                                    )
            if check(accurateUserInput, 1, 4):
                top = True
                condition2 = False
            elif check(accurateUserInput, 5, 5):
                condition2 = False
            else:
                print("Неверный ввод")
    elif check(userInput, 6, 6):
        condition = False
    else:
        print("Невверный ввод")

    if tip and top:
        userInput = int(userInput)
        accurateUserInput = int(accurateUserInput)
        apply_operation(entity(accurateUserInput), userInput)


