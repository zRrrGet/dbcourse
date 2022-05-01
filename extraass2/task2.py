import psycopg2
import string    
import random 
import time

conn = psycopg2.connect(dbname='task1', user='postgres', host='localhost')
cursor = conn.cursor()

# for i in range(1, 100000):
#     cursor.execute("INSERT INTO purchases(id, customer_id) VALUES (%s, %s) RETURNING id, customer_id", (i, random.choice(range(1, 1000000))))
#     for row in cursor:
#         print(row)

types = [f"TYPE{x}" for x in range(1, 51)]

# for i in range(1, 100000):
#     name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
#     details = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
#     cursor.execute("INSERT INTO products(id, name, details, price, type) VALUES (%s, %s, %s, %s, %s) RETURNING id, name, details, price, type", (i, name, details, random.choice(range(1000, 1000000)), types[random.choice(range(0, 50))]))
#     for row in cursor:
#         print(row)

# for i in range(1, 100000):
#     cursor.execute("INSERT INTO purchases_products_list(id, purchase_id, product_id) VALUES (%s, %s, %s) RETURNING id, purchase_id, product_id", (i, i, random.choice(range(1, 100000))))
#     for row in cursor:
#         print(row)

# for i in range(0, 50):
#     cursor.execute("INSERT INTO sales(id, type, discount) VALUES (%s, %s, %s) RETURNING id, type, discount", (i+1, types[i], random.choice(range(1, 100))))
#     for row in cursor:
#         print(row)

# conn.commit()

# cursor.execute("SELECT pr.id, pr.name, pr.details, pr.price, pr.type FROM purchases p JOIN purchases_products_list ppl ON p.id = ppl.id JOIN products pr on p.id = pr.id JOIN sales s ON pr.type = s.type")
# for row in cursor:
#     print(row)

# cursor.execute("SELECT customer_id, SUM(d) FROM (SELECT p.customer_id, ((SUM(pr.price)/100*(s.discount))) d FROM purchases p JOIN purchases_products_list ppl ON p.id = ppl.id JOIN products pr on p.id = pr.id JOIN sales s ON pr.type = s.type GROUP BY p.customer_id, s.discount) n1 GROUP BY customer_id")
# for row in cursor:
#     print(row)

cursor.execute("SELECT pr.id, pr.name, pr.details, pr.price, pr.type FROM purchases p JOIN purchases_products_list ppl ON p.id = ppl.id JOIN products pr on p.id = pr.id JOIN sales s ON pr.type = s.type")
for row in cursor:
    print(row)

cursor.execute("SELECT customer_id, SUM(d) FROM (SELECT p.customer_id, ((SUM(pr.price)/100*(s.discount))) d FROM purchases p JOIN purchases_products_list ppl ON p.id = ppl.id JOIN products pr on p.id = pr.id JOIN sales s ON pr.type = s.type GROUP BY p.customer_id, s.discount) n1 GROUP BY customer_id")
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON products(type)")
cursor.execute("CREATE INDEX ON sales(type)")

cursor.close()
conn.close()