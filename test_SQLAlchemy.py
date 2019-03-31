# -*- coding: utf-8 -*-

import os, sqlite3

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

engine = create_engine('sqlite:///data/test.db')
DBSession = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    score = Column(Integer)



def get_score_in(low, high):
    session = DBSession()
    try:
        users = session.query(User).filter(User.score>=low , User.score<=high).order_by(User.score).all()

        arr = []
        for user in users:
            arr.append((user.name,user.score))
        return arr

        # names = []
        # for record in result:
        #     names.append((record[0]))
        # return names
    finally:
        session.close()


def test_1():
    assert get_score_in(80, 95) == ['Adam']
    assert get_score_in(60, 80) == ['Bart', 'Lisa']
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam']
