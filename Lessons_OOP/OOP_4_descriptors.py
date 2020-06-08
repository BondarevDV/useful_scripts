
class CoordValueUptoVer3_6:
    """дескриптор данных для версий python до 3.6"""
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __delete__(self, instance, owner):
        del self.__value


class CoordValue:
    """дескриптор данных для версий python начиная 3.6"""
    def __set_name__(self, owner, name):
        # print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __delete__(self, instance, owner):
        del self.__value


class NoneDataDescr:
    """дескриптор данных для версий python начиная 3.6"""
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Point1:
    X = CoordValueUptoVer3_6("X")
    Y = CoordValueUptoVer3_6("Y")
    Z = CoordValueUptoVer3_6("Z")

    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z


class Point2:
    X = CoordValue()
    Y = CoordValue()
    Z = CoordValue()

    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z


def main():
    point1 = Point1()
    point1.X = 1
    print(point1.X)

    point2 = Point2()
    point2.X = 2
    print(point2.X)

    point3 = Point3()
    point3.X = 2
    print(point3.X)


if __name__ == '__main__':
    main()
