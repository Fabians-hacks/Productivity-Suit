
def todo():
    list_of_todo = []

    with open("C:\\Users\\fabi_\\PycharmProjects\\Productivity Suit\\Data\\tasks.txt", "r") as f:

        for task in f:
            list_of_todo.append(task)


        #list_of_todo = [element.strip('\n') for element in list_of_todo]
        string_of_todo = str(list_of_todo)
        for s in string_of_todo:
            if s == "}" or s== "{":
                s.remove()
    return(list_of_todo)

