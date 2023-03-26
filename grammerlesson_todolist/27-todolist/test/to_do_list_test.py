import unittest
import sys
import os
from src import to_do_list


class PrivateTestProblem(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        to_do_list.file_path = "./tasks.txt"
        pass

    def test_listF(self):
        if os.path.exists("./tasks.txt"):
            os.remove("./tasks.txt")
        self.stream_in.write('''todo -a "discuss question" "play baseball" "go shopping" "programming"''')
        self.stream_in.write('todo -all')
        self.stream_in.write("todo -quit")

        to_do_list.to_do()
        expect = ("todo:discuss question" + "\n"
                  + "todo:play baseball" + "\n"
                  + "todo:go shopping" + "\n"
                  + "todo:programming" + "\n")

        self.assertEqual(expect, "".join(self.stream_out.buff))

    def test_listG(self):
        self.stream_in.write('''todo -d "discuss question" "programming"''')
        self.stream_in.write('todo -all')
        self.stream_in.write("todo -quit")

        to_do_list.to_do()
        expect = ("todo:play baseball" + "\n"
                  + "todo:go shopping" + "\n")

        self.assertEqual(expect, "".join(self.stream_out.buff))

    def test_listH(self):
        self.stream_in.write('''todo -a "discuss question" "programming"''')
        self.stream_in.write('''todo -c "play baseball" "go shopping"''')
        self.stream_in.write('todo -all')
        self.stream_in.write("todo -quit")

        to_do_list.to_do()
        expect = ("completed:play baseball" + "\n"
                  + "completed:go shopping" + "\n"
                  + "todo:discuss question" + "\n"
                  + "todo:programming" + "\n")

        self.assertEqual(expect, "".join(self.stream_out.buff))

    def test_listI(self):
        self.stream_in.write('''todo -a "do eye exercises" "play games"''')
        self.stream_in.write('todo -f todo')
        self.stream_in.write("todo -quit")

        to_do_list.to_do()
        expect = ("todo:discuss question" + "\n"
                  + "todo:programming" + "\n"
                  + "todo:do eye exercises" + "\n"
                  + "todo:play games" + "\n")

        self.assertEqual(expect, "".join(self.stream_out.buff))

    def test_listJ(self):
        self.stream_in.write('''todo -c "play games"''')
        self.stream_in.write('todo -f completed')
        self.stream_in.write("todo -quit")

        to_do_list.to_do()
        expect = ("completed:play baseball" + "\n"
                  + "completed:go shopping" + "\n"
                  + "completed:play games" + "\n")

        self.assertEqual(expect, "".join(self.stream_out.buff))

    def tearDown(self):
        sys.stdout = self.out_stream
        sys.stdin = self.in_stream
        pass


class MyStream:
    def __init__(self):
        self.buff = []
        self.write_count = 0

    def write(self, output_stream):
        self.buff.append(output_stream)

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur
