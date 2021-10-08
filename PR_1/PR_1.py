"""
ANY=0, ONE=1, TWO=2, THREE=3, QUORUM=4, ALL=5, LOCAL_QUORUM=6,
EACH_QUORUM=7, SERIAL=8, LOCAL_SERIAL=9, LOCAL_ONE=10
"""


from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement


class CassandraDB:
    def __init__(self, key_space_name='testkeyspace'):
        self.cluster = Cluster()
        self.session = cluster.connect(str(key_space_name))

    def __error(exception):
        raise exception

    def __success(rows):
        result = []
        try:
            for i in rows:
                result.append(i)
            return result
        except Exception as e:
            raise e

    def execute_query(self, query, level=ConsistencyLevel.QUORUM):
        self.session.execute(SimpleStatement(query, consistency_level=level))

    def execute_read_query(self, query, level=ConsistencyLevel.QUORUM):
        result = []
        output = self.session.execute(SimpleStatement(query, consistency_level=level))
        return self.__success(output.result())

    def execute_async_read_query(self, query, level=ConsistencyLevel.QUORUM):
        result = []
        output = self.session.execute_async(SimpleStatement(query, consistency_level=level))
        return output.add_callbacks(self.__success, self.__error)

    def __execute_prepared_read_query(self, query, level=ConsistencyLevel.QUORUM):
        return self.session.prepare(SimpleStatement(query, consistency_level=level))
            

class TestTable:
    def __init__(self):
        self.db = CassandraDB()

    def __create_table(self):
        self.db.execute_query("""
            CREATE TABLE IF NOT EXISTS users (
                login text,
                password text,
                age int,
                PRIMARY KEY (login)
            );
        """)

    def test_value(self):
        self.db.execute_query("""
            DELETE FROM users;
            INSERT INTO users (login, password, age)
            VALUES
                ('login1', 'password1', 11),
                ('login2', 'password2', 22),
                ('login3', 'password3', 33);
        """)

    def get_table(self):
        return self.db.execute_read_query("""
            SELECT * FROM users;
        """)

    def delete_user(self, login):
        self.db.execute_query("""
            DELETE FROM users
            WHERE login = '%s'
        """ % login)

    def add_user(self, login, password, age):
        self.db.execute_query("""
            INSERT INTO users (login, password, age)
            VALUES
                ('%s', '%s', '%s')
        """ % (login, password, age))

    def get_user(self, login):
        return self.db.execute_read_query("""
            SELECT * FROM users
            WHERE login = '%s'
        """ % login).one()