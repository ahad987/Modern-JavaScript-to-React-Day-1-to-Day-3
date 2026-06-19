student_info = {
    'name': 'John Doe',
    'age': 20,
    'major': 'Computer Science',
    'courses': ['Data Structures', 'Algorithms', 'Operating Systems']
}
print(student_info)

print("==================")

print(student_info['name'])
print(student_info['age'])

student_info['age1'] = 50
print(student_info['age1'])

print("==============Access Dictionary KEY ====")
for data in student_info:
    print(data)
print("============Access Dictionary value ======")
for data in student_info:
    print(student_info[data])
    
print("============New ======")

marks = {}
print("Dictionary length:", len(student_info))

del student_info['age1']
print("Dictionary after deletion:", student_info)

print("After POP:", student_info.pop('major'))

print("Dictionary after POP:", student_info)

print(student_info.clear())

print(student_info)

print("============New ======")

my_dict = {
    'name': "Alice",
    'age': 30,
    'address': "123 Main St"
}

print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())
print(my_dict.get('name'))

for data in my_dict.values():
    print(data)
    
for data in my_dict.keys():
    print(data)
    
for key, value in my_dict.items():
    print(key, value)
    
print("============New ======")

my_dict = {
    'name': "Alice",
    'age': 30,
    'address': "123 Main St"
}

list_key = []
list_value = []

for key, value in my_dict.items():
    list_key.append(key)
    list_value.append(value)
    
print("List of keys:", list_key)
print("List of values:", list_value)


print("==================Function===============")

def student_function():
    print("Hello python.")
    
student_function()

def my_function(num1, num2):
    print(num1 + num2)
    
my_function(10, 20)

def fun_defu_pa(num1 = 0, num2 = 0):
    print(num1 + num2)
    
fun_defu_pa(10)