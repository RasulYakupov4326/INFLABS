import utils.json_service as json_service

form = {
    "designation": str
}


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["exhibits"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["exhibits"]


def update_one_by_id(id, exhibits):
    db = json_service.get_database()

    for i, elem in enumerate(db["exhibits"]):
        if elem["id"] == id:
            elem["name"] = exhibits["name"]
            elem["contacts"] = exhibits["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["exhibits"]):
        if elem["id"] == id:
            candidate = db["exhibits"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(exhibits):
    db = json_service.get_database()

    last_exhibits_id = get_all()[-1]["id"]
    db["exhibits"].append({"id": last_exhibits_id + 1, **exhibits})

    json_service.set_database(db)
