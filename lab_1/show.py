class Show:
    """Класс спектакль.
    Хранит название, год, бюджет, список ролей.
    """
    __count = 1

    def __init__(self, name, year, budget, roles):
        self.__id = Show.__count
        Show.__count += 1

        self.__name = name
        self.__year = year
        self.__budget = budget
        self.__roles = roles

    def setName(self, name):
        self.__name = name

    def setYear(self, year):
        self.__year = year

    def setBudget(self, budget):
        self.__budget = budget

    def setRoles(self, roles):
        self.__roles = roles

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getYear(self):
        return self.__year

    def getBudget(self):
        return self.__budget

    def getRoles(self):
        return self.__roles

    def __str__(self):
        string = "{} | {} | {} | {} | ".format(self.__id, self.__name,
                                               self.__year, self.__budget)

        names = [role.getActor().getShortName() for role in self.__roles]

        string += ", ".join(names)

        return string
