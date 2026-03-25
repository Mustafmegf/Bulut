from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2, os
app = Flask(__name__)
CORS(app)
DATABASE_URL = os.getenv(
 "DATABASE_URL",
 "postgresql://Bulut_user:ZYZZLk5MLtwbJgcFzFu2RRctCzyWHwse@dpg-d6t8rj75r7bs73a8bjt0-a.oregon-postgres.render.com/Bulut"
)
def connect_db():
  return psycopg2.connect(DATABASE_URL)
@app.route("/ziyaretciler", methods=["GET", "POST"])
def ziyaretciler():
  conn = connect_db()
  cur = conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim TEXT)")
  conn.commit()

cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
isimler = [row[0] for now in cur.fetchall()]

cur.close()
conn.close()

return jsonify(isimler)

if__name__=="__main__":
   app.run(host="0.0.0.0",port=5001)
