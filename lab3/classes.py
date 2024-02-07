#1
class MyString:
    def __init__(self):
        self.input = ""

    def getString(self):
        self.input = input("Enter a string: ")

    def printString(self):
        print(self.input)

#2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

#3
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

#4
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Coordinates: x = {self.x};y = {self.y}")
    
    def move(self,new_x, new_y):
        self.x=new_x
        self.y=new_y
    
    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, sum):
        self.balance += sum
        print(f"Зачислено: {sum}")
        print(f"Баланс: {self.balance}")
    
    def withdraw(self, sum):
        if self.balance - sum < 0:
            print("Ошибка снятия")
        else:
            self.balance -= sum
            print(f"Снято: {sum}")
            print(f"Баланс: {self.balance}")

account1 = Account("Sasha",3000)
account1.deposit(500)
account1.withdraw(3500)
account1.withdraw(100)

#6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
nums = [1,2,3,4,5,6,7,8,9,10]
prime_nums = list(filter(lambda x : is_prime(x), nums))
print(*prime_nums)

