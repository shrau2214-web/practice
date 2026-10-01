# Validating emails and http urls
from pydantic import EmailStr, AnyUrl, BaseModel

class Emp(BaseModel):
    name: str
    email: EmailStr
    LinkedIn: AnyUrl

def display_emp_info(e: Emp):
    print('name:',e.name)
    print('email:',e.email)
    print('LinkedIn:',e.LinkedIn)

data={'name':'abc','email':'abc@gmail.com','LinkedIn':'https://www.linkedin.com/in/yaminirangan/'}
e=Emp(**data)
display_emp_info(e)

# field validator:is a decorator to validate a field manually
# field validators work in two modes : before and after
# before mode works on data before type conversion takes place
# after mode works on data after type conversion.

# Email validation
from pydantic import BaseModel, EmailStr, field_validator, validate_email
class Emp(BaseModel):
    name: str
    email: EmailStr

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['microsoft.com', 'google.com', 'gmail.com']

        # extract domain name after @
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Invalid email address')
        return value

    # Converting name into uppercase
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        value=value.upper()
        return value

def display_info(e1: Emp):
    print('name:',e1.name)
    print('email:',e1.email)

data = {'name': 'abc', 'email': 'abc12345@gmail.com'}
e1 = Emp(**data)
display_info(e1)

