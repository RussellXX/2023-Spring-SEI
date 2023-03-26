import unittest
import sys
from src import grammarlesson


class Test(unittest.TestCase):

    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test1(self):
        input_str = 'petr\n'
        output_str = 'YES\n'
        self.stream_in.write(input_str)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test2(self):
        input_str = 'etis atis animatis etis atis amatis\n'
        output_str = 'NO\n'
        self.stream_in.write(input_str)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test3(self):
        input_num = 'nataliala kataliala vetra feinites\n'
        output_str = 'YES\n'
        self.stream_in.write(input_num)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test4(self):
        input_str = 'vetra feinites\n'
        output_str = 'YES\n'
        self.stream_in.write(input_str)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test5(self):
        input_num = 'lios lios petr initis qwe\n'
        output_str = 'NO\n'
        self.stream_in.write(input_num)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test6(self):
        input_str = 'kataliala vetra\n'
        output_str = 'YES\n'
        self.stream_in.write(input_str)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        self.assertEqual(result, output_str)

    def test7(self):
        input_num = 'qweasbvflios\n'
        output_str = 'YES\n'
        self.stream_in.write(input_num)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test8(self):
        input_num = 'lios initis\n'
        output_str = 'NO\n'
        self.stream_in.write(input_num)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test9(self):
        input_num = 'petr initis lios\n'
        output_str = 'NO\n'
        self.stream_in.write(input_num)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test10(self):
        input_num = 'petra petra petra\n'
        output_str = 'NO\n'
        self.stream_in.write(input_num)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test11(self):
        input_num = 'liala petra initis\n'
        output_str = 'NO\n'
        self.stream_in.write(input_num)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)

    def test12(self):
        input_num = 'liala petra inites\n'
        output_str = 'YES\n'
        self.stream_in.write(input_num)
        grammarlesson.isPetyaLanguage()
        result = str(self.stream_out.readline())
        isEqual = result == output_str
        self.assertTrue(isEqual)



    def tearDown(self):
        sys.stdout = self.out_stream
        sys.stdin = self.in_stream
        pass


class MyStream:

    def __init__(self):
        self.buff = []

    def write(self, output_stream):
        self.buff.append(output_stream)

    def readline(self):
        result = ''
        while len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            result = result + cur
            if result.endswith('\n'):
                return result
        return result