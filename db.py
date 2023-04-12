import psycopg2



def get_db():
  db = psycopg2.connect(dbname="railway", user="postgres", password="CyeeKQrcQ3mAMWvJMkQO", host="containers-us-west-121.railway.app", port="6407") 
  return db


# cur = db.cursor()

# sql2= "INSERT INTO persons (name, age) VALUES ('Adriele', 23)"
# cur.execute(sql2)
# conn.commit()

# sql = "SELECT * FROM task"

# cur.execute(sql)
# res = cur.fetchall()

# print(res)