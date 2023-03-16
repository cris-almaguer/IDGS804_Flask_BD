from db import get_connection

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consulta_alumnos()')
        result_set = cursor.fetchall()
        for row in result_set:
            print(row)
except Exception as ex:
    print(str(ex))

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consulta_un_alumno(%s)', (1))
        result_set = cursor.fetchall()
        for row in result_set:
            print(row)
except Exception as ex:
    print(str(ex))

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agregar_alumno(%s, %s, %s)', ('Alejandro', 'Valdez', 'ale@gmail.com'))
        connection.commit()
        connection.close()
except Exception as ex:
    print(str(ex))