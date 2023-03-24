#! /usr/bin/env python
# -*- coding: utf-8 -*-


def process(param):
	L1 = filter(lambda x: len(x) > 1, param)
	L2 = map(lambda x: x.title(), L1)
	return ','.join(L2)
