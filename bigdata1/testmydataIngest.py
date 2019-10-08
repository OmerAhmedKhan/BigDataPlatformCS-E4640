import time
from pymongo import MongoClient
from helper import read_db, write_csv_to_db

client = MongoClient('34.69.192.142', 27017, username='root', password='FoSezeYin7Qr', authSource='admin')
n = 5
path = "/home/oak/Downloads/googleplaystore.csv"

tic = time.clock()
write_csv_to_db(client, path)
toc = time.clock()
print(toc-tic)

# tic = time.clock()
# for x in range(n):
#     read_db(client)
#
# toc = time.clock()
# print(toc-tic)
#
# n+=5
# tic = time.clock()
# for x in range(n):
#     read_db(client)
#
# toc = time.clock()
# print(toc - tic)
#
#
# n+=10
# tic = time.clock()
# for x in range(n):
#     read_db(client)
#
# toc = time.clock()
# print(toc - tic)
#
#
# n+=20
# tic = time.clock()
# for x in range(n):
#     read_db(client)
#
# toc = time.clock()
# print(toc - tic)
#
#
# n+=50
# tic = time.clock()
# for x in range(n):
#     read_db(client)
#
# toc = time.clock()
# print(toc - tic)

