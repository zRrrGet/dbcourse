| query | total cost | elapsed time in python | Index type |
| ----- | ----- | ----- | ----- |
| EXPLAIN ANALYSE select * from customers WHERE review='TEXT'     | 53828.43     | 0.08437776565551758     | None     |
| EXPLAIN ANALYSE select * from customers WHERE review='TEXT'     | 8.69     | 0.0011832714080810547     | btree(review)     |
| EXPLAIN ANALYSE select * from customers WHERE name='TEXT'     | 53828.43    | 0.0839071273803711     | None     |
| EXPLAIN ANALYSE select * from customers WHERE name='TEXT'     | 50754.27     | 0.18270373344421387     | brin(name)     |
| EXPLAIN ANALYSE select * from customers WHERE name = 'TEXT' OR address='TEXT'    |   54870.20   | 0.08497858047485352     | None     |
| EXPLAIN ANALYSE select * from customers WHERE name = 'TEXT' OR address='TEXT'     |   16.98   | 0.0008382797241210938     | btree(name), btree(address)     |
| EXPLAIN ANALYSE select * from customers WHERE review = 'TEXT' OR address='TEXT'     |   54870.20   | 0.08732366561889648     | None     |
| EXPLAIN ANALYSE select * from customers WHERE review = 'TEXT' OR address='TEXT'     | 53589.64     | 0.14327549934387207    | brin(review), btree(address)     |
