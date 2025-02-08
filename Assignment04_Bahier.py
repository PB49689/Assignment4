def add_task(task_list):
   #Create a function that takes in the list of a task
    while True:
        #create a while loop
        task = input("Input a task please, enter f (finished) when you want to stop adding parts to your list ")
        #Ask the user to assign a variable 
        if task == "f":
            #Check to see if the user selects f
            break
        #If it breaks it breaks
        task_list.append(task)
        #Shows all the elements of the array 
        print(task)
        #Prints all the variables to task 

#=================================================================#
def delete(task_list, i):
    #Establish a function called delete task thatt has the parameters of the array and the index of the array
    if 0 <= i < len(task_list):

        #Establishes an if then statement
        removed_task = task_list.pop(i)
        print( removed_task + " is  gone")
        #Establish a print statement that 
    else:
        print(" Try again")
        #Prints a statement try again

#=======================================================#
def sort_tasks(task_list, completed, notcompleted):
    #Establish a function that takes in the three parameters tasK_list, completed, notcompleted.
    for task in task_list[:]:
        #Establishes a for loop that traverses the array 
        choice = input(task + " to Complete (1) or Not Finished (2) ")
        #If the user selects one then the element of the array is completed if the user selects two then array goes to a different  
        if choice == "1":
            #If the user selects one 
            completed.append(task)
            #Then adds to the compelted list 
        elif choice == "2":
            #If the user selects two 
            notcompleted.append(task)
            #Then adds to the not completed list 
        else:
            print("Invalid ")
            #Invalid
    
    task_list.clear()
    #Clears the list 

#======================================================#
def delete_from_list(completed, notcompleted):
# Creates a function that takes in two lists asparameters    
    list_num = int(input("Enter list number (1 or 2) to delete from: "))
    #Enter list number due to each number representing the list
    if list_num == 1:
    #Create an if statement
        selected_list = completed
    #Establish that the seleted_list is part of said list
    elif list_num == 2:
        #Else if 
        selected_list = notcompleted
        #Selected list is not completed
    else:
       #Any other user choice is deleted
        print("Wrong")
        #Prints Wrong
        return

    print(str(list_num) + ":")
    
    for i in range(len(selected_list)):
        #Establish a for loop that traverses the entire list 
        print(str(i) + ": " + selected_list[i])
        #Establish a string th
    i = int(input("Enter the index of the task to delete: "))
    
    if 0 <= i < len(selected_list):
        #Establish an if then statement 
        removed_task = selected_list.pop(i)
        print("Task '" + removed_task + "' removed successfully from List " + str(list_num))
    else:
        print("Invalid")
        #Prints if the statement is invalid. 
#=======================================================#
def main():
    """Main function to run the task management system."""
    tasks = []
    #Intalizes the array 
    completed = []
    #inalizes the completed list
    notcompleted = []
    #Adds an array called notcompleted 

    while True:
    
        print(" Add a task, Sort tasks into lists, Delete a task, view list, exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
            #Calls the function add_task 
        elif choice == "2":
            #If the user selects two then calls the function sort tasks
            sort_tasks(tasks, completed, notcompleted)
        elif choice == "3":
            
            delete_from_list(completed, notcompleted)
            #Calls fuction delete list
        elif choice == "4":
            #Asks if the user whats to see all the elements of the array
            print(str(completed))
            #Calls the array completed
            print(str(notcompleted))
            #Calls the array notcompleted
        elif choice == "5":
            #If the user selects 5 
            print("Bye!")
            # Prints the statement bye 
            break
        #Exits everything
        else:
            print("Doesn't work")
            # Prints that it doesn't work 

# Run the main function
if __name__ == "__main__":
    main()
    # Calls the main function. 
