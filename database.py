import mysql.connector
import config

connection  = mysql.connector.connect(
  host = config.HOST,
  user = config.USER,
  password = config.PASSWORD,
  database = config.DATABASE
)


cursor = connection.cursor()
cursor.execute("CREATE TABLE paul_table (id INT AUTO_INCREMENT PRIMARY KEY, TIME VARCHAR(255), SCENARIO VARCHAR(255), USER_MSG_1 VARCHAR(255), BOT_MSG_1 VARCHAR(255), USER_MSG_2 VARCHAR(255), BOT_MSG_2 VARCHAR(255), USER_MSG_3 VARCHAR(255), BOT_MSG_3 VARCHAR(255), USER_MSG_4 VARCHAR(255), BOT_MSG_4 VARCHAR(255))")
cursor = connection.cursor()
connection.commit()
print("Table Name Created : paul_table")
