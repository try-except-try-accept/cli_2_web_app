
from sys import stdout
from queue import Queue

class Mocker:

    def __init__(self):
        self.q = Queue()

    def print_wrapper(self, *s, end="\n"):
        stdout.write("called print wrapper\n")
        stdout.write("".join(s))

        with open("output.txt", "a") as f:
            for string in s:
                f.write(string+" ")
            f.write(end)

        return None

    def input_wrapper(self, s=""):
        stdout.write("called input wrapper\n")
        self.print_wrapper(s)
        return self.q.get()