import random
NUM=10000000
def monte():
    counter = 0
    for i in range(NUM):
        if i%(NUM/100)==0:
            print(".",end="")
        x = random.random()
        y = random.random()
        #print("x:",x,"y:",y);
        if x*x+y*y < 1.0:
            counter += 1
    pi = 4.0*counter/NUM
    print("")
    print(pi)


def main():
    monte()

if __name__ == '__main__':
    main()
