# -*- coding: utf-8 -*-
import mysql.connector
import openpyxl


cnx = mysql.connector.connect(user='user', password='password',
                              host='ip', database='db')
cursor = cnx.cursor()


workbook = openpyxl.load_workbook('path\\filename.xlsx')
sheet = workbook['Лист1']

batch_size = 1000
rows = [row for row in sheet.iter_rows(values_only=True)]
sql = "INSERT INTO Data_Analyst.diagnosis (column_1, column_2) VALUES (%s, %s)"
for i in range(0, len(rows), batch_size):
    cursor.executemany(sql, rows[i:i+batch_size])

cnx.commit()

cursor.close()
cnx.close()


