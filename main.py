from pydantic import BaseModel, EmailStr, Field

class Result(BaseModel):
    name: str
    marks: int = Field(gt=0, le=101)
    email: EmailStr

result = {'name': 'Muhammad', 'marks': 102, 'email': "abc@gmail.com"}
result1 = Result(**result)
    
def add_result(result: Result):
    print(f"Student name is {result.name}")
    print(f"Student's email is {result.email}")
    print(f"{result.name} got {result.marks}")
    print("Added into database")

add_result(result1)

def update_result(result: Result):
    print(f"Student name is {result.name}")
    print(f"{result.name} got updated marks:  {result.marks}")
    print("Updated into database")
    