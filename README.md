# AirBnB clone - The console

## Project Description

>This is the first part of the Airbnbn Clone Project, in this part we have to create the console or command 
interpreter to manipulate data without a visual interface, this command interpreter is like a shell, it recives an user input and do some things to manipulate the data.

# Command Interpreter

## How to Start It
### Step 1
>Clone this github repository and move to the folder.
``` 
 $ git clone https://github.com/JuanManuelReyes/holbertonschool-AirBnB_clone.git 
 $ cd holbertonschool-AirBnB_clone
 ```
### Step 2
If you want to use the console on Interactive Mode, follow this instructions:
#### Interactive Mode
```
 $ ./console.py
 
 (hbnb) help

 Documented commands (type help <topic>):
 ========================================
 ENTER  EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$

```

If you want to use the console on Non-Interactive Mode, follow this instructions:
#### Non-Interactive Mode
```
$ echo "help" | ./console.py 
(hbnb) 

Documented commands (type help <topic>): 
======================================== 
ENTER  EOF  all  create  destroy  help  quit  show  update 
(hbnb) 
$ 
$ cat test_help 
help 
$ 
$ cat test_help | ./console.py 
(hbnb) 

Documented commands (type help <topic>): 
======================================== 
EOF help quit 
(hbnb) 
$

```

## How to Use It

---
| Commands  | Syntaxis                                       | Function|
| --------- | ---------------------------------------------  | ----------------------------------------- |
| `quit`    | ` quit `                                       | Quit command to exit the program |  
| `EOF`     |  ` *ctrl + C* `                                | EOF command to exit the program |
| `help`    | ` help <command> `                             | List available commands with "help" or detailed help with "help cmd" |
| `ENTER`   | ` *intro* `                                    | Do nothing |
| `create`  | ` create <class> `                             | Command used to create a new object. | 
| `show`    | ` show <class> <id> `                          | Command used to show the information of an object. |
| `destroy` | ` destroy <class> < id> `                      | Command used to deletes an object. |               
| `all`     | ` all <class> or all`                          | Command used to print all created objects. |
| `update`  | ` update <class> <id> <attribute name> <attribute value>` | Command used to uptdate attributes from created obejects |
                    
## Authors

* [Tarik Calixto](https://github.com/tarikaudi)
* [Juan Manuel Reyes](https://github.com/JuanManuelReyes)