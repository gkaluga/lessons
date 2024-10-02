from .package3.module1 import hello

def good_word(name):
    hello(name)
    print('You are the best', name)


if __name__ == '__main__':
    good_word('Urban')
