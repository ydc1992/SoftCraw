# -*- coding: utf-8 -*-
from sqlalchemy import Column, String , DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 数据库 orm
class Rule(Base):
    __tablename__ = 'XiaZaiZhan'
    # 表的结构:
    id              = Column(Integer, primary_key=True)
    allow_domains   = Column(String)
    start_urls      = Column(String)
    extract_from    = Column(String)   #网址格式规则
    allow_url       = Column(String)
    isEnable       = Column(Integer)   #是否启动
    download_xpath  = Column(String)   #下载地址xpath