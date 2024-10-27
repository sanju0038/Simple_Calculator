class Calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2
    
    def mod(self):
        return self.num1 % self.num2
    
print("Welcome to SANJU calculator")
print("-------------------------------------")
print(" 1️⃣ .Addition\n 2️⃣ .Subtraction\n 3️⃣ .Multiplication\n 4️⃣ .Division\n 5️⃣ .Modulus")
print("-------------------------------------")
choice=int(input("Enter your choice : "))
choice_list=[1,2,3,4,5]
if choice in choice_list:
    num1=int(input("Enter your first number : "))
    num2=int(input("Enter your second number : "))
    obj=Calculator(num1,num2)

    if choice == 1:
        print(f"The Addition ➕  of {num1} and {num2} is",obj.add())

    elif choice == 2:
        print(f"The Subtraction ➖  of {num1} and {num2} is",obj.sub())

    elif choice == 3:
        print(f"The Multiplication ✖️  of {num1} and {num2} is",obj.mul())

    elif choice == 4:
        print(f"The Division ➗  of {num1} and {num2} is",obj.div())

    elif choice == 5:
        print(f"The Modulus of (%)  {num1} and {num2} is",obj.mod())

else:
    print("You have entered the wrong choice🙌\nPlease select the choice between 1 to 5 !")

print("-------------------------------------")



