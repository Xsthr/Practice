from neo4j import GraphDatabase


class Company:
    def __init__(self, company_name, uri='bolt://localhost:7687', user='neo4j', password='000000'):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self._create_head(company_name)

    def close(self):
        self.driver.close()

    def _create_head(self, company_name):
        query = 'MERGE (a:Company { company_name: "%s" })' % company_name
        with self.driver.session() as session:
            session.write_transaction(self._default_transaction, query)

    def add_employee(self, company_name, employee):
        query = """
            MATCH (a:Company {company_name: "%s"})
            MERGE (b:Employee { name: "%s", surname: "%s", email: "%s" })
            MERGE (a)-[r:WorksIn]->(b)
        """ % (company_name, employee['name'], employee['surname'], employee['email'])
        with self.driver.session() as session:
            session.write_transaction(self._default_transaction, query)

    def delete_employee(self, employee):
        query = """
            MATCH (a:Employee { name: "%s", surname: "%s", email: "%s" })
            DETACH DELETE a
        """ % (employee['name'], employee['surname'], employee['email'])
        with self.driver.session() as session:
            session.write_transaction(self._default_transaction, query)

    def find_way(self, employee_first, employee_second):
        query = """
            MATCH (a:Employee { name: "%s", surname: "%s", email: "%s" }), 
                  (b:Employee { name: "%s", surname: "%s", email: "%s" }),
                  c = shortestPath((a)-[*]-(b))
            RETURN c
        """ % (employee_first['name'], employee_first['surname'], employee_first['email'],
               employee_second['name'], employee_second['surname'], employee_second['email'])
        with self.driver.session() as session:
            session.write_transaction(self._find_way_transaction, query)

    @staticmethod
    def _default_transaction(tx, query):
        return tx.run(query)

    @staticmethod
    def _find_way_transaction(tx, query):
        result = tx.run(query)
        for i in result:
            for j in i['c']:
                print(j)