import re
import mysql.connector
from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import(connection)
import os
import platform
import json
import logging

logging.basicConfig(filename="Adf_database.txt", filemode='a+',
                        format='%(asctime)s %(levelname)s-%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class userData:
    def __init__(self,first_name,mid_name,last_name, dob, gender,nationality, current_city, state, pincode, qualification, salary, pan):
        self.first_name=first_name
        self.mid_name=mid_name
        self.last_name=last_name
        self.dob=dob
        self.gender=gender
        self.gender=gender
        self.nationality=nationality
        self.current_city=current_city
        self.state=state
        self.pincode=pincode
        self.qualification=qualification
        self.salary=salary
        self.pan=pan
        self.reason=""
        self.result=""

    def validate_firstname(self):
        logging.info("validating first name of the user")
        p=re.compile("[A-Za-z\s]+$")
        if re.search(p,self.first_name):
            return True
        return False

    def validate_lastname(self):
        logging.info("validating last name of the user")
        p = re.compile("[A-Za-z\s]+$")
        if re.search(p, self.last_name):
            return True
        return False

    def calculate_age(self):
        logging.info("calculating the age of the user")
        d,m,y=map(int, self.dob.split('/'))
        n=date(d,m,y)
        total_days= 365.2425
        age=int((date.today()-n).days/total_days)
        return age

    def validate_nation(self):
        logging.info("validating the nation of the user")
        if self.nationality in ['india','america']:
            return True
        return False

    def validate_state(self):
        logging.info("validating the state of the user")
        if self.state.lower() in ["andhra pradesh", "arunachal pradesh", "assam", "bihar", "chhattisgarh", "karnataka", "tamil Nadu",
                                  "telangana","west bengal"]:
            return True
        return False

    def age_and_gender(self):
        logging.info("validating age with respect to the gender")
        age=self.calculate_age()
        if self.gender.lower()=='male' and age>21:
            return True
        elif self.gender.lower()=='female' and age>18:
            return True
        return False

    def validate_pin(self):
        logging.info("validating pincode of the user")
        reg = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
        p=re.compile(reg)
        if  re.search(p,self.pincode) and len(self.pincode)==6:
            return True
        return False

    def validate_salary(self):
        logging.info("validating salary of the user")
        if int(self.salary)>10000 and int(self.salary)<90000:
            return True
        return False

    def validate_pan(self):
        logging.info("validating pan of the user")
        reg = "[A-Za-z]{5}[0-9]{4}[A-Za-z]{1}"
        p = re.compile(reg)
        if re.search(p,self.pan) and len(self.pan)==10:
            return True
        return False

    def validate_result(self):
        ans= True
        if not self.validate_nation():
            self.reason +="Nation is Invalid " + ", "
        if not self.validate_state():
            self.reason +="State is Invalid " + ", "
        if not self.age_and_gender():
            self.reason +="Age is less than expected " + ", "
        if not self.validate_pin():
            self.reason +="pincode is invalid " + ", "
        if not self.validate_salary():
            self.reason +="salary is not as expected " + ", "
        if not self.validate_pan():
            self.reason +="pan number is invalid " + ", "

        if self.reason=="":
            self.result="success"
        else:
            self.result="failure"
            ans=False

        return ans

    def validate_details(self):
        self.validate_firstname()
        self.validate_lastname()
        self.validate_nation()
        self.validate_state()
        self.age_and_gender()
        self.validate_salary()
        self.validate_pin()
        self.validate_pan()
        self.validate_result()

        return True






