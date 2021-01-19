#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collec = client.logs.nginx

    print(f'{collec.count_documents({})} logs')
    print('Methods:')

    print(f'method GET: {collec.count_documents({"method": "GET"})}')
    print(f'method POST: {collec.count_documents({"method": "POST"})}')
    print(f'method PUT: {collec.count_documents({"method": "PUT"})}')
    print(f'method PATCH: {collec.count_documents({"method": "PATCH"})}')
    print(f'method DELETE: {collec.count_documents({"method": "DELETE"})}')
    print(f'{collec.count_documents({"path": "/status"})} status check')
