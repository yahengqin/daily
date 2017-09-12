import os
import configparser
import logging


class Config:
    def __init__(self):
        # 这里有个问题，路径写成相对路径后，是以启动的文件路径作为相对路径的，这里以main.py所在目录为基准
        self.path = "../config/config.ini"
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path)

    def get(self, field, key):
        try:
            result = self.cf.get(field, key)
        except Exception as e:
            logging.exception(e)
            return False
        return result

    def set(self, field, key, value):
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w'))
        except Exception as e:
            logging.exception(e)
            return False
        return True
