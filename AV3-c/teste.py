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
    nome = names.get_first_name()
    email = f"{nome.lower()}@gmail.com"
    cpf = f"{np.random.randint(100,1000)}.{np.random.randint(100,1000)}.{np.random.randint(100,1000)}-{np.random.randint(10,100)}"
    semestre = f"{np.random.randint(0, 7)}"
    curso = cursos[np.random.randint(0, 2)]

    cursor.execute(f"INSERT INTO faculdade(nome,email,cpf,semestre,curso, v) VALUES ('{nome}', '{email}', '{cpf}','{semestre}','{curso}', 1)")

mydb.commit()
