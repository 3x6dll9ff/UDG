# next = None , prev = None):

class LectionNode:
    def __init__(self, name:str = None, ime_predavaca:str = None, godina_nastanka:int = None, mjesec_nastanka:int = None, 
                 trajanje_minutes:int = None , next = None , prev = None):  
        self.lections = {
            "name": name,
            "ime_predavaca": ime_predavaca,
            "godina_nastanka": godina_nastanka,
            "mjesec_nastanka": mjesec_nastanka,
            "trajanje_minutes": trajanje_minutes,
        }
        self.next = next
        self.prev = prev

class ListLection:
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail


    def add_to_start(self, lection: LectionNode):
        if self.head is None:
            self.head = lection
            self.tail = lection
        else:
            lection.next = self.head
            self.head.prev = lection
            self.head = lection

    def add_to_end(self, lection: LectionNode):
        if self.tail is None:  
            self.head = lection
            self.tail = lection
        else:
            current = self.tail  
            current.next = lection  
            current.prev = current      
            self.tail = lection   


    #NOT WORKING
    def delete_by_name(self, name):
        if self.head is None:
            return 'None'
        else:
            if self.head.lections['name'].lower() == name.lower():
                current = self.head
                self.head = self.head.next
                self.head.prev = None
                current.next = None
            else:
                current = self.head
                prev = None
                while current is None:
                    if current.lections['name'].lower() == name.lower():
                        prev.next = current.next
                        current.next.prev = prev
                        current.next = None
                        current.prev = None
                    prev = current
                    current = current.next


    def print_sort_by_highest_trajanje_minutes(self, time):
        current = self.head
        while current is not None:
            if current.lections['trajanje_minutes'] > time:
                print(current.lections)
            current = current.next
 

    def print_name_with_highest_trajanje_minutes(self):
        current = self.head
        max_minutes = 0
        while current is not None:
            if current.lections['trajanje_minutes'] > max_minutes:
                max_minutes = current.lections['trajanje_minutes']
                max_name = current.lections['name']
                name_prof = current.lections['ime_predavaca']
            current = current.next
        print(f"Najduza je {max_name}  {max_minutes} minutes. Predavac -  {name_prof}")

    def print_parove_lekcija_predavac_start_from_end(self):
        current = self.tail
        while current is not None:
            if current.lections['godina_nastanka'] > 2020:
                print(current.lections)
            current = current.prev
        print("-----:")
        
        
                    
    def print_list(self):
        if self.head is None:
            print("List je prazna!")
        else:
            current = self.head
            while current is not None:
                print(current.lections)
                current = current.next


lection1 = LectionNode(name="matematika", ime_predavaca="Valentina", godina_nastanka=2022, mjesec_nastanka=1, trajanje_minutes=33)
lection2 = LectionNode(name="geodezija", ime_predavaca="Ognijen", godina_nastanka=2020, mjesec_nastanka=4, trajanje_minutes=10)
lection3 = LectionNode(name="elektrotehnika", ime_predavaca="Predrag", godina_nastanka=2023, mjesec_nastanka=2, trajanje_minutes=22)
lection4 = LectionNode(name="programiranje", ime_predavaca="Stevan", godina_nastanka=2019, mjesec_nastanka=5, trajanje_minutes=60)
lection5 = LectionNode(name="filosofija", ime_predavaca="Predrag", godina_nastanka=2019, mjesec_nastanka=3, trajanje_minutes=370)


double_list_lection = ListLection()
double_list_lection.add_to_start(lection1)
double_list_lection.add_to_start(lection2)
double_list_lection.add_to_start(lection3)
double_list_lection.add_to_end(lection4)
double_list_lection.print_list()
print(" ")
double_list_lection.delete_by_name('matematika')
double_list_lection.print_parove_lekcija_predavac_start_from_end()
print(" ")


double_list_lection.print_sort_by_highest_trajanje_minutes(30)
double_list_lection.print_name_with_highest_trajanje_minutes()


