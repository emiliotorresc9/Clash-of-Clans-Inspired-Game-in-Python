"""
Clases de los personajes y aldea
"""
class Constructor:
    def __init__(self):
        self.cultivar = 5
        self.cazar = 3
        self.minar = 10
        self.talar = 14
        self.atacar = 8
        self.construir = 20
        self.tipo = "Constructor"
        
class Guerrero:
    def __init__(self):
        self.cultivar = 2
        self.cazar = 8
        self.minar = 4
        self.talar = 6
        self.atacar = 12
        self.construir = 4
        self.tipo = "Guerrero"
        
class Soldado(Guerrero):
    def __init__(self):
        self.cultivar = 2
        self.cazar = 8
        self.minar = 4
        self.talar = 6
        self.atacar = 16
        self.construir = 4
        self.tipo = "Soldado"
        
class Jinete(Guerrero):
    def __init__(self):
        self.cultivar = 2
        self.cazar = 8
        self.minar = 4
        self.talar = 6
        self.atacar = 20
        self.construir = 4
        self.tipo = "Jinete"
        
class Minero:
    def __init__(self):
        self.cultivar = 8
        self.cazar = 5
        self.minar = 20
        self.talar = 9
        self.atacar = 8
        self.construir = 6 
        self.tipo = "Minero"
        
class Aldeano:
    def __init__(self):
        self.cultivar = 12
        self.cazar = 12
        self.minar = 12
        self.talar = 12
        self.atacar = 4
        self.construir = 3
        self.tipo = "Aldeano"
        
class Cazador(Aldeano):
    def __init__(self):
        self.cultivar = 12
        self.cazar = 20
        self.minar = 12
        self.talar = 12
        self.atacar = 4
        self.construir = 3
        self.tipo = "Cazador"
        
class Agricultor(Aldeano):
    def __init__(self):
        self.cultivar = 20
        self.cazar = 12
        self.minar = 12
        self.talar = 12
        self.atacar = 4
        self.construir = 3
        self.tipo = "Agricultor"
        
class Talador(Aldeano):
    def __init__(self):
        self.cultivar = 12
        self.cazar = 12
        self.minar = 12
        self.talar = 20
        self.atacar = 4
        self.construir = 3
        self.tipo = "Talador"
        
class Casa:
    def __init__(self):
        self.capacidad = 3
        self.requisito = 20
        self.tipo = "casa"


class Coliseo:
    def __init__(self):
        self.capacidad = 2
        self.requisito = 40
        self.tipo = "coliseo"
        
class Establo:
    def __init__(self):
        self.capacidad = 1
        self.requisito = 60
        self.tipo = "establo"
        
import Cola_de_doble_salida as DEQ
import random
class Aldea:
    def __init__(self):
        self.poblacion = DEQ.DoubleEndedQueue()
        self.construcciones = DEQ.DoubleEndedQueue()
        self.madera = 19#10
        self.piedra = 12#5
        self.oro = 2
        self.frutos = 10
        self.carne = 4
        
        aldeanos = []
        for i in range(5):
            aldeanos.append(Aldeano())
        
        guerreros = []
        for i in range(3):
            guerreros.append(Guerrero())
            
        for aldeano in aldeanos:
            self.poblacion.insert_front(aldeano)
            
        for guerrero in guerreros:
            self.poblacion.insert_rear(guerrero)
            
        self.poblacion.insert_front(Constructor())
        self.construcciones.insert_front(Casa())
            
            
    def elegir_miembros(self, actividad):
        best = self.poblacion.get_front()
        
        for miembro in self.poblacion: #Buscar al miembro mas apropiado
            if getattr(miembro, actividad, None) > getattr(best, actividad, None):            
                best = miembro

        if getattr(best, actividad, None) == getattr(self.poblacion.get_front(), actividad, None):
            return self.poblacion.remove_front()
        
        elif getattr(best, actividad, None) == getattr(self.poblacion.get_rear(), actividad, None):
            return self.poblacion.remove_rear()
        
        else:
            return self.poblacion.get_element(best)  

    def perder_recursos(self, rival):
        recursos = ['madera', 'piedra', 'oro', 'frutos', 'carne']
        
        objetos_saquados = set()
        mi_nivel = self.get_nivel_batalla()
        
        if rival < (mi_nivel // 3):
            perdidas = random.randint(1, 2)
            porcentaje_perdida = 0.3  # 30% de pérdida
            porcentaje_perdida = random.randint(0, 0.3)
        elif rival >= (mi_nivel // 3) and rival < ((mi_nivel // 3)*2):
            perdidas = random.randint(3, 4)
            porcentaje_perdida = 0.6  # 60% de pérdida
        else:
            perdidas = 5
            porcentaje_perdida = 0.9  # 90% de pérdida
        
        for i in range(perdidas):
            objeto = random.choice(recursos)
            if objeto not in objetos_saquados:
                objetos_saquados.add(objeto)
                
                # Obtiene el valor actual del recurso
                valor_actual = getattr(self, objeto)
                
                # Calcula la nueva cantidad, redondeando a enteros
                nueva_cantidad = max(0, int(round(valor_actual * (1 - porcentaje_perdida))))
                
                # Actualiza el valor del recurso
                setattr(self, objeto, nueva_cantidad)
                
                
    def ganar_recursos(self, accion, ganancias):
        if accion == "cultivar":
            self.frutos += ganancias//3
        elif accion == "cazar":
            self.carne += ganancias//3
        elif accion == "minar":
            self.piedra += ganancias//3
            self.oro += ganancias//6
        elif accion == "talar":
            self.madera += ganancias//3
            
            
    def ligar(self, construcciones, op, cuantos):         
        if op == 1:
            if self.frutos >= 10 and self.carne >= 2 and self.oro >= 1:
                print("Se estan ligando un contructor")
                print("Ahora tienes un constructor mas")
                self.frutos -= 10
                self.carne -= 2
                self.oro -= 1
                return [Constructor()]
            return "recursos"
        elif op == 2:
            if self.frutos >= 3*cuantos and self.carne >= 7*cuantos and self.oro >= 2*cuantos and cuantos <= 2:
                print(f"Se estan ligando {cuantos} guerreros")
                miembros = []
                for i in range(cuantos):
                    miembros.append(Guerrero())
                print(f"Ahora tienes {cuantos} guerreros mas")
                self.frutos -= 3*cuantos
                self.carne -= 7*cuantos
                self.oro -= 2*cuantos
                return miembros
            return "recursos"
        elif op == 3:
            si = False
            coliseos = 0
            for edificio in construcciones:
                if getattr(edificio, "tipo") == "coliseo":
                    si = True
                    coliseos += 1
            if si == True:
                if self.frutos >= 5*cuantos and self.carne >= 10*cuantos and self.oro >= 3*cuantos and cuantos <= coliseos*2:
                    print(f"Se estan ligando {cuantos} Soladados")
                    miembros = []
                    for i in range(cuantos):
                        miembros.append(Soldado())
                    print(f"Ahora tienes {cuantos} soldados mas")
                    self.frutos -= 5*cuantos
                    self.carne -= 10*cuantos
                    self.oro -= 3*cuantos
                    return miembros
                return "recursos"
            
            return "Coliseo"
        elif op == 4:
            si = False
            establos = 0
            for edificio in construcciones:
                if getattr(edificio, "tipo") == "establo":
                    si = True
                    establos += 1
            if si == True:
                if self.frutos >= 10*cuantos and self.carne >= 16*cuantos and self.oro >= 4*cuantos and cuantos <= establos:
                    print(f"Se estan ligando {cuantos} Jinetes")
                    miembros = []
                    for i in range(cuantos):
                        miembros.append(Jinete())
                    print(f"Ahora tienes {cuantos} jinetes mas")
                    self.frutos -= 10*cuantos
                    self.carne -= 16*cuantos
                    self.oro -= 4*cuantos
                    return miembros
                return "recursos"
            return "Establo"
        elif op == 5:
            if self.frutos >= 7 and self.carne >= 5 and self.oro >= 0:
                print("Se esta ligando un minero")
                print("Ahora tienes un minero mas")
                self.frutos -= 7
                self.carne -= 5
                self.oro -= 0
                return [Minero()]
            return "recursos"
        elif op == 6:
            si = False
            casas = 0
            for edificio in construcciones:
                if getattr(edificio, "tipo") == "casa":
                    si = True
                    casas += 1
            if self.frutos >= 3*cuantos and self.carne >= 1*cuantos and self.oro >= 0*cuantos and cuantos <= casas*3:
                print(f"Se estan ligando {cuantos} aldeanos")
                miembros = []
                for i in range(cuantos):
                    miembros.append(Aldeano())
                print(f"Ahora tienes {cuantos} aldeanos mas")
                self.frutos -= 3*cuantos
                self.carne -= 1*cuantos
                self.oro -= 0*cuantos
                return miembros
            return "recursos"
        elif op == 7:
            if self.frutos >= 10 and self.carne >= 0 and self.oro >= 1:
                print("Se esta ligando un cazador")
                print("Ahora tienes un cazador mas")
                self.frutos -= 10
                self.carne -= 0
                self.oro -= 1
                return [Cazador()]
            return "recursos"
        elif op == 8:
            if self.frutos >= 0 and self.carne >= 5 and self.oro >= 1:
                print("Se esta ligando un agricultor")
                print("Ahora tienes un agricultor mas")
                self.frutos -= 0
                self.carne -= 5
                self.oro -= 1
                return [Agricultor()]
            return "recursos"
        elif op == 9:
            if self.frutos >= 5 and self.carne >= 5 and self.oro >= 1:
                print("Se esta ligando un talador")
                print("Ahora tienes un talador mas")
                self.frutos -= 5
                self.carne -= 5
                self.oro -= 1
                return [Talador()]
            return "recursos"

        
    def construir(self, poblacion, op): #Modificar
        
        if op == 1:
            if self.madera >= 19 and self.piedra >= 12 and self.oro >= 1:
                miembros = []
                miembros.append("construir")
                miembros.append(Casa())
                nivel = 0
                while nivel < 10:
                    if poblacion == 0:
                        return False
                    miembro = self.elegir_miembros("construir")
                    nivel += getattr(miembro, "construir")
                    poblacion -= 1
                    miembros.append(miembro)
                self.madera -= 19
                self.piedra -= 12
                self.oro -= 1
                return miembros
            return None
        
        elif op == 2:
            if self.madera >= 30 and self.piedra >= 25 and self.oro >= 6:
                miembros = []
                miembros.append("construir")
                miembros.append(Coliseo())
                nivel = 0
                while nivel < 17:
                    if poblacion == 0:
                        return False
                    miembro = self.elegir_miembros("construir")
                    nivel += getattr(miembro, "construir")
                    poblacion -= 1
                    miembros.append(miembro)
                self.madera -= 30
                self.piedra -= 25
                self.oro -= 6
                return miembros
            return None
            
        elif op == 3:
            if self.madera >= 50 and self.piedra >= 40 and self.oro >= 10:
                miembros = []
                miembros.append("construir")
                miembros.append(Establo())
                nivel = 0
                while nivel < 25:
                    if poblacion == 0:
                        return False
                    miembro = self.elegir_miembros("construir")
                    nivel += getattr(miembro, "construir")
                    poblacion -= 1
                    miembros.append(miembro)
                self.madera -= 50
                self.piedra -= 40
                self.oro -= 10
                return miembros
            return None
            
    
    
    def ataque(self, miembros, mi_nivel, rival): #Modificar
        recursos = ['madera', 'piedra', 'oro', 'frutos', 'carne']
        # mi_nivel = 0
        muertes = 0
        # for miembro in miembros:
        #     mi_nivel += getattr(miembro, "atacar", None)
        
        objetos_saquados = set()    
        # rival = random.randint(10, mi_nivel+5)
        
        # print(f"Tu nivel de batalla {mi_nivel}")
        # print(f"Nivl de batalla del rival encontrado {rival}")
        # print();print("Desesas continuar con el ataque?")
        # print("[1] Si")
        # print("[2] No")
        
        # desicion = int(input())
        
        # if desicion == 2:
        #     print("Ataque cancelado, miembros elegidos regresando a la aldea")
        #     return [False, 0]
            # while miembros:
            #     miembro = miembros.pop()
            #     self.poblacion.insert_front(miembro)
            #     return
        
        # if mi_nivel < rival:
        #     return None
            
        
        """Calculo de ganancias y perdidas de miembros"""
        if rival < (mi_nivel // 3):
            ganancias = random.randint(1, 2)
            porcentaje_ganancia = 0.9  # 90% de ganancia
            muertes = random.randint(0, len(miembros)//4)
            
        elif rival >= (mi_nivel // 3) and rival < ((mi_nivel // 3)*2):
            ganancias = random.randint(3, 4)
            porcentaje_ganancia = 0.6  # 60% de ganancia
            muertes = random.randint(0, (len(miembros)//4)*2)
        else:
            ganancias = 5
            porcentaje_ganancia = 0.3  # 30% de ganancia
            muertes = random.randint(0, (len(miembros)//4)*3)
        
        """Obtener ganancias"""
        for i in range(ganancias):
            objeto = random.choice(recursos)
            if objeto not in objetos_saquados:
                objetos_saquados.add(objeto)
                
                # Obtiene el valor actual del recurso
                valor_actual = getattr(self, objeto)
                
                # Calcula la nueva cantidad, redondeando a enteros
                nueva_cantidad = max(0, int(round(valor_actual * (1 + porcentaje_ganancia))))
                
                # Actualiza el valor del recurso
                setattr(self, objeto, nueva_cantidad)
    
    
        """Perder miembros"""
        return muertes
        # while muertes > 0:
        #     miembro = miembros.pop()
        #     self.poblacion.insert_front(miembro)
        #     muertes -= 1
    
    def batalla(self, rival):
        mi_nivel = self.get_nivel_batalla()
        poblacion = self.poblacion.size()
        perdidas = 0
        
        if rival < (mi_nivel / 4):
            # El rival es mucho más débil, permitimos que las pérdidas sean entre 0% y 20% de la población
            perdidas = random.randint(0, int(poblacion * 0.2))
        elif rival >= (mi_nivel / 4) and rival < (mi_nivel / 2):
            # El rival es más débil pero no tanto, eliminamos entre el 20% y el 35% de la población
            perdidas = random.randint(max(1, int(poblacion * 0.2)), max(1, int(poblacion * 0.35)))
        elif rival >= (mi_nivel / 2) and rival < (3 * mi_nivel / 4):
            # El rival es casi igual en fuerza, eliminamos entre el 35% y el 50% de la población
            perdidas = random.randint(max(1, int(poblacion * 0.35)), max(1, int(poblacion * 0.5)))
        elif rival >= (3 * mi_nivel / 4) and rival <= mi_nivel:
            # El rival es ligeramente superior, eliminamos entre el 50% y el 60% de la población
            perdidas = random.randint(max(1, int(poblacion * 0.5)), max(1, int(poblacion * 0.6)))
        elif rival > mi_nivel:
            # El rival es mucho más fuerte, eliminamos entre el 60% y el 90% de la población
            perdidas = random.randint(max(1, int(poblacion * 0.6)), max(1, int(poblacion * 0.9)))
            
        for i in range(perdidas):
            if poblacion == 1: #Asegurarse de al menos quedarse con un miembro de la poblacion
                break
            eliminar = random.randint(1, poblacion)
            miembro_eliminado = self.poblacion.get_front()
            #Con este bucle se elige de manera aleatoria un miembro para eliminarlo
            for i, miembro in enumerate(self.poblacion):
                if i >= eliminar:
                    break
                miembro_eliminado = miembro
            if miembro_eliminado == self.poblacion.get_front():
                self.poblacion.remove_front()
            elif miembro_eliminado == self.poblacion.get_rear():
                self.poblacion.remove_rear()
            else:
                self.poblacion.get_element(miembro_eliminado) #Metodo para eliminar al miembro si no esta en uno de los extremos
            poblacion -= 1
            
    def get_nivel_batalla(self):
        mi_nivel = 0
        for miembro in self.poblacion:
            mi_nivel += getattr(miembro, "atacar")
        return mi_nivel
            
        




if __name__ == "__main__":            
    x = Aldea()
    x.batalla(50)