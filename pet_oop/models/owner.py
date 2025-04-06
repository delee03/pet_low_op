class Owner:
    def __init__(self, name, phone, address):
        self.__name = name
        self.__phone = phone
        self.__address = address

    @property
    def name(self):
        return self.__name

    def get_info(self):
        return f"Owner: {self.__name}, Phone: {self.__phone}, Address: {self.__address}"
