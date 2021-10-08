from pymongo import MongoClient


def insert_document(collection, data):
    return collection.insert_one(data).inserted_id


def find_document(collection, elements, multiple=False):
    if multiple:
        results = collection.find(elements)
        return [i for i in results]
    else:
        return collection.find_one(elements)


def update_document(collection, query_elements, new_values):
    collection.update_one(query_elements, {'$set': new_values})


def delete_document(collection, query):
    collection.delete_one(query)


# Подключние к базе данных
client = MongoClient('localhost', 27017)
db = client['TestDB']
test_collection = db['test']

# Добавление данных
test_dict = {'_id': '1', 'name': 'Test1', 'age': 11}
print(insert_document(test_collection, test_dict))

# Извлечение данных
print(find_document(test_collection, {'name': 'Test1'}))

# Изменение данных
test_dict = {'name': 'Test2', 'age': 22}
dict_id = insert_document(test_collection, test_dict); print(dict_id)
print(find_document(test_collection, {'_id': dict_id}))

update_document(test_collection, {'_id': dict_id}, {'age': 0})
print(find_document(test_collection, {'_id': dict_id}))

# Удаление данных
delete_document(test_collection, {'_id': dict_id})
print(find_document(test_collection, {'_id': dict_id}))