import dis
import inspect



class Point:
    """ Урок создание свойства точка на трёхмерной плоскости первая версия"""

    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __checkValue(self, item):
        if isinstance(item, int):
            return True
        else:
            raise ValueError("Неверный формат данных")

    def __setCoordX(self, x):
        if self.__checkValue(x):
            self.__x = x

    def __getCoordX(self):
        return self.__y

    def __delCoordX(self):
        print("удаление коорднаты точки по оси x")
        del self.__x

    def __setCoordY(self, y):
        if self.__checkValue(y):
            self.__y = y

    def __getCoordY(self):
        return self.__x

    def __delCoordY(self):
        print("удаление коорднаты точки по оси y")
        del self.__y

    @property
    def Z(self):
        return self.__z

    @Z.setter
    def Z(self, z):
        if self.__checkValue(z):
            self.__z = z

    @Z.deleter
    def Z(self):
        print("удаление коорднаты точки по оси z")
        del self.__z

    X = property(fget=__getCoordX, fset=__setCoordX, fdel=__delCoordX, doc="Координата по оси X")
    Y = property(__getCoordY, __setCoordY, __delCoordY)
    #Z = property(__getCoordZ, __setCoordZ, __delCoordZ)


def main():
    p1 = Point()
    print(p1.X)
    p1.X = 43
    print(p1.X)
    pt = Point()
    pt.Z = 123
    z = pt.Z
    print(z)
    del pt.Z


if __name__ == "__main__":
    main()

