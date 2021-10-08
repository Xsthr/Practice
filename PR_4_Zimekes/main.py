from company import Company


def main():
    neo4j = Company('MIREA')
    employee_first = {'name':'Ivan', 'surname':'Ivanov', 'email':'ivan@mirea.ru'}
    employee_second = {'name': 'Andrej', 'surname': 'Andreev', 'email': 'andrey@mirea.ru'}
    employee_third = {'name': 'Viktor', 'surname': 'Viktorov', 'email': 'viktor@mirea.ru'}
    neo4j.add_employee('MIREA', employee_first)
    neo4j.add_employee('MIREA', employee_second)
    neo4j.add_employee('MIREA', employee_third)
    neo4j.delete_employee(employee_third)
    neo4j.find_way(employee_first, employee_second)


if __name__ == '__main__':
    main()