# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:40:16 2023

@author: User

"""
import datetime
from dataclasses import dataclass
@dataclass
class nuevo_usuario:
        nombre: str = ""
        profesion: str = ""
        edad: int = 0
        monto: int = 0
        
        def informacion(self):        
            nombre = input("cual es su nombre completo\n")
            self.nombre = nombre        
            edad = input("Cual es su edad\n")
            self.edad = edad        
            opciones2 = input("presione '1' si es estudiante, presione '2' si ejerce un puesto de trabajo, presione '3' si es independiente, presione '4' si no actualmente esta desempleado\n")
            if opciones2 == "2":
                profesion = input("mencione cual es el puesto de trabajo y el nombre de la empresa\n")
                self.profesion = profesion
            elif opciones2 == "3":
                profesion = "independiente"
                self.profesion = profesion
            elif opciones2 == "4":
                profesion= "desempleado"  
                self.profesion = profesion
            elif opciones2 == "1":
                profesion = input("presione '1' si es estudiante de secundaria, presione '2' si es estudiente de educaion superior\n")
                self.profesion = profesion
                if profesion == "1":
                    profesion = "estudiante de secundaria"
                    self.profesion = profesion
                elif profesion == "2":
                    profesion = "estudiante de educacion superior"
                    self.profesion = profesion
        def __str__(self):
            return f"nombre: {self.nombre}, profesion:{self.profesion}, edad:{self.edad}, monto solicitado: {self.monto}"
                    
class perfil:
    def __init__(self, nombre, profesion, edad):
        self.nombre: str = nombre
        self.profesion: str = profesion
        self.edad: int = edad
        self.cantidad: int = 0
        self.saldo_pagado: int = 0
        self.cuotas: int = 0
        self.cuotainicial: int = 0
        self.fecha_ultimacuota = 0
    
    def cuota_inicial(self, tipo_prestamo, cant_cuotas):
        self.cuotas += 1
        resultado = self.cantidad * 0.3
        if tipo_prestamo == 1:
            resultado += self.cantidad*0.05
            self.cuotainicial= resultado
            print( "El total de tu cuota inicial es:", resultado)
            capital= int(input("ingrese la cantidad de capital que va a depositar\n"))
            self.saldo_pagado += capital

        else:
            resultado += self.cantidad * 0.03
            self.cuotainicial= resultado
            print( "El total de tu cuota inicial es:", resultado)
        capital= int(input("ingrese la cantidad de capital que va a depositar\n"))
        self.saldo_pagado += capital

    
    def cuota_corriente(self, cant_cuotas, tipo_prestamo)-> int:
        capital= int(input("ingrese la cantidad de capital que va a depositar\n"))
        self.saldo += capital
        self.cuotas += 1
        resultado = self.cantidad - self.cuotainicial
        resultado = resultado / cant_cuotas
        if tipo_prestamo == 1:
            resultado += self.cantidad * 0.05
            return resultado
            
        else:
            resultado += self.cantidad * 0.03
            return resultado

def prestamo_finalizado(perfil) -> bool:
    if perfil.cantidad == perfil.saldo_pagado:
        return False
    else:
        return True
    
class propietario:
    def __init__(self):
        self.usuario : str = "f834ur834u9843uj"
        self.saldo : int = 0
        
    def curriculum(self,perfiles):
        if input("Desea saber el curriulum de todos sus clientes? s/n\n") == "s":
            for i in perfiles:
                print(i)
    def recarga(self):
        incremento = int(input("Cuanto desea recargar en su saldo"))
        self.saldo += incremento
    def notificacion(self, lista:list, lista2: list)-> bool:
        if len(lista) > 0:
            print("Tiene nuevos aspitrantes a prestamos")
            for i in lista:
                print(i)
                elecccion = input("Desea conceder el prestamo? s/n\n")
                if elecccion == "s":
                    lista2.append(i)                                        
                    return True                
                else:                                        
                    return False
                
                
def obtener_fecha_actual():
    fecha_actual = datetime.date.today()
    return fecha_actual

def intereses_mora(perfil):
    mora = perfil.cuota_corriente(cant_cuotas, tipo_prestamo)
    mora = mora + 0.01
    
    print("usted ha pagado menos de lo acordado, se han subito los intereses un 0.01% ")
        
     
clientes= []
perfiles= []
ofreciminetos = []
    
    
    
print("""
██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████       █████      ██ ███    ██ ██    ██ ███████ ██████  ███████ ██  ██████  ███    ██ ███████ ███████     ███████ ██      
██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██     ██   ██     ██ ████   ██ ██    ██ ██      ██   ██ ██      ██ ██    ██ ████   ██ ██      ██          ██      ██      
██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██     ███████     ██ ██ ██  ██ ██    ██ █████   ██████  ███████ ██ ██    ██ ██ ██  ██ █████   ███████     ███████ ██      
██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██     ██   ██     ██ ██  ██ ██  ██  ██  ██      ██   ██      ██ ██ ██    ██ ██  ██ ██ ██           ██          ██ ██      
██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████      ██   ██     ██ ██   ████   ████   ███████ ██   ██ ███████ ██  ██████  ██   ████ ███████ ███████     ███████ ███████ 
                                                                                                                                                                                                    
                                                                                                                                                                                                    
""")
fin = False
while not fin:
    jefe = propietario()
    validacion = False
    persona = input("ingrese nombre de usuario\n")
    if persona== "f834ur834u9843ujo":
        validacion = jefe.notificacion(ofreciminetos, clientes)
        if input("desea saber el curriculum de todos sus clientes s/n?") == "s":
            jefe.curriculum(perfiles)
        if input("Desea recarcar efectivo en su cuenta s/n?") == "s":
            jefe.recarga()
    else:              
        opciones= input("presione '1' si desesa un prestamo,presione '2' si desea realizar el pago de una cuota \n")
        if opciones != "1" and opciones != "2":
            print("ingrese numero valido ")
        
        if opciones == "1":
            if persona in clientes and validacion:
                print("Usted ya tiene un prestamo vigente")
            else:
                prestamo_valido = False
                while not prestamo_valido:
                    cantidad = int(input("cuanta cantidad desea realizar\n"))
                    if cantidad <= 4000000:
                        print("Debe realizar prestamos por enima de 4 millones")
                    else:
                        prestamo_valido = True
                nuevo_usuario.monto = cantidad
                if persona not in clientes:
                    clientes.append(persona)
                    persona1 = clientes.index(persona)
                    persona1 = nuevo_usuario()
                    persona1.monto = cantidad
                    persona1.informacion()                
                    ofreciminetos.append(persona1)
                    print("Su informacion ha sido enviada")
                if validacion:                    
                    persona1.cantidad = cantidad
                    if cantidad >= 4000000 and cantidad <= 55000000:
                        tipo_prestamo = 1                
                    else:
                        tipo_prestamo = 2                
                else:
                    print("su prestamo esta en revision")
                
        elif opciones == "2":
            if persona not in clientes:
                print("Usted es un usuario nuevo, no tiene prestamos vijentes")
                clientes.append(persona)
                persona1 = clientes.index(persona)
                persona1 = nuevo_usuario()
                ofreciminetos.append(persona1)
                persona1.informacion()
                print("Su informacion ha sido enviada")
            
            elif validacion:
                print("su prestamo ha sido validado")
                cliente1 = perfil(persona1.nombre, persona1.profesion, persona1.edad,)
                cliente1.cantidad = persona1.monto
                perfiles.append(cliente1)
                if cliente1.cantidad == 0:
                    print("usted no tiene prestamos vijentes")
                else:
                    cant_cuotas = int(input("A cuantas cuotas desea pagar su prestamo?\n"))
                    if cliente1.cuotas == 0:
                        print("Debe de realizar el pago de la cuota inicial")
                        print("recuerde que la cuota inicial debe ser el 30% del prestamo mas los intereses")
                        cliente1.cuota_inicial(tipo_prestamo, cant_cuotas)
                        cliente1.fecha_ultimacuota = obtener_fecha_actual()
                    else:                    
                        cliente1.cuota_corriente(cant_cuotas, tipo_prestamo)
                        cliente1.fecha_ultimacuota = obtener_fecha_actual()
        
            elif not validacion:
                print("su prestamo esta en revision")
            
        
            if not prestamo_finalizado(cliente1):        
                print("Su deuda ha sido pagada")
        




    
