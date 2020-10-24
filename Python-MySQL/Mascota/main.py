#Actividad 12 Mascotas
import mysql.connector

bd = mysql.connector.connect(user='cam',password='12345678',database='mascotas')
cursor = bd.cursor()

while True:
    print ('1) Agregar empleado')
    print ('2) Mostrar empleadoss')
    print ('0) Salir')
    op = input()

    if op == '1':
        nombre = input ('nombre: ')
        apellidos = input ('apellidos: ')
        correo = input ('correo: ')
        contra = input ('contraseña: ')
        foto = input ('foto: ')
        profesion = input ('profesion: ')

        consulta = "INSERT INTO empleado_veterinaria(nombre, apellidos, correo, contrasena, foto, profesion) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(consulta,(nombre,apellidos,correo,contra,foto,profesion))
        bd.commit()
        if cursor.rowcount:
            print ("Se agrego empleado")
        else:
            print("Error")
        
    elif op == '2':
        consulta = "SELECT * FROM empleado_veterinaria"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print("id: ",row[0])
            print("nombre: ",row[1])
            print("apellidos: ",row[2])
            print("correo: ",row[3])
            print("contraseña: ",row[4])
            print("foto: ",row[5])
            print("profesion: ",row[6])
            
    elif op == '0':
        break
