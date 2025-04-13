import psycopg2

config = {
    'dbname': 'users',
    'user': 'postgres', 
    'password': 'G0lden_wings222'
}

def get_connection():
    return psycopg2.connect(**config)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_scores (
            username TEXT PRIMARY KEY,
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_scores WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def add_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_scores (username) VALUES (%s)", (username,))
    conn.commit()
    cursor.close()
    conn.close()

def update_score_and_level(username, score, level):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE user_scores SET score = %s, level = %s WHERE username = %s
    """, (score, level, username))
    conn.commit()
    cursor.close()
    conn.close()