# 0x00. AirBnB clone - The console

## Background Context
### Welcome to the AirBnB clone project!

#### First step: Write a command interpreter to manage your AirBnB objects.

<p>
This is the first step towards building your first full web application: the ___AirBnB clone___. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
</p>

<p>
Each task is linked and will help you to:

-  put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
-  create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-  create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from BaseModel
-  create the first abstracted storage engine of the project: File storage.
-  create all unittests to validate all our classes and storage engine
</p>

### What’s a command interpreter?

<p>
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
</p>

### Usage
1. ___Starting the console___
```
$ ./console.py
(hbnb)
```

2. ___Creating an object___
```
(hbnb) create
** class name missing **
(hbnb) create User
670265eb-5982-489e-8b92-2dff054f0776
```

3. ___Showing an object___
```
(hbnb) show User
** instance id missing **
(hbnb) show User 670265eb-5982-489e-8b92-2dff054f0776
[User] (670265eb-5982-489e-8b92-2dff054f0776) {'created_at': datetime.datetime(2023, 11, 10, 22, 8, 58, 458246), 'id': '670265eb-5982-489e-8b92-2dff054f0776', 'updated_at': datetime.datetime(2023, 11, 10, 18, 12, 09, 458261)}
```

4. ___Updating objects___
```
(hbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'created_at': datetime.datetime(2023, 11, 10, 22, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2023, 11, 10, 18, 11, 32, 341161)}"]
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612
** attribute name missing **
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612  Age "24"
(hbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'Age': 20, 'created_at': datetime.datetime(2023, 11, 10, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2023, 11, 10, 22, 13, 9, 937933)}"]
(hbnb)
```

5. ___Destroying objects___
```
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 670265eb-5982-489e-8b92-2dff054f0776
(hbnb)
```

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
<p>All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`</p>
