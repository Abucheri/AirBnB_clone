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

4. Create BaseModel from dictionary
	- Previously we created a method to generate a dictionary representation of an instance (method `to_dict())`.
	- Now it’s time to re-create an instance with this dictionary representation.
	```
	<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
	```
	- Update `models/base_model.py`:
		- `__init__(self, *args, **kwargs)`:
			- you will use `*args`, `**kwargs` arguments for the constructor of a `BaseModel`. (more information inside the ___AirBnB clone___ concept page)
			- `*args` won’t be used
			- if `kwargs` is not empty:
				- each key of this dictionary is an attribute name (___Note___ `__class__` from `kwargs` is the only one that should not be added as an attribute. See the example output, below)
				- each value of this dictionary is the value of this attribute name
				- ___Warning___: `created_at` and `updated_at` are strings in this dictionary, but inside your `BaseModel` instance is working with `datetime` object. You have to convert these strings into `datetime` object. Tip: you know the string format of these datetime
			- otherwise:
				- create `id` and `created_at` as you did previously (new instance)
	```
	guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
	#!/usr/bin/python3
	from models.base_model import BaseModel

	my_model = BaseModel()
	my_model.name = "My_First_Model"
	my_model.my_number = 89
	print(my_model.id)
	print(my_model)
	print(type(my_model.created_at))
	print("--")
	my_model_json = my_model.to_dict()
	print(my_model_json)
	print("JSON of my_model:")
	for key in my_model_json.keys():
	    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

	print("--")
	my_new_model = BaseModel(**my_model_json)
	print(my_new_model.id)
	print(my_new_model)
	print(type(my_new_model.created_at))

	print("--")
	print(my_model is my_new_model)

	guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
	56d43177-cc5f-4d6c-a0c1-e167f8c27337
	[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
	<class 'datetime.datetime'>
	--
	{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
	JSON of my_model:
	    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
	    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
	    __class__: (<class 'str'>) - BaseModel
	    my_number: (<class 'int'>) - 89
	    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
	    name: (<class 'str'>) - My_First_Model
	--
	56d43177-cc5f-4d6c-a0c1-e167f8c27337
	[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
	<class 'datetime.datetime'>
	--
	False
	guillaume@ubuntu:~/AirBnB$ 
	```

5. Store first object
	- Now we can recreate a `BaseModel` from another one by using a dictionary representation:
	```
	<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
	```
	- It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.
	- Writing the dictionary representation to a file won’t be relevant:
		- Python doesn’t know how to convert a string to a dictionary (easily)
		- It’s not human readable
		- Using this file with another program in Python or other language will be hard.
	- So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.
	- Now the flow of serialization-deserialization will be:
	```
	<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
	```
	- Magic right?
	- Terms:
		- ___simple Python data structure___: Dictionaries, arrays, number and string. ex: `{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }`			
		- ___JSON string representation___: String representing a simple data structure in JSON format. ex: `'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'`
	- Write a class `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances:
		- `models/engine/file_storage.py`
		- Private class attributes:
			- `__file_path`: string - path to the JSON file (ex: `file.json`)
			- `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`)
		- Public instance methods:
			- `all(self)`: returns the dictionary `__objects`
			- `new(self, obj)`: sets in `__objects` the `obj` with key `<obj class name>.id`
			- `save(self)`: serializes `__objects` to the JSON file (path: `__file_path`)
			- `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
	-  Update `models/__init__.py`: to create a unique `FileStorage` instance for your application 
		- import `file_storage.py`
		- create the variable `storage`, an instance of `FileStorage`
		- call `reload()` method on this variable
	- Update `models/base_model.py`: to link your `BaseModel` to `FileStorage` by using the variable `storage`
		- import the variable `storage`
		- in the method `save(self)`:
			- call `save(self)` method of `storage`
		- `__init__(self, *args, **kwargs)`:
			- if it’s a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`
	```
	guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
	#!/usr/bin/python3
	from models import storage
	from models.base_model import BaseModel

	all_objs = storage.all()
	print("-- Reloaded objects --")
	for obj_id in all_objs.keys():
	    obj = all_objs[obj_id]
	    print(obj)

	print("-- Create a new object --")
	my_model = BaseModel()
	my_model.name = "My_First_Model"
	my_model.my_number = 89
	my_model.save()
	print(my_model)

	guillaume@ubuntu:~/AirBnB$ cat file.json
	cat: file.json: No such file or directory
	guillaume@ubuntu:~/AirBnB$ 
	guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
	-- Reloaded objects --
	-- Create a new object --
	[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
	guillaume@ubuntu:~/AirBnB$ 
	guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
	{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
	guillaume@ubuntu:~/AirBnB$
	guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
	-- Reloaded objects --
	[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
	-- Create a new object --
	[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
	guillaume@ubuntu:~/AirBnB$ 
	guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
	-- Reloaded objects --
	[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
	[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
	-- Create a new object --
	[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
	guillaume@ubuntu:~/AirBnB$ 
	guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
	{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
	guillaume@ubuntu:~/AirBnB$ 
	```
6. Console 0.0.1
	- Write a program called `console.py` that contains the entry point of the command interpreter:
		- You must use the module `cmd`
		- Your class definition must be: `class HBNBCommand(cmd.Cmd):`
		- Your command interpreter should implement:
			- `quit` and `EOF` to exit the program
			- `help` (this action is provided by default by `cmd` but you should keep it updated and documented as you work through tasks)
			- a custom prompt: `(hbnb)`
			- an empty line + `ENTER` shouldn’t execute anything
		- Your code should not be executed when imported
	- ___Warning:___
	- You should end your file with:
	```	
	if __name__ == '__main__':
	    HBNBCommand().cmdloop()
	```
	- to make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise
	```
	guillaume@ubuntu:~/AirBnB$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) help quit
	Quit command to exit the program

	(hbnb) 
	(hbnb) 
	(hbnb) quit 
	guillaume@ubuntu:~/AirBnB$ 
	```
	- ___No unittests needed___

### Project Authors:
- O'Brien Abucheri <[Abucheri](https://github.com/Abucheri/)>
