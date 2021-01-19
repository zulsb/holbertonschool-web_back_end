#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    collec = client.logs.nginx

    print(f'{collec.count_documents({})} logs')
    print('Methods:')

    print(f'\tmethod GET: {collec.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {collec.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {collec.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {collec.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {collec.count_documents({"method": "DELETE"})}')
    print(f'{collec.count_documents({"path": "/status"})} status check')
