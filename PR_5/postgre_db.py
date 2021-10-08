from psycopg2.extras import DictCursor
import psycopg2 as psql


class DatabasePostgre:
    def __init__(self, database, user, password, host, port):
        try:
            self.connection = psql.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port)
        except psql.OperationalError as error:
            raise error
        self.table_name = 'work_table'

    def __execute_query(self, query):
        self.connection.autocommit = True
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except psql.OperationalError as error:
            raise error

    def __execute_read_query(self, query):
        cursor = self.connection.cursor(cursor_factory=DictCursor)
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except psql.OperationalError as error:
            return error

    def __read_column_name(self):
        return self.__execute_read_query("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = '%s'
            ORDER BY ordinal_position
        """ % self.table_name)

    def __read_table_value(self):
        return self.__execute_read_query("""
            SELECT * FROM "%s"
        """ % self.table_name)

    def get_dic(self):
        result = {}
        columns = self.__read_column_name()
        values = self.__read_table_value()

        for value in values:
            result[str(value[columns[0][0]])] = {}
            for column_index in range(1, len(columns)):
                if value[str(columns[column_index][0])] is not None:
                    result[str(value[columns[0][0]])][str(columns[column_index][0])] = str(value[str(columns[column_index][0])])

        return result

    def add_dic(self, dic):
        self.clear()
        keys = []
        for d_p_key in dic.keys():
            d_keys = dic[d_p_key].keys()
            for d_key in d_keys:
                if d_key not in keys:
                    keys.append(d_key)

        query = 'CREATE TABLE IF NOT EXISTS "%s" (\n\t"p_key" TEXT PRIMARY KEY' % self.table_name
        for key in keys:
            query += ',\n\t"%s" TEXT' % key
        query += ');'
        self.__execute_query(query)

        for d_p_key in dic.keys():
            query = 'INSERT INTO "%s"\n\t("p_key"' % self.table_name
            for d_key in dic[d_p_key].keys():
                query += ', "%s"' % d_key

            query += ')\nVALUES\n\t(\'%s\'' % d_p_key
            for d_key in dic[d_p_key].keys():
                query += ', \'%s\'' % dic[d_p_key][d_key]

            query += ')'
            self.__execute_query(query)

    def clear(self):
        self.__execute_query('DROP TABLE IF EXISTS "%s"' % self.table_name)
