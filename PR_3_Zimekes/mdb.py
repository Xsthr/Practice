from pymongo import MongoClient


class Student:
    def __init__(self, ip='localhost', port=27017):
        self.client = MongoClient(ip, port)
        self.db = self.client['pr3']
        self.collection = self.db['student']

    def _insert_document(self, data):
        return self.collection.insert_one(data).inserted_id

    def _find_document(self, elements, multiple=False):
        if multiple:
            results = self.collection.find(elements)
            return [i for i in results]
        else:
            return self.collection.find_one(elements)

    def _update_document(self, query_elements, new_values):
        self.collection.update_one(query_elements, {'$set': new_values})

    def _delete_document(self, query):
        self.collection.delete_one(query)

    def add_student(self, id, fullname, login, pswd):
        self._insert_document({'std_id': id, 'std_fullname': fullname, 'std_login': login, 'std_pswd': pswd})

    def get_student(self, id):
        return self._find_document({'std_id': id})

    def edit_fullname_student(self, id, fullname):
        self._update_document({'std_id': id}, {'std_fullname': fullname})

    def edit_login_student(self, id, login):
        self._update_document({'std_id': id}, {'std_login': login})

    def edit_pswd_student(self, id, pswd):
        self._update_document({'std_id': id}, {'std_pswd': pswd})

    def delete_student(self, id):
        self._delete_document({'std_id': id})
