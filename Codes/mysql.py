import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='shreyas', db='aadhar', charset='utf8mb4')

cur = conn.cursor()
cur.execute("SELECT * FROM e_details")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()
