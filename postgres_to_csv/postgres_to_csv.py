import psycopg2
import csv

# query = """
#         SELECT * FROM customer ORDER BY id
#     """
    
query = """
            SELECT c.*, t.* FROM customer c, cart t WHERE c.id = t.custid ORDER BY t.custid, t.cartnumber
    """

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=target")
cur = conn.cursor()
cur.execute(query)

# all = cur.fetchall()
# print all

with open('result.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for row in cur.fetchall():
        writer.writerow(row)


conn.close()

