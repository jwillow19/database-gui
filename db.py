import mysql.connector
# Connect to MySQL DB
# db = mysql.connector.connect(
#     database='inventory_db',
#     host='localhost',
#     user='root',
#     passwd='y5832592_Y'
# )

# db = ()
# # Create Cursor object - instantiates objects that can execute operations such as SQL statements
# mycursor = db.cursor()

# Query with cursor.execute('QUERY')
# mycursor.execute(
#     'CREATE TABLE products(model varchar(20))')


class Database:
    # __init__ === class constructor in JS; self == this
    def __init__(self, db):
        self.conn = mysql.connector.connect(database=db,
                                            host='localhost',
                                            user='root',
                                            passwd='y5832592_Y')
        # cursor
        self.cur = self.conn.cursor()
        # Execute
        self.cur.execute('CREATE TABLE IF NOT EXISTS products (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, model VARCHAR(20) NOT NULL, brand VARCHAR(20) NOT NULL, size VARCHAR(15) NOT NULL, color VARCHAR(100) NOT NULL, stock_quantity INT NOT NULL DEFAULT 0, gender VARCHAR(10) NOT NULL, shape VARCHAR(50) NOT NULL, frame_type VARCHAR(100) NOT NULL, style VARCHAR(255) NOT NULL, price DECIMAL(6,2) NOT NULL, created_at TIMESTAMP DEFAULT NOW(), quantity_sold INT NOT NULL DEFAULT 0, unique key model_color (model, color) )')
        # Commit
        self.conn.commit()

    # CRUD
    def fetch(self):
        self.cur.execute('SELECT * FROM products')
        # store query results from cursor object to rows
        rows = self.cur.fetchall()
        return rows

    def insert(self, model, brand, size, color, stock_quantity, price, gender, frame_type, shape, style):
        self.cur.execute('INSERT INTO products (model, brand, size, color, stock_quantity, price, gender, frame_type, shape, style) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE stock_quantity = stock_quantity + VALUES(stock_quantity)',
                         (model, brand, size, color, stock_quantity, price, gender, frame_type, shape, style))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute('DELETE FROM products WHERE id=%s', (id,))
        self.conn.commit()

    def update(self, id, model, brand, size, color, stock_quantity, price, gender, frame_type, shape, style):
        self.cur.execute('UPDATE products SET model=%s, brand=%s, size=%s, color=%s, stock_quantity=%s, price=%s, gender=%s, frame_type=%s, shape=%s, style=%s WHERE id=%s',
                         (model, brand, size, color, stock_quantity, price, gender, frame_type, shape, style, id))
        self.conn.commit()
    # Destructor - called when ojbect is deleted

    def __del__(self):
        self.conn.close()


# db = Database('inventory_db')
# db.insert('RB3005', 'RayBan', '52-21-150', 'black', 10, 199,
#           'Both', 'eyeglasses', 'circle', 'metal, plastic')
# db.insert('RB3006', 'RayBan', '52-21-150', 'black, red, blue', 4, 199,
#           'Both', 'sunglasses', 'aviator', 'metal, plastic')
# db.insert('BOSS55', 'BOSS', '52-21-150', 'silver', 10, 220,
#           'Both', 'eyeglasses', 'circle', 'wood')
# db.insert('GG01235OK', 'Gucci', '52-21-150', 'silver', 5, 280,
#           'Both', 'eyeglasses', 'circle', 'metal')
# db.insert('SL1000', 'SL', '52-21-150', 'silver', 4, 300,
#           'Both', 'eyeglasses', 'circle', 'metal')
# db.insert('SL1000', 'SL', '52-21-150', 'gold', 3, 300,
#           'Both', 'eyeglasses', 'circle', 'metal')
