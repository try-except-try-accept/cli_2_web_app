from __future__ import print_function





def main():

    while True:

        print("hello")
        print("olu")
        print("blah")

        input("How are you")
        print("Go")


from helpers import Mocker

m = Mocker()

print = m.print_wrapper
input = m.input_wrapper