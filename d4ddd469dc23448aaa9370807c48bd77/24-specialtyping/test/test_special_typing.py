import unittest
import sys
from src import special_typing


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_special_typing1(self):
        self.stream_in.write('4')
        self.stream_in.write('ababa')
        self.stream_in.write('ba')
        self.stream_in.write('ababa')
        self.stream_in.write('bb')
        self.stream_in.write('aaa')
        self.stream_in.write('aaaa')
        self.stream_in.write('aababa')
        self.stream_in.write('ababa')
        expect = 'YES\n' + 'NO\n' + 'NO\n' + 'YES\n'
        special_typing.special_typing()
        result = ''
        for i in range(len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_special_typing2(self):
        self.stream_in.write('2')
        self.stream_in.write('lrlrrlrllrlrlrllllrlrllrl')
        self.stream_in.write('llrlrl')
        self.stream_in.write('xyxyxyyxyxyyyxyxyx')
        self.stream_in.write('xxy')
        expect = 'YES\n' + 'NO\n'
        special_typing.special_typing()
        result = ''
        for i in range(len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_special_typing3(self):
        self.stream_in.write('10')
        self.stream_in.write('paxghjnihn')
        self.stream_in.write('hn')
        self.stream_in.write('hdmevxvn')
        self.stream_in.write('n')
        self.stream_in.write('azdfhfxem')
        self.stream_in.write('xem')
        self.stream_in.write('eowhldode')
        self.stream_in.write('dode')
        self.stream_in.write('wlclsnht')
        self.stream_in.write('ct')
        self.stream_in.write('bpflheocamv')
        self.stream_in.write('v')
        self.stream_in.write('flejfh')
        self.stream_in.write('hixqqbnikthccagc')
        self.stream_in.write('dugt')
        self.stream_in.write('eebmbpykcsmi')
        self.stream_in.write('oivgrzwppny')
        self.stream_in.write('zhfyiuu')
        self.stream_in.write('ebkqjcbcwviqkojnzyruwygtbvwws')
        self.stream_in.write('bofzr')
        expect = 'YES\n' + 'YES\n' + 'YES\n' + 'YES\n' + 'YES\n' + 'YES\n' + 'NO\n' + 'NO\n' + 'NO\n' + 'NO\n'
        special_typing.special_typing()
        result = ''
        for i in range(len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_special_typing4(self):
        self.stream_in.write('1')
        self.stream_in.write('abx')
        self.stream_in.write('ab')
        expect = 'NO\n'
        special_typing.special_typing()
        result = ''
        for i in range(len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_special_typing5(self):
        self.stream_in.write('1')
        self.stream_in.write('abcdef')
        self.stream_in.write('abc')
        expect = 'NO\n'
        special_typing.special_typing()
        result = ''
        for i in range(len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

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
        if len(self.buff) > 10000:
            sys.exit("Too many outputs, error! There may be an endless loop in your code!")

    def readline(self):
        if len(self.buff) > 0:
            cur = self.buff[0]
            del self.buff[0]
            return cur
        return ''
