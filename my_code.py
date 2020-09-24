# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# none

def avg(user_list):
    average = sum(user_list) / len(user_list)
    return average
        


if __name__ == '__main__':
    list = []
    num = 0
    while num != 'done':
        num = input("Enter a number, if done, type 'done': ")
        if num == 'done':
            break
        list.append(int(num))

    print(avg(list))