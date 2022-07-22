import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=#"<password>",
  database='test'
)

mycursor = mydb.cursor()

def create_doctor_load():
    sql = "insert into Doctor1(doc_id, name, ph_no, speciality, e_mail) values( %s, %s, %s, %s, %s)"
  
    val =[("D001", "Doctor 1", 9457892345, "Cardiologist", "d1@gmail.com"),
            ("D002", "Doctor 2", 9792345672, "Optician", "d2@gmail.com"),
            ("D003", "Doctor 3", 9492346785, "Dentist", "d3@yahoo.co.in"),
            ("D004", "Doctor 4", 9423567923, "General Physician", "d4@google.com"),
            ("D005", "Doctor 5", 9456223236, "ENT Specialist", "d5@gmail.com"),
            ("D006", "Doctor 6", 8232426742, "General Physician", "d6@gmail.com"),
            ("D007", "Doctor 7", 9234545611, "Dentist", "d7@yahoo.com"),
            ("D008", "Doctor 8", 7230009999, "Optician", "d8@gmail.com"),
            ("D009", "Doctor 9", 8000790023, "ENT Specialist", "d9@gmail.com"),
            ("D010", "Doctor 10", 9456326665, "Cardiologist", "d10@gmail.com")]
    
    mycursor.executemany(sql, val)
    mydb.commit()