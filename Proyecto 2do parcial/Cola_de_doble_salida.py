class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data
        

class DoubleEndedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def insert_front(self, data):
        new_node = Node(data)
        
        if not self.front:
            self.front = new_node
            self.rear = new_node
        
        else:
            self.front.prev = new_node
            new_node.next = self.front
            self.front = new_node              
        
    
    def insert_rear(self, data):
        new_node = Node(data)
        
        if not self.rear:
            self.front = new_node
            self.rear = new_node
        
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    
    def remove_front(self):
        if not self.front:  # La cola está vacía
            raise IndexError("remove_front from empty queue")
        
        current = self.front
        if self.front == self.rear:  # Solo hay un elemento
            self.front = None
            self.rear = None
        else:
            self.front = current.next
            self.front.prev = None
        
        return current.data

    
    
    def remove_rear(self):
        if not self.rear:  # La cola está vacía
            raise IndexError("remove_rear from empty queue")
        
        current = self.rear
        if self.front == self.rear:  # Solo hay un elemento
            self.front = None
            self.rear = None
        else:
            self.rear = current.prev
            self.rear.next = None
        
        return current.data

    
    
    def get_front(self):
        return self.front.data
    
    
    def get_rear(self):
        return self.rear.data
    
    
    def size(self):
        current = self.front
        size = 0
        
        while current:
            size += 1
            current = current.next
            
        return size
    
    
    def printr(self):
        current = self.front
        
        while current:
            print(current.data, end=", ")
            current = current.next
            
            
    def get_element(self, element):
        current = self.front
        
        while current:
            if current.data == element:
                break
            current = current.next
        
        self.front.data, current.data = current.data, self.front.data
        
        data = self.remove_front()
        return data
        
    
    
    def __iter__(self):
        datos = []
        current = self.front
        
        while current:
            datos.append(current.data)
            current = current.next
        
        return iter(datos)