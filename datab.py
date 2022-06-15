import pymysql
def connect(update, context):
    db= pymysql.connect(
        host='sql5.freemysqlhosting.net',
        user='sql5499180',
        password='K1tSivryHS',
        db = 'PRODUCTOS_CUPCAKE'
    )
    update.message.reply_text('Conectando a la base de datos')
    cursor = db.cursor()
    return db, cursor

def create_table(update, context):
    db, cursor = connect(update, context)
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS users (
            name text,
            username text,
            id INTEGER
        )
    """)
    update.message.reply_text('Tabla creada')
    db.commit()
    db.close()

def delete_table(update, context):
    db, cursor = connect(update, context)
    cursor.execute(f"""
        DROP TABLE users
    """)
    update.message.reply_text('Tabla eliminada')
    db.commit()
    db.close()

def show_users(update, context):
    db, cursor = connect(update, context)
    cursor.execute(f"""
        SELECT * FROM users
    """)
    update.message.reply_text(f'{cursor.fetchall()}')
    db.commit()
    db.close()

def register(update, context):
    name = update.effective_user.first_name
    username = update.effective_user.username
    id = update.effective_user.id
    db, cursor = connect(update, context)
    cursor.execute(f"""SELECT * FROM users WHERE name = '{name}' AND username = '{username}' AND id = '{id}'""")
    if cursor.fetchall():
        update.message.reply_text('Usuario Ya existe')
    elif name is None or username is None:
        update.message.reply_text('Te falta gregar')
    else:
        cursor.execute(f"""
            INSERT INTO users (name, username, id)
            VALUES ('{name}', '{username}', '{id}')
        """)
        update.message.reply_text('registrado')
        db.commit()
        db.close()

def logout(update, context):
    db, cursor = connect(update, context)
    name = update.effective_user.first_name
    username = update.effective_user.username
    id = update.effective_user.id
    cursor.execute(f"""
        DELETE FROM users WHERE name = '{name}' AND username = '{username}' AND id = '{id}'
    """)
    update.message.reply_text('Usuario eliminado')
    db.commit()
    db.close()
