import redis


class DatabaseRedis:
    def __init__(self, db=0):
        self.r = redis.Redis(db=db)

    def __get_keys(self):
        return self.r.keys()

    def __get_value(self, key):
        return self.r.hgetall(key)

    def get_dic(self):
        result = {}
        b_p_keys = self.__get_keys()

        for b_p_key in b_p_keys:
            result[b_p_key.decode()] = {}
            b_dic = self.__get_value(b_p_key)
            dic = {}
            for b_key in b_dic.keys():
                result[b_p_key.decode()][b_key.decode()] = b_dic[b_key].decode()

        return result

    def add_dic(self, dic):
        self.clear()
        with self.r.pipeline() as pipe:
            for name, field in dic.items():
                for key, value in field.items():
                    pipe.hset(name, key, value)
            pipe.execute()
        self.r.bgsave()

    def clear(self):
        self.r.flushdb()
