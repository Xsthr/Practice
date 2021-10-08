import redis
import logging

logging.basicConfig(level=logging.INFO)


class CakeShop:
    __CAKES_DIC = {
        'cake_0': {
            'name': 'Plain',
            'quantity': '3',
            'purchases': '0',
            'price': '280'
        },
        'cake_1': {
            'name': 'Apple Crumb',
            'quantity': '3',
            'purchases': '0',
            'price': '300'
        },
        'cake_2': {
            'name': 'Crumb Cheese',
            'quantity': '3',
            'purchases': '0',
            'price': '270'
        },
        'cake_3': {
            'name': 'Chocolate',
            'quantity': '3',
            'purchases': '0',
            'price': '310'
        }
    }

    def __init__(self, db=0):
        self.r = redis.Redis(db=db)  # База данных №0

    def add_dic(self):
        """Добавление словаря в базу данных"""
        with self.r.pipeline() as pipe:  # Конвейерная передача
            for name, field in self.__CAKES_DIC.items():
                for key, value in field.items():
                    pipe.hset(name, key, value)
            pipe.execute()  # Отправка запроса
        self.r.bgsave()  # Создание форка процесса. Запись данных на диск
        logging.info('__CAKES_DIC загружен в базу данных')

    def clear(self):
        """Очистка базы данных"""
        self.r.flushdb()
        logging.info('База данных очищена')

    def get_keys(self):
        """Получить ключи"""
        result = self.r.keys()
        logging.debug('Полученны ключи')
        return result

    def get_value(self, key):
        """Получить значение по ключу"""
        result = self.r.hgetall(key)
        logging.debug('Полученно значение ключа %s' % key)
        return result

    def buy_cake(self, cake_id):
        """Купить торт"""
        with self.r.pipeline() as pipe:
            while True:
                try:
                    pipe.watch(cake_id)  # Проверка на наличие изменений
                    quantity: bytes = self.r.hget(cake_id, 'quantity')  # Получение кол-ва тортов
                    if quantity > b'0':  # Проверка кол-ва тортов
                        pipe.multi()  # Блок запросов
                        pipe.hincrby(cake_id, 'quantity', -1)
                        pipe.hincrby(cake_id, 'purchases', 1)
                        pipe.execute()  # Конец блока запросов
                        logging.info('Куплен %s' % cake_id)
                    else:
                        pipe.unwatch()
                        logging.error('DecrementError: %s.quantity is zero' % cake_id)
                    break
                except redis.WatchError:
                    logging.warning('WatchError: cake_id %s' % cake_id)
