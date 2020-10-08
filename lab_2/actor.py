class Actor:
    """Класс актёр.
    Хранит идентификатор, полное имя, сокращённое имя, звание, стаж.

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

    def __init__(self, full_name, short_name, rank, experience):
        self.__id = Actor.__count
        Actor.__count += 1

        self.__full_name = full_name
        self.__short_name = short_name
        self.__rank = rank
        self.__experience = experience

    def setFullName(self, full_name):
        self.__full_name = full_name

    def setShortName(self, short_name):
        self.__short_name = short_name

    def setRank(self, rank):
        self.__rank = rank

    def setExperience(self, experience):
        self.__experience = experience

    def getID(self):
        return self.__id

    def getFullName(self):
        return self.__full_name

    def getShortName(self):
        return self.__short_name

    def getRank(self):
        return self.__rank

    def getExperience(self):
        return self.__experience

    def __str__(self):
        return "{} | {} | {} | {}".format(self.__id, self.__full_name,
                                          self.__rank, self.__experience)
