![the logo](https://github.com/Abucheri/AirBnB_clone/assets/24778489/c7fb7d38-1adb-4558-aad9-6a7fe23f9070)

# 0x00. AirBnB clone - The console

## Background Context
### Welcome to the AirBnB clone project!

#### First step: Write a command interpreter to manage your AirBnB objects.

<p>
This is the first step towards building your first full web application: the ___AirBnB clone___. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
</p>

In this first part We will be building a console application to carry out ___CRUD___, ___serialization___ and ___deserialization___ functions for the app. The console will also be creating, updating and destroting/deleting objects.

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

![console_map](https://github.com/Abucheri/AirBnB_clone/assets/24778489/78485517-4033-45b3-b304-38e58fd30e32)


0. README, AUTHORS
	- Write a `README.md`:
		- description of the project
		- description of the command interpreter:
			- how to start it
			- how to use it
			- examples
	- You should have an `AUTHORS` file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker’s AUTHORS page](https://github.com/moby/moby/blob/master/AUTHORS)
	- You should use branches and pull requests on GitHub - it will help you as team to organize your work

1. Be pycodestyle compliant!
	- Write beautiful code that passes the pycodestyle checks.

2. Unittests
	- All your files, classes, functions must be tested with unit tests
	```
	guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
	...................................................................................
	...................................................................................
	.......................
	----------------------------------------------------------------------
	Ran 189 tests in 13.135s

	OK
	guillaume@ubuntu:~/AirBnB$
	```
	- Note that this is just an example, the number of tests you create can be different from the above example.
	- ___Warning___:
	- Unit tests must also pass in non-interactive mode:
	```
	guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
	...................................................................................
	...................................................................................
	.......................
	----------------------------------------------------------------------
	Ran 189 tests in 13.135s

	OK
	guillaume@ubuntu:~/AirBnB$
	```

3. BaseModel
	- Write a class `BaseModel` that defines all common attributes/methods for other classes:
		- `models/base_model.py`
		- Public instance attributes:
			- `id`: string - assign with an `uuid` when an instance is created:
				- you can use `uuid.uuid4()` to generate unique `id` but don’t forget to convert to a string
				- the goal is to have unique `id` for each `BaseModel`
			- `created_at`: datetime - assign with the current datetime when an instance is created
			- `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
		- `__str__`: should print: `[<class name>] (<self.id>) <self.__dict__>`
		- Public instance methods:
			- `save(self)`: updates the public instance attribute `updated_at` with the current datetime
			- `to_dict(self)`: returns a dictionary containing all keys/values of `__dict__` of the instance:
				- by using `self.__dict__`, only instance attributes set will be returned
				- a key `__class__` must be added to this dictionary with the class name of the object
				- `created_at` and `updated_at` must be converted to string object in ISO format:
					- format: `%Y-%m-%dT%H:%M:%S.%f` (ex: `2017-06-14T22:31:03.285259`)
					- you can use `isoformat()` of `datetime` object
				- This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our `BaseModel`
	```
	guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
	#!/usr/bin/python3
	from models.base_model import BaseModel

	my_model = BaseModel()
	my_model.name = "My First Model"
	my_model.my_number = 89
	print(my_model)
	my_model.save()
	print(my_model)
	my_model_json = my_model.to_dict()
	print(my_model_json)
	print("JSON of my_model:")
	for key in my_model_json.keys():
	    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

	guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
	[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
	[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
	{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
	JSON of my_model:
	    my_number: (<class 'int'>) - 89
	    name: (<class 'str'>) - My First Model
	    __class__: (<class 'str'>) - BaseModel
	    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
	    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
	    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

	guillaume@ubuntu:~/AirBnB$ 
	```

### Project Authors:
- O'Brien Abucheri <[Abucheri](https://github.com/Abucheri/)>
