class TreeNode:
    def __init__(self, name: str = None, hours: float = None, salary: float = None, subject: str = None, rating: float = None, left = None, right = None):
        self.data = {
            "name" : name,
            "hours" : hours,
            "salary" : salary,
            "subject" : subject,
            "rating" : rating
        }

        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self, teacher_node = None):
        self.root = teacher_node


    def insert(self, teacher_node):
        if self.root is None:
            self.root = teacher_node
            return

        current = self.root
        while True:
            if teacher_node.data['hours'] < current.data['hours']:
                if current.left is None:
                    current.left = teacher_node
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = teacher_node
                    return
                current = current.right

    def find_teacher_by_subject(self, subject):
        teachers = []
        self._find_teacher_by_subject_recursive(self.root, subject, teachers)
        return teachers

    def _find_teacher_by_subject_recursive(self, node, subject, teachers):
        if node is not None:
            self._find_teacher_by_subject_recursive(node.left, subject, teachers)

            if node.data['subject'] == subject:
                teachers.append(node.data)

            self._find_teacher_by_subject_recursive(node.right, subject, teachers)

# Метод для поиска преподавателя с максимальным количеством часов
    def find_teacher_with_max_hours(self):
        if self.root is None:
            return None

        return self._find_teacher_with_max_hours_recursive(self.root)

    def _find_teacher_with_max_hours_recursive(self, node):
        if node is None:
            return None

        # Ищем преподавателя с максимальными часами в левом и правом поддереве
        left_max = self._find_teacher_with_max_hours_recursive(node.left)
        right_max = self._find_teacher_with_max_hours_recursive(node.right)

        # Сравниваем текущий узел с максимальными часами из левого и правого поддеревьев
        max_teacher = node
        if left_max and left_max.data['hours'] > max_teacher.data['hours']:
            max_teacher = left_max
        if right_max and right_max.data['hours'] > max_teacher.data['hours']:
            max_teacher = right_max

        return max_teacher

# Метод для поиска преподавателя с минимальным количеством часов
    def find_teacher_with_min_hours(self):
        if self.root is None:
            return None

        return self._find_teacher_with_min_hours_recursive(self.root)

# Рекурсивная функция для нахождения преподавателя с минимальным количеством часов
    def _find_teacher_with_min_hours_recursive(self, node):
        if node is None:
            return None

        # Ищем преподавателя с минимальными часами в левом и правом поддереве
        left_min = self._find_teacher_with_min_hours_recursive(node.left)
        right_min = self._find_teacher_with_min_hours_recursive(node.right)

        # Сравниваем текущий узел с минимальными часами из левого и правого поддеревьев
        min_teacher = node
        if left_min and left_min.data['hours'] < min_teacher.data['hours']:
            min_teacher = left_min
        if right_min and right_min.data['hours'] < min_teacher.data['hours']:
            min_teacher = right_min

        return min_teacher

# Метод для вычисления средней зарплаты преподавателей
    def calculate_average_salary(self):
        total_salary, total_teachers = self._calculate_salary_and_count(self.root)
        if total_teachers == 0:
            return 0
        return total_salary / total_teachers
    
# Рекурсивная функция для подсчета общей суммы зарплат и количества преподавателей
    def _calculate_salary_and_count(self, node):
        if node is None:
            return 0, 0

        # Получаем сумму зарплат и количество преподавателей для левого и правого поддеревьев
        left_salary, left_count = self._calculate_salary_and_count(node.left)
        right_salary, right_count = self._calculate_salary_and_count(node.right)

        # Суммируем все зарплаты и количество преподавателей
        total_salary = left_salary + right_salary + node.data['salary']
        total_teachers = left_count + right_count + 1

        return total_salary, total_teachers

# Метод для поиска преподавателя с наивысшей оценкой
    def find_teacher_with_highest_rating(self):
        if self.root is None:
            return None

        return self._find_teacher_with_highest_rating_recursive(self.root)

# Рекурсивная функция для нахождения преподавателя с наивысшей оценкой
    def _find_teacher_with_highest_rating_recursive(self, node):
        if node is None:
            return None

        # Ищем преподавателя с наивысшей оценкой в левом и правом поддеревьях
        left_highest = self._find_teacher_with_highest_rating_recursive(node.left)
        right_highest = self._find_teacher_with_highest_rating_recursive(node.right)

        # Сравниваем текущий узел с наивысшей оценкой из левого и правого поддеревьев
        highest_rating_teacher = node
        if left_highest and left_highest.data['rating'] > highest_rating_teacher.data['rating']:
            highest_rating_teacher = left_highest
        if right_highest and right_highest.data['rating'] > highest_rating_teacher.data['rating']:
            highest_rating_teacher = right_highest

        return highest_rating_teacher

# Метод для поиска преподавателя с наименьшей оценкой
    def find_teacher_with_lowest_rating(self):
        if self.root is None:
            return None

        return self._find_teacher_with_lowest_rating_recursive(self.root)

# Рекурсивная функция для нахождения преподавателя с наименьшей оценкой
    def _find_teacher_with_lowest_rating_recursive(self, node):
        if node is None:
            return None

        # Ищем преподавателя с наименьшей оценкой в левом и правом поддеревьях
        left_lowest = self._find_teacher_with_lowest_rating_recursive(node.left)
        right_lowest = self._find_teacher_with_lowest_rating_recursive(node.right)

        # Сравниваем текущий узел с наименьшей оценкой из левого и правого поддеревьев
        lowest_rating_teacher = node
        if left_lowest and left_lowest.data['rating'] < lowest_rating_teacher.data['rating']:
            lowest_rating_teacher = left_lowest
        if right_lowest and right_lowest.data['rating'] < lowest_rating_teacher.data['rating']:
            lowest_rating_teacher = right_lowest

        return lowest_rating_teacher        

# Метод для подсчета количества преподавателей с рейтингом выше заданного значения
    def count_teachers_with_rating_above(self, rating_threshold):
        return self._count_teachers_with_rating_above_recursive(self.root, rating_threshold)

# Рекурсивная функция для подсчета преподавателей с рейтингом выше заданного значения
    def _count_teachers_with_rating_above_recursive(self, node, rating_threshold):
        if node is None:
            return 0
        
        count = 0
        # Проверяем, если рейтинг преподавателя выше порогового значения
        if node.data['rating'] > rating_threshold:
            count = 1
        
        # Рекурсивно проверяем левое и правое поддеревья
        count += self._count_teachers_with_rating_above_recursive(node.left, rating_threshold)
        count += self._count_teachers_with_rating_above_recursive(node.right, rating_threshold)
        
        return count

# Метод для подсчета общего числа преподавателей
    def count_total_teachers(self):
        return self._count_total_teachers_recursive(self.root)

# Рекурсивная функция для подсчета преподавателей
    def _count_total_teachers_recursive(self, node):
        if node is None:
            return 0  

        left_count = self._count_total_teachers_recursive(node.left)
        right_count = self._count_total_teachers_recursive(node.right)

        # Суммируем все преподавателей
        return left_count + right_count + 1  # 1 для текущего узла

    def find_teachers_with_salary_above(self, salary_threshold):
        teachers = []
        self._find_teachers_with_salary_above_recursive(self.root, salary_threshold, teachers)
        return teachers
    
# Рекурсивная функция для поиска преподавателей с зарплатой выше заданного значения
    def _find_teachers_with_salary_above_recursive(self, node, salary_threshold, teachers):
        if node is not None:
            # Проверяем, если зарплата преподавателя выше порогового значения
            if node.data['salary'] > salary_threshold:
                teachers.append(node.data)

            # Рекурсивно проверяем левое и правое поддеревья
            self._find_teachers_with_salary_above_recursive(node.left, salary_threshold, teachers)
            self._find_teachers_with_salary_above_recursive(node.right, salary_threshold, teachers)

 # Метод для обхода дерева в порядке in-order (по количеству часов)
    def in_order_traversal(self):
        teachers = []
        self._in_order_traversal_recursive(self.root, teachers)
        return teachers

# Рекурсивная функция для обхода в порядке in-order
    def _in_order_traversal_recursive(self, node, teachers):
        if node is None:
            return

        # Сначала обрабатываем левое поддерево
        self._in_order_traversal_recursive(node.left, teachers)

        # Обрабатываем текущий узел (добавляем преподавателя в список)
        teachers.append(node.data)

        # Затем обрабатываем правое поддерево
        self._in_order_traversal_recursive(node.right, teachers)




teacher1 = TreeNode("John Doe", 120, 3000, "Mathematics", 4.5)
teacher2 = TreeNode("Jane Doe", 80, 2500, "Physics", 4.7)
teacher3 = TreeNode("Alice Smith", 150, 3500, "Chemistry", 4.8)

tree = BinaryTree()

tree.insert(teacher1)
tree.insert(teacher2)
tree.insert(teacher3)


################################################################
subject_to_find = "Physics"
found_teachers = tree.find_teacher_by_subject(subject_to_find)


if found_teachers:
    for teacher in found_teachers:
        print(f"Name: {teacher['name']}, Subject: {teacher['subject']}, Hours: {teacher['hours']}, Salary: {teacher['salary']}, Rating: {teacher['rating']}")
else:
    print(f"No teachers found for subject: {subject_to_find}")

################################

# Ищем преподавателя с максимальным количеством часов
max_teacher = tree.find_teacher_with_max_hours()

# Печатаем найденного преподавателя
if max_teacher:
    print(f"Teacher with maximum hours: Name: {max_teacher.data['name']}, Hours: {max_teacher.data['hours']}, Subject: {max_teacher.data['subject']}, Salary: {max_teacher.data['salary']}, Rating: {max_teacher.data['rating']}")
else:
    print("No teachers found.")

################################

# Ищем преподавателя с минимальным количеством часов
min_teacher = tree.find_teacher_with_min_hours()

# Печатаем найденного преподавателя
if min_teacher:
    print(f"Teacher with minimum hours: Name: {min_teacher.data['name']}, Hours: {min_teacher.data['hours']}, Subject: {min_teacher.data['subject']}, Salary: {min_teacher.data['salary']}, Rating: {min_teacher.data['rating']}")
else:
    print("No teachers found.")

################################

# Вычисляем среднюю зарплату
average_salary = tree.calculate_average_salary()

# Печатаем среднюю зарплату
print(f"Average salary of all teachers: {average_salary:.2f}")

################################################################

# Ищем преподавателя с наивысшей оценкой
highest_rating_teacher = tree.find_teacher_with_highest_rating()

# Печатаем преподавателя с наивысшей оценкой
if highest_rating_teacher:
    print(f"Teacher with highest rating: Name: {highest_rating_teacher.data['name']}, Rating: {highest_rating_teacher.data['rating']}, Subject: {highest_rating_teacher.data['subject']}, Salary: {highest_rating_teacher.data['salary']}, Hours: {highest_rating_teacher.data['hours']}")
else:
    print("No teachers found.")

################################

# Поиск преподавателя с наименьшей оценкой
lowest_rating_teacher = tree.find_teacher_with_lowest_rating()

if lowest_rating_teacher:
    print(f"Teacher with lowest rating: Name: {lowest_rating_teacher.data['name']}, Rating: {lowest_rating_teacher.data['rating']}, Subject: {lowest_rating_teacher.data['subject']}, Salary: {lowest_rating_teacher.data['salary']}, Hours: {lowest_rating_teacher.data['hours']}")
else:
    print("No teachers found.")


################################################################

# Подсчет преподавателей с рейтингом выше 4.6
rating_threshold = 4.6
count = tree.count_teachers_with_rating_above(rating_threshold)

print(f"Number of teachers with rating above {rating_threshold}: {count}")

################################################################

# Подсчет общего числа преподавателей
total_teachers = tree.count_total_teachers()

print(f"Total number of teachers in the tree: {total_teachers}")

################################################################
# Заданный порог зарплаты
salary_threshold = 3000

# Находим преподавателей с зарплатой выше порогового значения
teachers_above_threshold = tree.find_teachers_with_salary_above(salary_threshold)

if teachers_above_threshold:
    for teacher in teachers_above_threshold:
        print(f"Name: {teacher['name']}, Subject: {teacher['subject']}, Salary: {teacher['salary']}, Rating: {teacher['rating']}")
else:
    print(f"No teachers found with salary above {salary_threshold}")

################################
# Выполняем обход in-order и выводим отсортированных преподавателей по количеству часов
sorted_teachers = tree.in_order_traversal()
for teacher in sorted_teachers:
    print(f"Name: {teacher['name']}, Hours: {teacher['hours']}, Subject: {teacher['subject']}, Salary: {teacher['salary']}, Rating: {teacher['rating']}")