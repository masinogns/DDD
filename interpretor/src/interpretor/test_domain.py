
from dataclasses import dataclass

from statistics import mode
from typing import Optional, List, Set
from collections import namedtuple

import unittest
from datetime import date

import pandas as pd
import json
import os

from domain import repository

class TestModel(unittest.TestCase):
    def test_etl_config(self):
        
        abs_path = os.path.join(os.getcwd(), "interpretor\src\interpretor")
        file_path = os.path.join(abs_path, os.path.join("domain", "model.json"))
        print(file_path)
        
        with open(file_path) as file:
            schema = json.load(file)

        
        a = repository.ObjectSchema("", schema)
        print(a)
        



if __name__ == '__main__':
    unittest.main()
    