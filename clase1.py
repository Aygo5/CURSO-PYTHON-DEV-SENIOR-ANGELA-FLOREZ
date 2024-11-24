estudiantes=[]
cursos=["Java","Python"]
docentes=[]
horarios=[]

#Funcion para matricular estudiantes
def matricularestudiantes():
    nombre= input("Digite nombre del estudiante: ")
    print("Seleccione el curso a matricular: ")
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    cursoSeleccionado = int(input("Ingrese el número del curso"))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso= cursos[cursoSeleccionado-1]
        estudiante={'Nombre: ': nombre, 'Curso: ': curso}
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre}, Matriculado en el Curso: {curso}')
    else:
        print(f"Opción de curso no valida, recuerde que solo hay {len(cursos)}")

#funcion para asignar docente
def asignarDocente():
    print('Seleccionar el curso al que desea asignar un docente: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}:{curso}')

    cursoSeleccionado = int(input("Ingrese el número del curso"))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso= cursos[cursoSeleccionado-1]
        nombreDocente= input('Ingrese el nombre del docente: ')
        docente={'Nombre: ': nombreDocente, 'Curso: ': curso}
        docentes.append(docente)
        print(f'Docente: {nombreDocente}, Asignado en el Curso: {curso}')
    else:
        print(f"Opción de curso no valida, recuerde que solo hay {len(cursos)}")

#funcion para asignar horario

def asignarHorario():
    print ('Seleccionar el curso al que deseas asginar el horario: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}:{curso}')

    cursoSeleccionado = int(input("Ingrese el número del curso"))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso= cursos[cursoSeleccionado-1]
        dias= input('Ingrese los días de clase (ej: martes y jueves): ')
        hora= input('Ingrese la hora de clase (ej: 6 pm): ')
        horario= {'Curso: ': curso, 'dias: ': dias, 'hora': hora}
        print(f'Horario asignado al curso: {curso}: {dias} a las {hora}')
    else:
        print(f"Opción de curso no valida, recuerde que solo hay {len(cursos)}")

def mostrarEstudiantes():
    if estudiantes:
        print(f'Lista de estudiantes matriculados')
        for estudiante in estudiantes:
            print(f'Estudiante: {estudiante['nombre']} Curso: {estudiante['curso']}')
        else:
            print('No hay estudiantes matriculados')

def mostrarDocentes():
    if mostrarDocentes:
        print(f'Lista de docentes asignados')
        for docente in estudiantes:
            print(f'Estudiante: {docente['nombre']} Curso: {docente['curso']}')
        else:
            print('No hay docentes asignados')

def mostrarHorarios():
    if estudiantes:
        print(f'\nHorarios de los cursos')
        for horario in horarios:
            print(f'Curso: {horario['curso']}, Dias: {horario{'dias'}}, Hora: {horario['hora']}')
        else:
            print('No hay horarios asignados')

