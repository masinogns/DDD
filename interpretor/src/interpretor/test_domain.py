from statistics import mode
from typing import Optional, List, Set
# from collections import namedtuple

import unittest
from datetime import date

import pandas as pd
import json
import os

from domain import domain

class TestModel(unittest.TestCase):
    def test_etl_config(self):
        
        abs_path = os.path.join(os.getcwd(), "interpretor\src\interpretor")
        file_path = os.path.join(abs_path, os.path.join("domain", "model.json"))
        print(file_path)
        
        with open(file_path) as file:
            schema = json.load(file)
        
        _SOURCE = 'source'
        _TARGET = 'target'
        _ATTR = 'attribute'
        _OBJECT = 'table_name'
        # print(schema)
        for key, value in schema.items():
            pair = zip(value[_SOURCE][_ATTR],
                       value[_TARGET][_ATTR])
            
            object = domain.ObjectSchema(
                id = key
                , source=value[_SOURCE][_OBJECT]
                , target=value[_TARGET][_OBJECT]                
                , attribute= list(pair)
            )
            print(object)
        
        print(object.id)
        print(object.source)
        print(object.target)
        print(object.attribute)
        
                
                




if __name__ == '__main__':
    unittest.main()
    