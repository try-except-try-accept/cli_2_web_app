
from sys import stdout
from queue import Queue

class Mocker:

    def __init__(self):
        self.q = Queue()
        self.lines = []
        self.line_index = 0


    def print_wrapper(self, *s, end="\n"):
        stdout.write("called print wrapper\n")
        stdout.write("".join(s))

        this_line = " ".join(s)

        self.add_line(this_line)




        return None

    def get_new_lines(self):

        i = self.line_index
        stdout.write("Getting new lines from " + str(i))
        self.line_index = len(self.lines)-1
        stdout.write("to " + str(self.line_index))
        return self.lines[i:]

    def add_line(self, line):
        if not self.lines or line.strip() != self.lines[-1].strip():
            self.lines.append(line)



    def input_wrapper(self, s=""):
        stdout.write("called input wrapper\n")
        self.print_wrapper(s)
        return self.q.get()