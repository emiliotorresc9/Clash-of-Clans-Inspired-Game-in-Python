class Node:
    def __init__(self, priority, data):
        # Inicializa el nodo con prioridad, datos, y punteros a hijos y padre
        self.priority = priority
        self.data = data
        self.left = None
        self.rigth = None
        self.parent = None
        
        
class Heap:
    def __init__(self):
        # Inicializa el heap con raíz vacía y tamaño 0
        self.__root = None
        self.__size = 0
        
    def is_empty(self):
        # Verifica si el heap está vacío
        return True if self.__size == 0 else False
    
    def get_size(self):
        # Devuelve el tamaño del heap
        return self.__size
    
    def get_root(self):
        # Devuelve la raíz del heap
        return None if not self.__root else self.__root
    
    def print_heap(self):
        # Imprime el heap a partir de la raíz
        self.__printt(self.__root, 0)
        
    def enqueue(self, priority, data):
        # Agrega un nuevo nodo al heap
        new_node = Node(priority, data)
        
        if not self.__root:
            # Si el heap está vacío, el nuevo nodo se convierte en la raíz
            self.__root = new_node
        else:
            # Inserta el nodo en la última posición y ajusta su posición
            self.__insert_node(new_node)
            self.__bubble_up(new_node)
        self.__size += 1
        
    def dequeue(self):
        # Elimina el nodo con la mayor prioridad (raíz) y ajusta el heap
        if not self.__root:
            raise IndexError("Dequeue from empty queue")
        
        max_node = self.__root
        priority, data = max_node.priority, max_node.data
        
        if self.__size == 1:
            # Si hay un solo nodo, el heap queda vacío
            self.__root = None
        else:
            # Intercambia la raíz con el último nodo y lo elimina
            last_node = self.__find_last_node()
            self.__swap(max_node, last_node)
            self.__remove_last_node()
            self.__bubble_down(self.__root)
        
        self.__size -= 1
        return priority, data
    
    def change_priority(self, priority, data, new_priority):
        # Cambia la prioridad de un nodo específico
        node = self.__find_node(self.__root, priority, data)
        
        if node is None:
            raise Exception(f"No se encontró el nodo con prioridad {priority} y datos {data}")
        
        node.priority = new_priority
        # Ajusta el heap después de cambiar la prioridad
        self.__rearrange(node)

    def remove(self, priority, data):
        # Elimina un nodo con la prioridad y datos especificados
        node_to_remove = self.__find_node(self.__root, priority, data)
        
        if node_to_remove is None:
            raise Exception(f"No se encontró el nodo con prioridad {priority} y datos {data}")
        
        if self.__size == 1:
            # Si es el último nodo, simplemente lo quitamos
            self.__root = None
            self.__size -= 1
            return
        
        # Intercambia el nodo a eliminar con el último nodo
        last_node = self.__find_last_node()
        self.__swap(node_to_remove, last_node)
        self.__remove_last_node()
        self.__size -= 1
        
        # Reorganiza el heap para mantener la propiedad
        self.__rearrange(node_to_remove)
        
    def toss(self, datas):
        # Inserta varios nodos al heap a partir de una lista de tuplas (prioridad, datos)
        nodes = []
        
        for i in range(len(datas)):
            priority, data = datas[i]
            new_node = Node(priority, data)
            nodes.append(new_node)
        
        if not self.__root:
            # Si el heap está vacío, el primer nodo es la raíz
            self.__root = nodes[0]
            self.__size += 1
            
            for i in range(1, len(nodes)):
                self.__insert_node(nodes[i])
                self.__size += 1
        else:
            for i in range(len(nodes)):
                self.__insert_node(nodes[i])
                self.__size += 1
        
        self.convert_to_max_heap()
    
    def convert_to_min_heap(self):
        # Convierte el heap en un min-heap reorganizando los nodos
        nodes = self.__get_all_nodes(self.__root)
        
        for i in range(3):
            for node in reversed(nodes):
                self.__rearrange_2(node, True)
        
    def convert_to_max_heap(self):
        # Convierte el heap en un max-heap reorganizando los nodos
        nodes = self.__get_all_nodes(self.__root)
        
        for i in range(3):
            for node in reversed(nodes):
                self.__rearrange_2(node)
    
    def print_top_k(self, k):
        # Imprime los primeros 'k' elementos con mayor prioridad
        if self.is_empty():
            raise Exception("Empty Heap")
            
        if k > self.__size:
            print(f"El valor k es mayor que el tamaño del heap. Mostrando los {self.__size} elementos en su lugar.")
            k = self.__size
        
        temp_heap = Heap()
        nodes = self.__get_all_nodes(self.__root)
        for node in nodes:
            temp_heap.enqueue(node.priority, node.data)
        
        temp_heap_2 = Heap()
        for i in range(k):
            priority, data = temp_heap.dequeue()
            temp_heap_2.enqueue(priority, data)
        
        temp_heap_2.print_heap()
    
    def __get_all_nodes(self, node):
        # Devuelve una lista con todos los nodos del heap usando recorrido in-order
        nodes = []
        
        if node:
            nodes.extend(self.__get_all_nodes(node.left))
            nodes.append(node)
            nodes.extend(self.__get_all_nodes(node.rigth))
            
        return nodes
    
    def __rearrange(self, node):
        # Reorganiza el nodo en el heap, ya sea hacia arriba o hacia abajo
        if not node.left and not node.rigth:
            return
        
        if node.parent and node.priority > node.parent.priority:
            self.__bubble_up(node)
        else:
            self.__bubble_down(node)
    
    def __rearrange_2(self, node, order=False):
        # Reorganiza el nodo dependiendo si es un max-heap o min-heap
        if not node.left and not node.rigth:
            return
    
        if not order:
            self.__bubble_down_max_heap(node)
        else:
            self.__bubble_down_min_heap(node)
    
    def __bubble_up_min_heap(self, node):
        # Ajusta la posición del nodo hacia arriba en un min-heap
        while node.parent:
            if node.parent.priority > node.priority:
                self.__swap(node.parent, node)
                node = node.parent
            else:
                break
            
    def __bubble_down_min_heap(self, node):
        # Ajusta la posición del nodo hacia abajo en un min-heap
        while node.left:
            smaller_child = node.left
            
            if node.rigth and node.rigth.priority < smaller_child.priority:
                smaller_child = node.rigth
            
            if node.priority > smaller_child.priority:
                self.__swap(node, smaller_child)
                node = smaller_child
            else:
                break
    
    def __bubble_down_max_heap(self, node):
        # Ajusta la posición del nodo hacia abajo en un max-heap
        while node.left:
            larger_child = node.left
            
            if node.rigth and node.rigth.priority > larger_child.priority:
                larger_child = node.rigth
            
            if node.priority < larger_child.priority:
                self.__swap(node, larger_child)
                node = larger_child
            else:
                break
    
    def __find_node(self, node, priority, data):
        # Encuentra un nodo con una prioridad y datos específicos
        if not node:
            return None
        if node.priority == priority and node.data == data:
            return node
        
        found_node = self.__find_node(node.left, priority, data)
        if found_node:
            return found_node
        
        return self.__find_node(node.rigth, priority, data)

    def __insert_node(self, new_node):
        # Inserta un nuevo nodo en la última posición del heap
        path = bin(self.__size + 1)[3:]
        current = self.__root
        parent = None
        
        for direction in path:
            parent = current
            current = current.left if direction == '0' else current.rigth
            
        new_node.parent = parent
        if not parent.left:
            parent.left = new_node
        else:
            parent.rigth = new_node
    
    def __bubble_up(self, node):
        # Ajusta la posición del nodo hacia arriba en un max-heap
        while node.parent:
            if node.parent.priority < node.priority:
                self.__swap(node.parent, node)
                node = node.parent
            else:
                break
    
    def __bubble_down(self, node):
        # Ajusta la posición del nodo hacia abajo en un max-heap
        while node.left:
            bigger_child = node.left
            
            if node.rigth and node.rigth.priority > bigger_child.priority:
                bigger_child = node.rigth
                
            if node.priority < bigger_child.priority:
                self.__swap(node, bigger_child)
                node = bigger_child
            else:
                break
    
    def __find_last_node(self):
        # Encuentra el último nodo en el heap
        path = bin(self.__size)[3:]
        current = self.__root
        
        for direction in path:
            current = current.left if direction == '0' else current.rigth
        
        return current
    
    def __remove_last_node(self):
        # Elimina el último nodo del heap
        path = bin(self.__size)[3:]
        current = self.__root
        parent = None
        
        for direction in path:
            parent = current
            current = current.left if direction == '0' else current.rigth
        
        if parent.left == current:
            parent.left = None
        else:
            parent.rigth = None
    
    def __swap(self, node_1, node_2):
        # Intercambia dos nodos (su prioridad y datos)
        node_1.priority, node_2.priority = node_2.priority, node_1.priority
        node_1.data, node_2.data = node_2.data, node_1.data
    

            
    
    def __printt(self, node, n):
        # Imprime el heap de manera jerárquica
        if node:
            self.__printt(node.left, n+1)
            print("       "*n + f"({node.priority}, {node.data})")
            self.__printt(node.rigth, n+1)
            
    
def mergue_recursivo(heap1, heap2):
    if not heap2.get_root():
        raise Exception("Heap2 is empty")
    recursividad(heap1, heap2, heap2.get_root())

def recursividad(heap, heap2, node):
    if node:
        recursividad(heap, heap2, node.left)
        priority, data = node.priority, node.data
        heap.enqueue(priority, data)
        recursividad(heap, heap2, node.rigth) 
        
def mergue(heap1, heap2):
    # Fusiona heap2 en heap1 de manera iterativa usando una pila para recorrer el árbol.
    current = heap2.get_root()  # Comienza en la raíz de heap2
    stack = []  # Pila para hacer el recorrido
    visited = set()  # Conjunto para marcar los nodos visitados
    
    if current == None:
        raise IndexError("Heap2 is empty")  # Error si heap2 está vacío
        
    visited.add(current)  # Marca la raíz como visitada
    heap1.enqueue(current.priority, current.data)  # Inserta la raíz en heap1
    
    # Recorre el árbol de heap2 usando un bucle.
    while current or stack:
        if current and current.left and current.left not in visited:
            # Si el nodo actual tiene un hijo izquierdo no visitado, lo visita.
            stack.append(current)  # Guarda el nodo actual en la pila
            current = current.left  # Se mueve al hijo izquierdo
            visited.add(current)  # Lo marca como visitado
            heap1.enqueue(current.priority, current.data)  # Lo inserta en heap1
            
        elif current and current.rigth and current.rigth not in visited:
            # Si el nodo actual tiene un hijo derecho no visitado, lo visita.
            current = current.rigth  # Se mueve al hijo derecho
            visited.add(current)  # Lo marca como visitado
            heap1.enqueue(current.priority, current.data)  # Lo inserta en heap1
            
        elif stack:
            # Si no hay más hijos por visitar, regresa al nodo anterior usando la pila.
            current = stack.pop()  # Saca un nodo de la pila
            
        else:
            current = None  # Finaliza el recorrido si ya no hay nodos

def merge_multiple_heaps(heaps):
    for i in range(1, len(heaps)):
        if not heaps[i].get_root():
            raise Exception(f"Heap{i+1} is empty")
        mergue_recursivo(heaps[0], heaps[i])
        
        
def is_valid_heap(node, is_max_heap=True):
    # Si el nodo es None, consideramos que es válido (caso base para hojas)
    if not node:
        return True

    # Comprobamos la propiedad del heap con el hijo izquierdo (si existe)
    if node.left:
        if is_max_heap and node.priority < node.left.priority:
            return False
        if not is_max_heap and node.priority > node.left.priority:
            return False

    # Comprobamos la propiedad del heap con el hijo derecho (si existe)
    if node.rigth:
        if is_max_heap and node.priority < node.rigth.priority:
            return False
        if not is_max_heap and node.priority > node.rigth.priority:
            return False

    # Comprobamos recursivamente los hijos izquierdo y derecho
    return is_valid_heap(node.left, is_max_heap) and is_valid_heap(node.rigth, is_max_heap)
