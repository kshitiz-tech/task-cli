'''
Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
'''
 
import sys
import time
from validator import format_validator

    
#Task class for each task 
class Task():
    #tasks list is a class based list which will store each individual task as an object in this task list
    tasks = []

    #initializing the tasks field
    def __init__(self,task,status, createdAt, updatedAt):
        if len(Task.tasks) == 0:
            self.id = 1
        else: 
            self.id = len(Task.tasks)+1
        self.task = task
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt


    def add(self):
        try: 
            Task.tasks.append(self)
        except Exception as e:
            print(f"Error: {e}")

    def update(self,task,updatedAt):
        self.task = task
        self.updatedAt = updatedAt

    def delete(self,id):
        if self.id == id:
            Task.tasks.remove(self)

    def mark_in_progress(self, id ):
        if self.id == id:
            self.status = 'in-progress'

    def mark_todo(self,id):
        if self.id == id:
            self.status = 'todo'

    def mark_done(self,id):
        if self.id == id:
            self.status = 'done'

    def list(self):
        for task in Task.tasks:
            print(task)

    def __str__(self):

        return f'ID: {self.id}\tDescription: {self.task}\tStatus: {self.status}\tCreatedAt:{self.createdAt}\tUpdatedAt:{self.updatedAt}'
    
    def list_status(self,status):
        if self.status == status:
            print(self)

#timer function for returning the time accessed for createdAt and updatedAt field
def timer():
    the_time = time.localtime()
    return f"{the_time[2]}/{the_time[1]}/{the_time[0]} {the_time[3]}:{f'{the_time[4]:02d}'}"

#creating object for task
def create_object(task,status,createdAt,updatedAt):
    task = Task(task,status,createdAt,updatedAt)
    return task

#validates the id passed as an argument. 
def exist_validator(id):
    for task in Task.tasks:
        if task.id == id:
            return True, task
    return False, None

#writes a json file to save all the data in the tasks[] list. 
def save():
    with open("database.json", "a+") as file:
        file.write('{\"task\":{')
        count = 0
        for record in Task.tasks:
            file.write(f"\"id\":{record.id},\"description\": \"{record.task}\",\"status\":\"{record.status}\",\"createdAt\":\"{record.createdAt}\",\"updatedAt\":\"{record.updatedAt}\"")
            count += 1
            if count == len(Task.tasks):
                file.write("}\n")
            else:
                file.write("},\n")


        
#if called, displays all of the syntax for the commands
def help():
    print('''
add :\tadd "<task you want to add>"
update:\tupdate "<task with updated details>" <task_id of which task you want to update>
delete:\tdelete <task_id of the task you want to delete>
list:\tlist (lists all of the task)
list with status:list <status>
mark-in-progress:mark-in-progress <task_id to mark>
mark-todo:\tmark-todo <task_id to mark>
mark-done:\tmark-done <task_id to mark>
ctrl + (any key): for exit

'''
    )


#main function 
def main():


    commands = ['add', 'update', 'delete', 'mark-in-progress', 'mark-todo', 'mark-done','list','help','save']


    while True:

        print("task-cli ", end = '') 

        try: 
            inputs = input()
        except (KeyboardInterrupt, EOFError):
            sys.exit()
        if len(inputs) < 1:
            continue
        inputs = inputs.strip().split()
        command = inputs[0]
        co_arg = ' '.join(inputs[1:])

        #command validation
        if command not in commands:  
            print(f"Error:{command} Command not found")
            continue

        match command:

            case 'add':

                validated, detail = format_validator(command,co_arg)

                if validated:
                    task = create_object(detail,'not-done',timer(),updatedAt= None)

                    try:
                        task.add()
                    except Exception as e:
                        print(f"Error: {e}")
                    else:
                        print("Task Added Successfully")

                else:
                    print(detail)

            case 'update':
                boolean, task, id = format_validator(command,co_arg)
                if boolean:

                    validated_id ,task = exist_validator(id)
                    if not validated_id:
                        print("Task does not exists. ")
                        continue
                    try:
                        task.update(task=detail,updatedAt=timer())
                    except Exception as e:
                        print(f"Error: {e}")
                    else:
                        print("Task Updated Successfully. UpdatedAt: ",timer())
                    
                else:
                    print(task)
                
            case 'delete':
                boolean, id = format_validator(command,co_arg)

                if boolean:
                    validated_id,task = exist_validator(id)

                    if not validated_id:
                        print("Task does not exists. ")
                        continue
                    try:

                        task.delete(id)
                    except Exception as e:
                        print(f"Error: {e}")
                    else:
                        print("Task Deleted Successfully")
                else:
                    print(id)
                
            case 'mark-in-progress':

                boolean, id = format_validator(command,co_arg)
                
                if boolean:
                    validated_id,task = exist_validator(id)
                    if not validated_id:
                        print("Task does not exists. ")
                        continue
                    try:
                        task.mark_in_progress(id)
                    except Exception as e:
                        print(f"Error: {e}")
                    else:
                        print("Task marked Successfully")
                    
                else:
                    print(id)

            case 'mark-todo':
                boolean, id = format_validator(command,co_arg)
                if boolean:
                    validated_id,task = exist_validator(id)
                    if not validated_id:
                        print("Task does not exists. ")
                        continue
                    try:
                        task.mark_todo(id)
                    except Exception as e:
                        print(f"Error: {e}")
                    else:
                        print("Task marked Successfully")
                    
                else:
                    print(id)


            case 'mark-done':
                boolean, id = format_validator(command,co_arg)
                if boolean:
                    validated_id,task = exist_validator(id)
                    if not validated_id:

                        print("Task does not exists. ")

                        continue
                    try:
                        task.mark_done(id)
                    except Exception as e:
                        print(f"Error: {e}")
                    else:
                        print("Task marked Successfully")
                    
                else:
                    print(id)

            case 'list':
                boolean, args = format_validator(command,co_arg)
                if boolean:
                    if args == None:
                        try:
                            task.list()
                        except Exception as e:
                            print(f"Error: {e}")
                        else:
                            pass
                    else:
                        if args not in ['in-progress','todo','not-done','done']:

                            print("Invalid status requested")
                            continue
                        try:
                            task.list_status(args)
                        except Exception as e:
                            print(f"Error: {e}")
                        else:
                            pass
                        
                else:
                    print(args)
            case 'help':
                help()
            
            case 'save':
                save()
                sys.exit()
       
main()



        
