import dis
import inspect


class Point:
    """ точка на трёхмерной плоскости """
    MAX_SIZE = 220
    #__slots__ = ["__X", "__y", "test"] # прописываем публичные атрибуты

    def __init__(self):
        self.test = 0
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self.distance = 0

    def __del__(self):
        # caller_frame = inspect.currentframe().f_back
        # dis.dis(caller_frame.f_code)
        print("удаление объекта ", self.__str__())

    def __checker(self, item):
        if isinstance(item, int):
            return True
        else:
            print(" Координата точки ({}) должна иметь тип данных {}".format(item, int.__name__))

    def setCoordX(self, x):
        if self.__checker(x):
            self.__x == x

    def setCoordY(self, y):
        if self.__checker(x):
            self.__y == y

    def setCoordZ(self, z):
        if self.__checker(x):
            self.__z == z

    def getCoordX(self):
        return self.__x

    def getCoordY(self):
        return self.__y

    def getCoordZ(self):
        return self.__z

    def __getattribute__(self, item):

        if (item == "_Point__x") or (item == "_Point__y") or (item == "_Point__z"):
            print("Это частная переменная используйте getter")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print("установка атрибута key {} , value {}".format(key, value))
        if key == "MAX_SIZE":
            return AttributeError
        else:
            self.__dict__[key] = value

    def __delattr__(self, item):
        print("удаление атрибута ", item)


def main():
    pass
    #print(Point.__x)
    p1 = Point()
    p1.setCoordX("123")
    p1.__dict__["DISTANCE"] = 123
    p1.test1 = 1
    # print(p1.__checker('12313'))
    print(p1.DISTANCE)
    print(p1._Point__x)
    print(p1._Point__y)
    print(p1._Point__z)
    print(Point.__dict__)
    print(Point.__doc__)


if __name__ == "__main__":
    main()

