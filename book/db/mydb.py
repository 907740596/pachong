# -*- coding: utf-8 -*-
__author__ = 'zhougy'
__date__ = '2018/6/7 上午12:30'

'''
采用sqlalchemy实现实体类的ORM映射
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index

MYSQL_DB_MAP = {
    'USER': 'root',  # 登陆用户名
    'PASSWORD': 'root',  # 登陆密码
    'HOST': '127.0.0.1',  # 数据库地址
    'PORT': 3306,
    'DATABASE': 'shucheng',  # 数据库名称
}

# mysql_conn_str = "mysql+pymysql://django:123456@192.168.58.12:3306/bookstore"
# 一定要按照顺序
mysql_conn_str = f"mysql+pymysql://{MYSQL_DB_MAP['USER']}:{MYSQL_DB_MAP['PASSWORD']}@{MYSQL_DB_MAP['HOST']}:{MYSQL_DB_MAP['PORT']}/{MYSQL_DB_MAP['DATABASE']}"

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/shucheng",
                       max_overflow=5)
Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    image_url= Column(String(500))
    book_name = Column(String(500))
    bool_jianjie = Column(String(500))
    book_id = Column(String(500))
    book_type = Column(String(500))
    booker = Column(String(125))


class Text(Base):
    __tablename__ = 'bookd'
    id = Column(Integer, primary_key=True)
    text_id = Column(String(500))
    book_title = Column(String(500))
    book_text = Column(String(1024))






def init_db():
    Base.metadata.create_all(engine)


'''
将ORM类映射到db数据库中，产生DB表
'''


def create_session():
    init_db()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


'''
objs-- 传入的ORM类对象或者对象列表
'''


def add_records(session, objs):
    if isinstance(objs, list):
        session.add_all(objs)
    else:
        session.add(objs)
    session.commit()


'''
查询数据
'''


def query_records(session, Cls, Conditions=None):
    if Conditions == None:
        return session.query(Cls).all()
    return session.query(Cls).filter_by(Conditions).all()


if __name__ == "__main__":
    session = create_session()
    # print(session)
    # test(address='beijing')
    records = query_records(session, Text)
    for rec in records:
        print(rec.book_title + ', ' + rec.image_url)
