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
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE review=%s", ("6WTP37J0B6A20VRPCAVKKE6QC5EGMNTHK9S41HOZC062J7XVVFTZZXYSFYZ19IESY257RFYM04BGW5OILU5C4HKDQNBKWF4M8FG1GF1J3LSUKJFW981WS9MVFXDLF4Z8UVQSWWSGZAI1A3XQ1CG9N7Y78Q9VVTPFENUD59CZ0SFNA30I6CHYL02LTI0GTLNYIA7JRQIX5846HQLILF1ECIQJRZ1O4UH02KXTX5S31YHMQ13WS3WWW9W44X68APV",))
end = time.time()
print("ELAPSED TIME WITHOUT INDEX: ", end - start)
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON customers USING btree(review)")
start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE review=%s", ("6WTP37J0B6A20VRPCAVKKE6QC5EGMNTHK9S41HOZC062J7XVVFTZZXYSFYZ19IESY257RFYM04BGW5OILU5C4HKDQNBKWF4M8FG1GF1J3LSUKJFW981WS9MVFXDLF4Z8UVQSWWSGZAI1A3XQ1CG9N7Y78Q9VVTPFENUD59CZ0SFNA30I6CHYL02LTI0GTLNYIA7JRQIX5846HQLILF1ECIQJRZ1O4UH02KXTX5S31YHMQ13WS3WWW9W44X68APV",))
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
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE name=%s", ("O4Z0KG1DGZ1DA6J",))
end = time.time()
print("ELAPSED TIME WITHOUT INDEX: ", end - start)
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON customers USING brin(name)")
start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE name=%s", ("O4Z0KG1DGZ1DA6J",))
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
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE name = %s OR address=%s", ("PBLRT37P0Q2QPRO", "CREY91WUO3FEVTXIY6QOFL5W89XQOIB8ZZX7ZFHOEX0AXP9Q5BUQ3Q4UN5DVTKD",))
end = time.time()
print("ELAPSED TIME WITHOUT INDEX: ", end - start)
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON customers USING btree(name)")
cursor.execute("CREATE INDEX ON customers USING btree(address)")
start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE name = %s OR address=%s", ("PBLRT37P0Q2QPRO", "CREY91WUO3FEVTXIY6QOFL5W89XQOIB8ZZX7ZFHOEX0AXP9Q5BUQ3Q4UN5DVTKD",))
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
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE review = %s OR address=%s", ("NKSY9Y835AY3S12JBHM9UVRN8WLKW6BTPBMEXYD3EN6PAS3VS6HFLJZ45DRXW0JW0T917AX63SI8VC3S4IECQ2RJYFRG3H54YBMC4MSSNORSVAHZCLL575SJBWJCHS5J6SDW3Q24WWUCBGSR3MCUXX47LBP3YSKUTEMNJPB2VGJBNHHFY44C8TUFE6T53C7ALVC9Z3CBIAMEEEEFALM5V6UN6PIVNSRIUDRXQKPM5YGYLADLIGSJ0W4YDKGGK8V", "CREY91WUO3FEVTXIY6QOFL5W89XQOIB8ZZX7ZFHOEX0AXP9Q5BUQ3Q4UN5DVTKD",))
end = time.time()
print("ELAPSED TIME WITHOUT INDEX: ", end - start)
for row in cursor:
    print(row)

cursor.execute("CREATE INDEX ON customers USING brin(review)")
cursor.execute("CREATE INDEX ON customers USING btree(address)")
start = time.time()
cursor.execute("EXPLAIN ANALYSE select * from customers WHERE review = %s OR address=%s", ("NKSY9Y835AY3S12JBHM9UVRN8WLKW6BTPBMEXYD3EN6PAS3VS6HFLJZ45DRXW0JW0T917AX63SI8VC3S4IECQ2RJYFRG3H54YBMC4MSSNORSVAHZCLL575SJBWJCHS5J6SDW3Q24WWUCBGSR3MCUXX47LBP3YSKUTEMNJPB2VGJBNHHFY44C8TUFE6T53C7ALVC9Z3CBIAMEEEEFALM5V6UN6PIVNSRIUDRXQKPM5YGYLADLIGSJ0W4YDKGGK8V", "CREY91WUO3FEVTXIY6QOFL5W89XQOIB8ZZX7ZFHOEX0AXP9Q5BUQ3Q4UN5DVTKD",))
end = time.time()
print("ELAPSED TIME WITH brin review btree address INDEX:", end - start)
for row in cursor:
    print(row)
print("")
cursor.close()
conn.close()