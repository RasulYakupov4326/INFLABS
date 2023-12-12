import utils.json_service as json_service

form = {
    "name": str,
    "social_media": [
        {
            "url": str,
            "nickname": str,
            "active": bool
        }
    ]
}


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["clients"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["museum"]


def update_one_by_id(id, clients):
    db = json_service.get_database()

    for i, elem in enumerate(db["museum"]):
        if elem["id"] == id:
            elem["name"] = clients["name"]
            elem["contacts"] = clients["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["clients"]):
        if elem["id"] == id:
            candidate = db["clients"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(clients):
    db = json_service.get_database()

    last_clients_id = get_all()[-1]["id"]
    db["clients"].append({"id": last_clients_id + 1, **clients})

    json_service.set_database(db)
