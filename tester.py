

def main():
    dorm = Dormitory()

    H = Human('Vasya', 18, 'good', 'dorm', 10)
    H()
    H.go(dorm)
    H()


if __name__ == '__main__':
    main()

from humans import Human
from locations import Dormitory
