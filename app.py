from flask import Flask,jsonify,request
import pymysql
import os
import jwt, datetime
from dotenv import load_dotenv
from functools import wraps
load_dotenv()
app = Flask(__name__)

def get_conn():
    print("connecting to db:", os.getenv('db_name', 'bachelor_life'))
    return pymysql.connect(
        host=os.getenv('db_host', 'localhost'),
        port=int(os.getenv('db_port', '3306')),
        user=os.getenv('db_user', 'root'),
        password=os.getenv('db_password', '7848893307'),
        database=os.getenv('db_name', 'bachelor_life'),
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )


@app.get("/")
def health():
	return {"ok": True, "service": "bachlife api"}
@app.get("/rentals")
def list_rentals():
	conn = get_conn()
	with conn:
		with conn.cursor() as cur:
			cur.execute("select id, title, location, monthly_rent, description, available from rentals where available=1")
			rows = cur.fetchall()
		return jsonify(rows)
@app.get("/food")
def list_food():
	conn = get_conn()
	with conn:
		with conn.cursor() as cur:
			cur.execute("select id, name, type, price, description from food")
			rows = cur.fetchall()
		return jsonify(rows)

@app.get("/essentials")
def list_essentials():
	conn = get_conn()
	with conn:
		with conn.cursor() as cur:
			cur.execute("select id, item, price, in_stock from essentials where in_stock > 0")
			rows = cur.fetchall()
	return jsonify(rows)

#####

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return {"error": "Token is missing"}, 401
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user_id = decoded["user_id"]
        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}, 401
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}, 401
        return f(*args, **kwargs)
    return decorated

#####
@app.post("/order")
@token_required
def place_order():
	data = request.get_json(silent=True) or {}
	user_id = request.user_id
	category = data.get("category")
	item_id = data.get("item_id")

	if not user_id or category not in ("rental", "food", "essential") or not item_id:
		return {"error": "user_id, category[rental|food|essential], item_id are required"}, 400
########################
	conn = get_conn()
	with conn:
		with conn.cursor() as cur:
			if category == "essential":
				cur.execute("select in_stock from essentials where id=%s", (item_id,))
				row = cur.fetchone()
				if not row:
					return {"error": "essential not found"}, 404
				if row["in_stock"] <= 0:
					return {"error": "out of stock"}, 400

				cur.execute("insert into orders (user_id, category, item_id, status) values (%s,%s,%s,'pending')",(user_id, category, item_id))
				cur.execute("update essentials set in_stock = in_stock - 1 where id=%s", (item_id,))
				return {"message": "order placed", "order_id": cur.lastrowid}, 201
			
			elif category == "food":
				cur.execute("select id from food where id=%s", (item_id,))
				if not cur.fetchone():
					return {"error": "food not found"}, 404
				cur.execute("insert into orders (user_id, category, item_id, status) values (%s,%s,%s,'pending')",(user_id, category, item_id))
				return {"message": "order placed", "order_id": cur.lastrowid}, 201

			else:  # rental
				cur.execute("select available from rentals where id=%s", (item_id,))
				row = cur.fetchone()
				if not row:
					return {"error": "rental not found"}, 404
				if not row["available"]:
					return {"error": "rental not available"}, 400
				cur.execute("insert into orders (user_id, category, item_id, status) values (%s,%s,%s,'pending')",(user_id, category, item_id))
				cur.execute("update rentals set available=0 where id=%s", (item_id,))
				return {"message": "order placed", "order_id": cur.lastrowid}, 201

@app.get("/orders/<int:user_id>")
def user_orders(user_id):
	conn = get_conn()
	with conn:
		with conn.cursor() as cur:
			cur.execute("select id, category, item_id, status, created_at from orders where user_id=%s order by created_at desc", (user_id,))
			rows = cur.fetchall()
			return jsonify(rows)
@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        return jsonify([
            {"id": 1, "item": "Camera", "qty": 2},
            {"id": 2, "item": "Tripod", "qty": 1}
        ])
    elif request.method == "POST":
        data = request.json
        return jsonify({"ok": True, "order": data}), 201
# @app.get("/rentals")

# @app.get("/food")

# @app.get("/essentials")

@app.get("/users")
def list_users():
    try:
        conn = get_conn()
        with conn:
            with conn.cursor() as cur:
                cur.execute("select id, name, email, phone_no from user")
                rows = cur.fetchall()
        return jsonify(rows)
    except Exception as e:
        print("❌ Error in /users:", e)
        return jsonify([])   # return empty array instead of crashing


SECRET_KEY = "supersecret"  # you can put this in .env

@app.post("/login")
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, email, password FROM user WHERE email=%s", (email,))
            user = cur.fetchone()

            if not user or user["password"] != password:
                return {"error": "Invalid email or password"}, 401

            payload = {
                "user_id": user["id"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            return {"message": "Login successful", "token": token, "user_id": user["id"]}


if __name__ == "__main__":
	app.run(debug=True)

