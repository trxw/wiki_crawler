#!/usr/bin/python
import crawl_working_1
from pymongo import MongoClient

client = MongoClient()
test_database = client['test_database']
test_collection = test_database['test_collection']
