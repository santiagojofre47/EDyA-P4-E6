import random
from claseMonticuloBinario import MonticuloBinario

if __name__ == '__main__':
    lista_pacientes = MonticuloBinario(30)#capacidad para 30 pacientes
    tAtencion = 4
    tLlegada = 2
    timer_atencion = 0
    i = 0
    cant_atendidos = 0
    while i < 30:#Simulacion de media hora
        if 1/tLlegada == random.randint(0, 1)/tLlegada:#Analizamos llegada de un paciente
            print('Ha llegado un paciente!')
            unPaciente = random.randint(1,15)
            lista_pacientes.insertar(unPaciente)
        if timer_atencion == tAtencion:
            if not lista_pacientes.vacio():
                lista_pacientes.Eliminar_Minimo()
                cant_atendidos+=1
                print('Se atendio un paciente!')
            timer_atencion = 0
        
        timer_atencion+=1
        i+=1
    print('----- SIMULACION FINALIZADA -----')
    print('Cantidad de pacientes atendidos: {}'.format(cant_atendidos))
        



