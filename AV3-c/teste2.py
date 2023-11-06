import names
import mysql.connector
import numpy as np

mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  password="root",
  database="gabi"
)

cursor = mydb.cursor()

cursos = ["BCC", "BEE", "P"]

for i in range(100):
    nome = "Gabrielli"
    email = "gabrielli@gmail.com"
    cpf = "123.923.852-54"
    semestre = "4"
    curso = "BCC"

    cursor.execute(f"INSERT INTO faculdade(nome,email,cpf,semestre,curso, v) VALUES ('{nome}', '{email}', '{cpf}','{semestre}','{curso}', 1)")

mydb.commit()