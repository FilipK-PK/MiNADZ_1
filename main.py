from pymongo import MongoClient
import keys


PATH = f"mongodb+srv://MiNADZ:{keys.PASSWORD}@atlascluster.y8etfyq.mongodb.net/?retryWrites=true&w=majority"


if __name__ == "__main__":
    try:
        client = MongoClient(PATH)
    except Exception:
        print('Bład połacczenia sie z baza')
        exit(-1)

    db = client['Projekt_1']
    colect = db['projekt_1']

    """ to dodaje nowy elementa do bazy danych """
    try:
        post = {"_id": 0, "name": "tim", "score": 5}
        colect.insert_one(post)
    except Exception:
        print("Bład dodania elementu do bazy")
        print("Element pewnie juz istnieje")
