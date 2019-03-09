from linked_list import MyList
from linked_class import Stack
from myclass import Person
from myclass import Student

Student_1 = Student('Anton', 20, 3)
Student_2 = Student('Mariya', 19, 2)
Student_3 = Student('Pavel', 21, 4)
Student_4 = Student('Viktor', 21, 3)  
my_stack = Stack()
my_stack.push(Student_1)
my_stack.push(Student_2)
my_stack.push(Student_3)
my_stack.push(Student_4)
print("Stack Size:", my_stack.length())
st = my_stack.pop(NAME)
print("The result of the pop () method:", st.get_student_name(), st.get_student_age(), st.get_student_course())
print("Stack Size:", my_stack.length())
st = my_stack.peek()
print("The result of the peek() method:", st.get_student_name(), st.get_student_age(), st.get_student_course())
print("Stack Size:", my_stack.length())

st = my_stack.pop()
print("The result of the pop () method:", st.get_student_name(), st.get_student_age(), st.get_student_course())
