from datetime import date
from datetime import timedelta
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=#"<password>",
  database='test'
)

mycursor = mydb.cursor()

today = date.today()

def create_single_entry (d_id, date1, start, end):
    sql = "insert into appointment1 (D_ID, P_ID, DTTM, T_Start, T_End) values (%s, %s, %s, %s, %s)"
    values = (d_id, None, date1, start, end)
    mycursor.execute(sql,values)
    mydb.commit()

def create_entry_for_date (d_id, date1):
    create_single_entry (d_id, date1, "10", "11")
    create_single_entry (d_id, date1, "11", "12")
    create_single_entry (d_id, date1, "12", "13")
    create_single_entry (d_id, date1, "14", "15")
    create_single_entry (d_id, date1, "15", "16")
    create_single_entry (d_id, date1, "16", "17")
    create_single_entry (d_id, date1, "17", "18")


def create_entry(d_id, days):
    today = date.today()
    for x in range (days):
        create_entry_for_date(d_id, today)
        today = today + timedelta(days=1)
