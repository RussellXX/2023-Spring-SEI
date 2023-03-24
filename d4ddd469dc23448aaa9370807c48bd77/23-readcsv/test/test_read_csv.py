#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
from src import read_csv

resource1 = 'test/resource-1.csv'
resource2 = 'test/resource-2.csv'
raw1 = 'test/rawdata1-ReadOnly.csv'
raw2 = 'test/rawdata2-ReadOnly.csv'


class TestReadCSV(unittest.TestCase):
    def setUp(self):
        self.stream_out = MyStream()
        self.stream_in = MyStream()
        self.out_stream = sys.stdout
        self.in_stream = sys.stdin
        sys.stdout = self.stream_out
        sys.stdin = self.stream_in
        pass

    def test_read_csv1(self):
        self.stream_in.write('1')
        self.stream_in.write('INSERT Happy,staff,30000')
        read_csv.getcommand(resource1)
        self.stream_in.write('1')
        self.stream_in.write('SHOWALL')
        read_csv.getcommand(resource1)
        expect = 'Name     Title   Salary\n' + 'Happy    staff   30000.00\n' + 'David    staff   41500.00\n' + 'Micheal  staff   50000.00\n' + 'Oliver   staff   50500.00\n' + 'Zarnecki staff   51500.00\n' + 'Ling     ceo     55900.00\n' + 'Johnson  manager 56500.00\n' + 'AVG:47985.71\n'
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_read_csv2(self):
        self.stream_in.write('1')
        self.stream_in.write('SHOWALL')
        read_csv.getcommand(resource2)
        expect = 'Name      Title   Salary\n' + 'JingLan   staff   51500.00\n' + 'JinboHu   manager 66500.00\n' + 'SiyuanCen ceo     85900.00\n' + 'AVG:67966.67\n'
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_read_csv3(self):
        self.stream_in.write('3')
        self.stream_in.write('INSERT Happy,staff,30000')
        self.stream_in.write('INSERT QinLiu,cto,99900')
        self.stream_in.write('SHOWALL')
        read_csv.getcommand(resource2)
        expect = 'Name      Title   Salary\n' + 'Happy     staff   30000.00\n' + 'JingLan   staff   51500.00\n' + 'JinboHu   manager 66500.00\n' + 'SiyuanCen ceo     85900.00\n' + 'QinLiu    cto     99900.00\n' + 'AVG:66760.00\n'
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def test_read_csv4(self):
        self.stream_in.write('8')
        self.stream_in.write('INSERT Happy,staff,30000')
        self.stream_in.write('INSERT A,cto,90000')
        self.stream_in.write('INSERT B,cto,99900')
        self.stream_in.write('INSERT C,staff,9970')
        self.stream_in.write('INSERT D,staff,9900')
        self.stream_in.write('INSERT E,cto,99600')
        self.stream_in.write('INSERT F,cto,1000')
        self.stream_in.write('INSERT G,cto,3000')
        read_csv.getcommand(resource2)
        self.stream_in.write('1')
        self.stream_in.write('SHOWALL')
        read_csv.getcommand(resource2)
        expect = 'Name      Title   Salary\n' + 'F         cto     1000.00\n' + 'G         cto     3000.00\n' + 'D         staff   9900.00\n' + 'C         staff   9970.00\n' + 'Happy     staff   30000.00\n' + 'JingLan   staff   51500.00\n' + 'JinboHu   manager 66500.00\n' + 'SiyuanCen ceo     85900.00\n' + 'A         cto     90000.00\n' + 'E         cto     99600.00\n' + 'B         cto     99900.00\n' + 'AVG:49751.82\n'
        result = ''
        for i in range(0, len(self.stream_out.buff)):
            result = result + self.stream_out.buff[i]
        self.assertEqual(expect, result)

    def tearDown(self):
        sys.stdout = self.out_stream
        sys.stdin = self.in_stream
        f1 = open(raw1)
        f2 = open(resource1, 'w')
        f2.write(f1.read())
        f2.close()
        f1.close()
        f1 = open(raw2)
        f2 = open(resource2, 'w')
        f2.write(f1.read())
        f2.close()
        f1.close()
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


if __name__ == '__main__':
    print(unittest.main)
