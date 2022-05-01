import psycopg2
import string    
import random 
import time

conn = psycopg2.connect(dbname='task1', user='postgres', host='localhost')
cursor = conn.cursor()
# for i in range(1, 1000001):
#     name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
#     address = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 63))
#     review = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 255))
#     cursor.execute("INSERT INTO customers (id, name, address, review) VALUES (%s, %s, %s, %s) RETURNING id, name, address, review", (i, name, address, review))
#     for row in cursor:
#         print(row)

start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE review=%s", ("TEXT",))
end = time.time()
print("ELAPSED TIME WITHOUT INDEX: ", end - start)
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON customers USING btree(review)")
start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE review=%s", ("TEXT",))
end = time.time()
print("ELAPSED TIME WITH btree INDEX:", end - start)
for row in cursor:
    print(row)

# conn.commit()
cursor.close()
conn.close()
#######################
conn = psycopg2.connect(dbname='task1', user='postgres', host='localhost')
cursor = conn.cursor()

start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE name=%s", ("TEXT",))
end = time.time()
print("ELAPSED TIME WITHOUT INDEX: ", end - start)
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON customers USING brin(name)")
start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE name=%s", ("TEXT",))
end = time.time()
print("ELAPSED TIME WITH brin INDEX:", end - start)
for row in cursor:
    print(row)
print("")
cursor.close()
conn.close()
#######################
conn = psycopg2.connect(dbname='task1', user='postgres', host='localhost')
cursor = conn.cursor()

start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE name = %s OR address=%s", ("TEXT", "TEXT",))
end = time.time()
print("ELAPSED TIME WITHOUT INDEX: ", end - start)
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON customers USING btree(name)")
cursor.execute("CREATE INDEX ON customers USING btree(address)")
start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE name = %s OR address=%s", ("TEXT", "TEXT",))
end = time.time()
print("ELAPSED TIME WITH btree address btree name INDEXES:", end - start)
for row in cursor:
    print(row)
print("")
cursor.close()
conn.close()
#######################
conn = psycopg2.connect(dbname='task1', user='postgres', host='localhost')
cursor = conn.cursor()

start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE review = %s OR address=%s", ("TEXT", "TEXT",))
end = time.time()
print("ELAPSED TIME WITHOUT INDEX: ", end - start)
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON customers USING brin(review)")
cursor.execute("CREATE INDEX ON customers USING btree(address)")
start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE review = %s OR address=%s", ("TEXT", "TEXT",))
end = time.time()
print("ELAPSED TIME WITH brin review btree address INDEX:", end - start)
for row in cursor:
    print(row)
print("")
cursor.close()
conn.close()