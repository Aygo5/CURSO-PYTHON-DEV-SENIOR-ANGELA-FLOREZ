estudiantes=[]
cursos=['Python', 'Java']
docentes= []
horarios= []

 #funcion para matricular estudiantes
def matricularEstudiante():
    nombre= input("Digite el nombre del estudiante: ")
    print("Seleccione el curso a matricular: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
    
    cursoSeleccionado= int(input("Ingrese el numero del curso: "))
    if cursoSeleccionado >0 and cursoSeleccionado <= len(cursos):
        curso= cursos[cursoSeleccionado-1]  
        estudiante= {'nombre': nombre, 'curso': curso}
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre}, matriculado en el curso {curso}')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos')

#funcion para asignar un docente a un curso
def asignarDocente():
    print("Seleccionar el curso al que desea asignar un docente: ")
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    cursoSeleccionado= int(input("Ingrese el numero del curso: "))
    if cursoSeleccionado >0 and cursoSeleccionado <= len(cursos):
        curso= cursos[cursoSeleccionado-1]  
        nombreDocente= input('Ingrese el nombre del docente: ')
        docente= {'nombre': nombreDocente, 'curso': curso}
        docentes.append(docente)
        print(f'Docente: {nombreDocente}, asignado al curso {curso}')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos')

#funcion para asignar horarios a un curso
def asignarHorario():
    print("Seleccionar el curso al que desa asignar el horario: ")
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    cursoSeleccionado= int(input("Ingrese el numero del curso: "))
    if cursoSeleccionado >0 and cursoSeleccionado <= len(cursos):
        curso= cursos[cursoSeleccionado-1]  
        dias= input("Ingrese los días de clase (ej: martes y jueves): ")
        hora= input("Ingrese la hora: ")
        horario= {'curso': curso, 'dias':dias, 'hora':hora}
        horarios.append(horario)
        print(f'Horario asiganado al curso: {curso}: {dias} a las {hora}')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos')
 
def mostrarEstudiantes():
    if estudiantes:
        print('Lista de estudiantes matriculados: ')
        for estudiante in estudiantes:
            print(f'Estudiante: {estudiante['nombre']}, Curso: {estudiante['curso']}')
    else:
        print('No hay estudiantes matriculados')  

def mostrarDocentes():
    if docentes:
        print('Lista de estudiantes matriculados: ')
        for docente in docentes:
            print(f'Estudiante: {docente['nombre']}, Curso: {docente['curso']}')
    else:
        print('No hay docentes asignados')  

def mostrarHorarios():
    if horarios:
        print('\nHorarios de los cursos: ')
        for horario in horarios:
            print(f'Curso: {horario['curso']}, Dias: {horario['dias']}, Hora: {horario['hora']}')
    else:
        print('No hay horarios asignados')  

while True:
    print('\n Sistema de matrícula Dev Senior')
    print('1. Matricular estudiante')
    print('2. Asignar docente a un curso')
    print('3. Asignar horario a un curso')
    print('4. Mostrar la lista de estudiantes matriculados')
    print('5. Mostrar la lista de docentes asignados')
    print('6. Mostrar horarios de los cursos')
    print('7. Salir')

    opcion= int(input('Digite la opcion: '))
    if opcion==1:
        matricularEstudiante()
    elif opcion==2:
        asignarDocente()
    elif opcion==3:
        asignarHorario()
    elif opcion==4:
        mostrarEstudiantes()
    elif opcion==5:
        mostrarDocentes()
    elif opcion==6:
        mostrarHorarios()
    elif opcion==7:
        print('Gracias por usar el sistema de matricula de Dev Senior')
        break
    else:
        print('Opcion no válida')
        

            




