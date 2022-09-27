import math
import numpy as np

class MonticuloBinario:
    __arreglo = None
    __tamanio = None

    def __init__(self, tamanio = 10):
        self.__arreglo = np.empty(tamanio,dtype = int)
        self.__tamanio = tamanio
        self.__arreglo[0] = 0

    def insertar(self, elemento):
        if self.__arreglo[0] < self.__tamanio:
            self.__arreglo[self.__arreglo[0]+1] = elemento 
            actual = self.__arreglo[0]+1
            posicion_padre = math.floor((self.__arreglo[0]+1)/2)
            while posicion_padre != 0 and self.__arreglo[posicion_padre] > self.__arreglo[actual]:
                aux = self.__arreglo[actual]
                self.__arreglo[actual] = self.__arreglo[posicion_padre]
                self.__arreglo[posicion_padre] = aux
                actual = posicion_padre
                posicion_padre = math.floor(actual/2)
            self.__arreglo[0]+=1
        else:
            print('ERROR: arreglo lleno')
    
    def Eliminar_minimo(self):
        if self.vacio():
            print('ERROR: Arbol vacio!')
        else:
            self.__arreglo[1] = self.__arreglo[self.__arreglo[0]]
            self.__arreglo[0]-=1
            i = 1
            while i < self.__arreglo[0]:
                pHijo_izquierdo = i*2
                pHijo_derecho = (i*2)+1
                
                if pHijo_izquierdo <= self.__arreglo[0] and self.__arreglo[pHijo_izquierdo] < self.__arreglo[i]:
                   
                    aux =  self.__arreglo[i]
                    self.__arreglo[i] = self.__arreglo[pHijo_izquierdo]  

                    self.__arreglo[pHijo_izquierdo] = aux
             

                if pHijo_derecho <= self.__arreglo[0] and self.__arreglo[pHijo_derecho]< self.__arreglo[i]:
             
                    aux =  self.__arreglo[i]

                    self.__arreglo[i] = self.__arreglo[pHijo_derecho] 
                    self.__arreglo[pHijo_derecho] = aux
                  
                i+=1

    def mostrar(self):
        for i in range(1,self.__arreglo[0]+1):
            print(self.__arreglo[i])
    
    def lleno(self):
        return (self.__arreglo[0] == self.__tamanio)
    
    def vacio(self):
        return (self.__arreglo[0] == 0)






