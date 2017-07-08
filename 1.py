# -*- coding:utf-8 -*-
import random

import re
import requests
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'newcoder')


def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10

    # continue , break , pass
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do special
        if i < 5:
            continue
        if i == 8:
            break
        print i


def demo_list():
    lista = [1, 2, 3]
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)  # 相当于lista+listb
    print 3, lista
    print 4, len(lista)
    print 5, 1 in listb
    listb.insert(0, 'www')  # 添加元素到listb中
    print 6, listb
    listb.pop(1)  # 从listb中删除元素
    print 7, listb
    listb.sort()
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    print 11, listb * 2
    listb.append('b')  # 添加元素到listb中
    print 12, listb
    listb.pop()  # 从listb末尾删除元素
    listb.pop()  # 从listb末尾删除元素
    print listb


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print dicta
    print dicta.keys(), dicta.values()
    print dicta.has_key(1), dicta.has_key('3')
    for key, value in dicta.items():
        print 'key-value:', key, value
    dictb = {'+': add, '-': sub}
    print dictb['+'](1, 2)
    print dictb.get('-')(15, 3)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(4)  # 从dicta中删除键值对
    print dicta
    del dicta[1]  # 从dicta中删除键值对
    print dicta
    dicta[1] = 1  # 直接添加元素到dicta中
    print dicta


def demo_set():
    seta = set((1, 2, 3))
    print seta
    listb = [2, 3, 4]
    setb = set(listb)
    print seta.intersection(setb), seta & setb
    print seta.union(setb), seta | setb
    print seta - setb
    seta.add('x')
    print seta


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im' + ' ' + self.name + ' ' + str(self.uid)


class Guest(User):
    def __repr__(self):
        return 'im guest:' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im' + ' ' + self.name + ' ' + str(self.uid) + ' ' + self.group


def creat_user(type):
    if type == 'USER':
        return User('U1', 1)
    elif type == 'ADMIN':
        return Admin('A1', 2, 'G1')
    else:
        return Guest('gu1', 3)


def demo_random():
    # random.seed(1)
    print 1, int(random.random() * 100)
    print 2, random.randint(0, 200)
    print 3, random.choice(range(0, 100, 10))
    print 4, random.sample(range(0, 100), 4)


def demo_re():
    str = 'abc12\r3df 3@08$dds'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1, p1.findall(str)
    print 2, p2.findall(str)
    str2 = 'a@163.com;12@gmail.com;dd@qq.com;E9@163.com'
    p3 = re.compile('\w+[@163|qq]+\.com')
    print 3, p3.findall(str2)
    str3 = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4, p4.findall(str3)
    p5 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5, p5.findall(str3)
    str4 = 'sss2017-07-08sdf'
    p6 = re.compile('\d{4}-\d{2}-\d{2}')
    print 6, p6.findall(str4)


if __name__ == '__main__':
    print 'hello newcoder'
    # demo_string()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    # demo_set()
    user1 = User('u1', 1)
    print user1
    admin1 = Admin('a1', 2, 'g1')
    print admin1
    print creat_user('ADMINX')
    # demo_random()
    demo_re()
