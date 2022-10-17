
from dataclasses import dataclass
from typing import Optional, List, Set

import unittest
from datetime import date

from domain import repository

import pandas as pd
import json
 

class TestModel(unittest.TestCase):
    def test_json_to_dataframe_one(self):
        control = repository.ControlConnection()
        
        json_data = { 
                        "WDB" : {
                            "ip": "Tom"
                            , "db_name": 60
                            , "type": "mongo"
                        },
                        "ZDB" : {
                            "ip": "James"
                            , "db_name": 89
                            , "type": "game chace"
                        },
                        "BDB" : {
                            "ip": "Jenny"
                            , "db_name": 79
                            , "type": "eeee"
                        }
                    }
        
        for key, value in pd.DataFrame.from_dict(json_data).items():
            control.allocate(repository.Connection(
                id=key, ip=value.ip, db_name=value.db_name, type=value.type
            ))
            # <ConnectionSet {Connection(id='WDB', ip='Tom', db_name=60, desc='mongo game')}>
        
        print(control)
        
    def test_database_mongo_session(self):
        conn = repository.Connection(
            id="WE"
            , ip="120.0.0.1"
            , db_name="web"
            , type="Mongo"
        )
        
        session = repository.SessionFactory(conn).get_instance()
        print(session)
        # sess = model.MongoSession(conn=conn).connect()

    def test_database_mysql_session(self):
        conn = repository.Connection(
            id="WE", ip="120.0.0.1", db_name="web", type="MySQL"
        )

        session = repository.SessionFactory(conn).get_instance()
        print(session)
        
    
if __name__ == '__main__':
    unittest.main()

