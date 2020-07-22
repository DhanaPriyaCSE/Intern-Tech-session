
from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Running in Laptop....")
        
class Desktop(Computer):
    def process(self):
        print("Running in Desktop....")

class Programmer:
    def work(self,com):
        print("coding")
        com.process()

class Employee:
    def get_salary(self):
        print("salary in progress...")

    def status(self,computer):
        computer.process()


lap=Laptop()
desk=Desktop()

programmer=Programmer()
programmer.work(lap)
programmer.work(desk)

#emp=Employee()
#emp.get_salary()
#emp.status(lap)

