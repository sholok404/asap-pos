#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 22:38:54 2017

@author: sholok404
"""

import sqlite3
conn = sqlite3.connect('products.sqlite')

class Product(object):
    sl = 0
    def __init__(self, name, process, size, ttl, stock):
        (self.name, self.process, self.size, self.ttl, self.stock) = (name, process, size, ttl, stock)
        self.sl = Product.sl
        Product.sl += 1
    def get_name(self):
        return self.name
    def get_process(self):
        return self.process
    def get_size(self):
        return self.size
    def get_ttl(self):
        return self.ttl
    def get_stock(self):
        return self.stock

def get_product_data():
    cursor = conn.cursor()
    cursor.execute('SELECT Name, Process, Size, TTL FROM products')
    data = cursor.fetchall()
    return data

data = get_product_data()

for i in data:
    i[0][0] = Product(i[0], i[1], i[2], i[3], 0)