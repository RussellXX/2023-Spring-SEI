#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from src import stream_process


class TestStreamProcess(unittest.TestCase):
	def setUp(self):
		pass

	def test_stream_process(self):
		expect = 'Neal,Stu,Rich,Bob'
		result = stream_process.process(['neal', 's', 'stu', 'j', 'rich', 'bob'])
		self.assertEqual(expect, result)

	def tearDown(self):
		pass


if __name__ == '__main__':
	print(unittest.main)
