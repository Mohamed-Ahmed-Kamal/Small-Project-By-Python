list = []
while True:
    userAction = input(
        "Enter Your Action ('add' or 'remove' or 'view' or 'exit')!? ")
    if userAction == "add":
        task = input("Enter Your Task => ")
        list.append(task.lower())
        print("Task Add.")
    elif (userAction == "view"):
        if not list:
            print("Nothing To Display :)")
        else:
            for i in list:
                print(i)
    elif (userAction == "remove"):
        if not list:
            print("Nothing To Remove :)")
        else:
            task = input("Enter Your Task To Delete => ").lower()
            if task in list:
                list.remove(task.lower())
                print("Done :)")
            else:
                print("This Commend Not Valied")
    elif (userAction == "exit"):
        break
