import os
import yagmail
from dotenv import load_dotenv
from loguru import logger
import sqlite3


def send_email(to, subject, contents, attachments=None):

    try:
        load_dotenv()
        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASS")

        if not sender_email or not sender_password:
            raise ValueError("Sender Email or Password not found in environment variables")

        yag = yagmail.SMTP(sender_email, sender_password)

        yag.send(
            to=to,
            subject=subject,
            contents=contents,
            attachments=attachments
        )

        logger.success("Email sent succesfully!")

    except Exception as x:
        logger.error(f"An error occured while sending the email: {str(e)}")
        return False
    
    else:    
        return True
    
    finally:
        if yag in locals():
            yag.close()




def get_connection():
    return sqlite3.connect("Email_manager.db")



def insert(table, data):

    conn = get_connection()
    cursor = conn.cursor()

    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?'] * len(data))
    values = tuple(data.values())

    query = f"INSERT INTO {table} ({columns}) values ({placeholders})"
    cursor.execute(query, values)
    conn.commit()
    conn.close()



def fetch(table, columns="*", where=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"SELECT {columns} FROM {table}"

    if where:
        conditions = ' AND '.join([f"{k}=?" for k in where])
        query += f"WHERE {conditions}"
        values = tuple(where.values())
        cursor.execute(query, values)

    else: 
        cursor.execute(query)   


    rows = cursor.fetchall()
    conn.close()
    return rows     



def update(table, data, where):
    conn = get_connection()
    cursor = conn.cursor()

    set_clause = ', '.join([f"{k}=?" for k in data])
    where_clause = ', '.join([f"{k}=?" for k in where])

    query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
    values = tuple(data.values()) + tuple(where.values())

    cursor.execute(query, values)
    conn.commit()
    conn.close()



def delete(table, where):
    conn = get_connection()
    cursor = conn.cursor()


    where_clause = ' AND '.join([f"{k}=?" for k in where])
    query = f"DELETE FROM {table} WHERE {where_clause}"

    values = tuple(where.values())

    cursor.execute(query, values)
    conn.commit()
    conn.close()































