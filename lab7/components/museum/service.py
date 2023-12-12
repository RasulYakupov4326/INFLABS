import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["museum"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["museum"]


def update_one_by_id(id, museum):
    db = json_service.get_database()

    for i, elem in enumerate(db["museum"]):
        if elem["id"] == id:

            elem["name"] = museum["name"]
            elem["contacts"] = museum["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["workers"]):
        if elem["id"] == id:

            candidate = db["workers"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(museum):
    db = json_service.get_database()

    last_museum_id = get_all()[-1]["id"]
    db["workers"].append({"id": last_museum_id + 1, **museum})

    json_service.set_database(db)