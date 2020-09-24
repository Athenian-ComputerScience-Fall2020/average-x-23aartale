# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# none

def avg(user_list):
    average = sum(user_list) / len(user_list)
    return average


if __name__ == '__main__':

    user_list = []

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    num3 = int(input("Enter your third number: "))
    num4 = int(input("Enter your fourth number: "))
    num5 = int(input("Enter your last number: "))

    print(avg([num1, num2, num3, num4, num5]))