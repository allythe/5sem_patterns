from humans import Human
from locations import Dormitory


def main():
    dorm = Dormitory()

    h = Human('Vasya', 18, 'good', 'dorm', 10)
    h()
    h.go(dorm)
    h()


if __name__ == '__main__':
    main()
