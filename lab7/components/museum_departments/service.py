import utils.json_service as json_service

form = {
    "title": str,
    "exhibits_id": [int],
    "workers_id": [int],
    "museum_departments_id": [int]
}


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["museum_departments"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["museum_departments"]


def update_one_by_id(id, museum_departments):
    db = json_service.get_database()

    for i, elem in enumerate(db["museum_departments"]):
        if elem["id"] == id:
            elem["title"] = museum_departments["title"]
            elem["exhibits_id"] = museum_departments["exhibits_id"]
            elem["workers_id"] = museum_departments["workers_id"]
            elem["museum_departments_id"] = museum_departments["museum_departments_id"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["museum_departments"]):
        if elem["id"] == id:
            candidate = db["museum_departments"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(museum_departments):
    db = json_service.get_database()

    last_museum_departments_id = get_all()[-1]["id"]
    db["museum_departments"].append({"id": last_museum_departments_id + 1, **museum_departments})

    json_service.set_database(db)
