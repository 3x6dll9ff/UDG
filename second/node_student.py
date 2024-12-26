class Student:
    def __init__(self, ime = None, prosjek = None, id = None, razred = None, izostanak = None):
        self.ime = ime
        self.prosjek = prosjek
        self.id = id
        self.razred = razred
        self.izostanak = izostanak

class Node_Student:
    def __init__(self, data: Student, next = None, prev = None,):
        self.data = data
        self.next = next
        self.prev = prev


class Student_List():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def print(self):
        current = self.head
        while current is not None:
            print(f"ID: {current.data.id}, Ime: {current.data.ime}, Prosjek: {current.data.prosjek}, Razred: {current.data.razred}, Izostanak: {current.data.izostanak}")
            current = current.next
        
    def append(self, new_element):
        if not self.head:
            self.head = new_element
            self.tail = new_element
        else:
            self.tail.next = new_element
            new_element.prev = self.tail
            self.tail = new_element

    def prosjek(self):
        current = self.head
        value = 0
        counter = 0
        while current is not None:
            value += current.value["prosjek"]
            counter += 1
            current = current.next
        return value / counter if counter > 0 else 0
    
    def prosjek_veci(self,prosjek):
        current = self.head
        while current is not None:
            if current.data["prosjek"] > prosjek:
                print(f"ID: {current.data['id']}, Ime: {current.data['ime']}, Prosjek: {current.data['prosjek']}, Razred: {current.data['razred']}, Izostanak: {current.data['izostanak']}")
            current = current.next

    def find_by_id(self, id):
        current = self.head
        while current is not None:
            if current.data["id"] == id:
                return current.data
            current = current.next
        return None
    
    def delete_by_id(self, id):
        current = self.head
        while current is not None:
            if current.data["id"] == id:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next 


    def id_set_avg(self,id, new_avg):
            current = self.head
            while current:
                if current.data["id"] == id:
                    current.data["prosjek"] = new_avg
                    return
                current = current.next
            return False
    
    def max_odsudstvo(self):
        current = self.head
        max_odsudstvo = 0
        max_id = None
        while current is not None:
            if current.data["izostanak"] > max_odsudstvo:
                max_odsudstvo = current.data["izostanak"]
                max_id = current.data["id"]
            current = current.next
        return max_id, max_odsudstvo
        
                
