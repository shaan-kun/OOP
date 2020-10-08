class Role:
    """Класс занятость.
    Хранит имя персонажа, актёра, стоимость годового контракта.

    Звание (rank):
    0 (высшая категория) - популярные и востребованные   - более 200 тыс
    1 категория          - не менее семи главных ролей   - 100 тыс
    2 категория          - Не менее пяти главных ролей   - 60-80 тысяч
    3 категория          - Не менее трёх главных ролей и
                           15 ролей второго плана        - 40 тысяч
    4 категория          - Две главные роли и десять
                           ролей второго плана           - 25 тысяч
    5 категория          - Одна главная роль и не менее
                           пяти второго плана            - 15 тысяч
    6 категория          - Не менее пяти эпизодических
                           ролей                         - 10 тысяч
    7 категория          - Без опыта                     - 5000
    8 категория          - Массовка                      - 600
    """
    __count = 1

    def __init__(self, name, actor):
        self.__id = Role.__count
        Role.__count += 1

        self.__name = name
        self.__actor = actor

        if actor.getRank() == 8:
            self.__contract_value = 600
        elif actor.getRank() == 7:
            self.__contract_value = 5000
        elif actor.getRank() == 6:
            self.__contract_value = 10000
        elif actor.getRank() == 5:
            self.__contract_value = 15000
        elif actor.getRank() == 4:
            self.__contract_value = 25000
        elif actor.getRank() == 3:
            self.__contract_value = 40000
        elif actor.getRank() == 2:
            self.__contract_value = 70000
        elif actor.getRank() == 1:
            self.__contract_value = 100000
        elif actor.getRank() == 0:
            self.__contract_value = 200000

    def setName(self, name):
        self.__name = name

    def setActor(self, actor):
        self.__actor = actor

    def setContractValue(self, contract_value):
        self.__contract_value = contract_value

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getActor(self):
        return self.__actor

    def getContractValue(self):
        return self.__contract_value

    def __str__(self):
        return "{} | {} | {} | {}".format(self.__id, self.__name,
                                          self.__actor.getShortName(),
                                          self.__contract_value)
