# 1. Why Pydantic?
Imagine you want to check the types used in your code, and validate them, and not only that but you also want to check the data which is being passed into the database is either correct or not. How can you do this? One Option is the vanilla `Python` language.
```python
def add_result(name, marks):
    if type(name) != str:
        raise TypeError("Name must be string")
    if type(marks) != int:
        raise TypeError("Marks must be an integer")
    if marks < 0:
        raise ValidationError("Marks must be greater than or equal to 0")
    print(f"Student name is {name}")
    print(f"{name} got {marks}")
    print("Added into database")
```
Now, Imagine there are Hundreds or Thousands of attributes or fields, so would you use the same approach as above? To solve this comes the `Pydantic`.

Pydantic Provides you the Type Validation, and also the data validation.
Now See the above approach handled using Pydantic.

# 2. First Pydantic Schema

## 2.1 Installation
First you should have python installed in your environment and then just type the below command
```bash
pip install pydantic
```
## 2.2 Basic Schema Code
### 2.2.1 TypeValidation
```python
from pydantic import BaseModel

class Result(BaseModel):
    name: str
    marks: int

result = {'name': 'Muhammad', 'marks': 'ninety'}
result1 = Result(**result)
    
def add_result(result: Result):
    if result.marks < 0:
        raise ValueError("Marks must be greater than or equal to 0")
    print(f"Student name is {result.name}")
    print(f"{result.name} got {result.marks}")
    print("Added into database")

add_result(result1)
```

### Output
```bash
pydantic_core._pydantic_core.ValidationError: 1 validation error for Result
marks
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='ninety', input_type=str]
    For further information visit https://errors.pydantic.dev/2.12/v/int_parsing

```
Notice how `Pydantic` automatically handles all the TypeValidation. If you want to use another function that uses the same attributes you can use it without worrying about the TypeValidation.

### 2.2.2 Multiple Functions
```python
from pydantic import BaseModel

class Result(BaseModel):
    name: str
    marks: int

result = {'name': 'Muhammad', 'marks': 90}
result1 = Result(**result)
    
def add_result(result: Result):
    if result.marks < 0:
        raise ValueError("Marks must be greater than or equal to 0")
    print(f"Student name is {result.name}")
    print(f"{result.name} got {result.marks}")
    print("Added into database")

add_result(result1)

def update_result(result: Result):
    if result.marks < 0:
        raise ValueError("Marks must be greater than or equal to 0")
    print(f"Student name is {result.name}")
    print(f"{result.name} got updated marks:  {result.marks}")
    print("Updated into database")

new_result = {'name': 'Muhammad', 'marks': 91}
result2 = Result(**new_result)

update_result(result2)
```
### Output
```bash
Student name is Muhammad
Muhammad got 90
Added into database
Student name is Muhammad
Muhammad got updated marks:  91
Updated into database
```
### 2.2.3 Data Validation
In Pydantic you can perform its built-in validation or you can use your custom one.

For e.g. If you want to validate email, instead of writing so many conditions you can just use Pydantic `EmailStr`.
```python
from pydantic import BaseModel, EmailStr

class Result(BaseModel):
    name: str
    marks: int
    email: EmailStr

result = {'name': 'Muhammad', 'marks': 90, 'email': "abccom"}
result1 = Result(**result)
    
def add_result(result: Result):
    if result.marks < 0:
        raise ValueError("Marks must be greater than or equal to 0")
    print(f"Student name is {result.name}")
    print(f"Student's email is {result.email}")
    print(f"{result.name} got {result.marks}")
    print("Added into database")

add_result(result1)

def update_result(result: Result):
    if result.marks < 0:
        raise ValueError("Marks must be greater than or equal to 0")
    print(f"Student name is {result.name}")
    print(f"{result.name} got updated marks:  {result.marks}")
    print("Updated into database")
```
### Output
```bash
pydantic_core._pydantic_core.ValidationError: 1 validation error for Result
email
  value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='abccom', input_type=str]
```
You can also use custom validation
```python
from pydantic import BaseModel, EmailStr, Field

class Result(BaseModel):
    name: str
    marks: int = Field(gt=0, le=100)
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
```
### Output
```bash
pydantic_core._pydantic_core.ValidationError: 1 validation error for Result
marks
  Input should be less than or equal to 101 [type=less_than_equal, input_value=102, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/less_than_equal
```