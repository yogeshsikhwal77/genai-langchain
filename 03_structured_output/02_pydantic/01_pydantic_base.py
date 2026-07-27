from pydantic import BaseModel,EmailStr,Field
from typing import Optional

# class Student(BaseModel):

#     name: str

# new_student = {'name':'yogesh'}   # if i give any other dtype it give error

# student = Student(**new_student)
# print(student)



# -------------------default fields---------------------#
# -------------------optional ---------------------#

class Student(BaseModel):

    name: str = 'yogesh'
    age: Optional[int] = None
    email: EmailStr  # validate email address

    cgpa : float = Field(gt=0,lt=10,default=7,description='decimal value represent the cgpa of the student') # make constrain between float max and min value 

new_student = {'age':'32','email':'yogesh@test.com'}    # it for age define as int but pydantic coerce smart it understand it is int
student = Student(**new_student)

print(student) # name='yogesh' age=32 email='yogesh@test.com' cgpa=7

student_dict = dict(student)

print(student_dict)  # {'name': 'yogesh', 'age': 32, 'email': 'yogesh@test.com', 'cgpa': 7}   

student_json = student.model_dump_json()
