from mdb import Student


def main():
    students = Student('localhost', 27017)
    students.add_student(0, 'name_test', 'login_test', 'password_test')
    print(students.get_student(0))
    students.edit_fullname_student(0, 'name_edit')
    print(students.get_student(0))
    students.delete_student(0)
    print(students.get_student(0))


if __name__ == '__main__':
    main()
