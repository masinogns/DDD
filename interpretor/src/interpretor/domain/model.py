from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set
from abc import ABCMeta, abstractmethod

class OutOfStock(Exception):
    pass


@dataclass(unsafe_hash=True)
class Connection:
    id: str
    ip: str
    db_name: str
    type: str
    # desc: str


class ControlConnection:      
    def __init__(self):
        self.connect_set = set()

    def allocate(self, conn: Connection):
        self.connect_set.add(conn)

    def __repr__(self) -> str:
        return f"<ConnectionSet {self.connect_set}>"


class Database(metaclass=ABCMeta):
    def __init__(self, conn:Connection):
        self.conn = conn

    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def add(self):
        pass
    
    
class mongoSession(Database):
    def __init__(self, conn: Connection):
        self._conn = conn
        
    def connect(self):
        return "Mongo Session {}".format(id)

    def get(self):
        return 'mongo get'
    
    def add(self):
        return 'mongo add'
    

class mysqlSession(Database):
    def __init__(self, conn: Connection):
        super().__init__(conn)
        
    def connect(self):
        return "MySQL Session"

    def get(self):
        return super().get()

    def add(self):
        return super().add()


class mssqlSession(Database):
    def __init__(self, conn: Connection):
        super().__init__(conn)
        
    def connect(self):
        return "MSSQL SEssion"

    def get(self):
        return super().get()

    def add(self):
        return super().add()

class SessionFactory(object):
    
    def __init__(self, conn:Connection):
        self.conn = conn
        self.db_choose = conn.type.lower() + "Session"
        
    def get_instance(self):
        # key is lower
        # db = {
        #     "mongo" : MongoSession
        #     , "mysql" : MySQLSession
        # }
        
        # return db[self.db_choose](self.conn).connect()
        return eval(self.db_choose)(self.conn).connect()
