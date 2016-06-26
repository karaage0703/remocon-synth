#! /usr/bin/python
# -*- mode:python; coding:utf-8 -*-
#
# ring.py -
#
# Copyright(C) 2009 by mzp
# Author: MIZUNO Hiroki / mzpppp at gmail dot com
# http://howdyworld.org
#
# Timestamp: 2009/07/06 21:25:02
#
# This program is free software; you can redistribute it and/or
# modify it under MIT Lincence.
# modified by karaage0703 2016/06/26 for addapting usecase and python3

class SequenceBuffer:
    def __init__(self,size):
        self.buffer = [0 for i in range(0,size)]
        self.size = size
        self.pos = 0

    def add(self,val):
        for i in range(self.size, 0, -1):
            self.buffer[i-1] = self.buffer[i-2]
        self.buffer[0] = val

    def get(self):
        val = self.buffer[self.pos]
        self.pos = (self.pos + 1) % self.size
        return val
