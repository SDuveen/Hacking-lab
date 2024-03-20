from subframes.subframe1 import create_subframe1
from subframes.subframe2 import create_subframe2
from subframes.subframe3 import create_subframe3

if __name__ == '__main__':
    subframe1 = create_subframe1(t_gd = 0, a_f2 = 0, a_f1 = 0, a_f0 = 0)
    subframe2 = create_subframe2()
    subframe3 = create_subframe3()

    print(subframe1)
    print(subframe2)
    print(subframe3)