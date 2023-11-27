<img  height="50px" align="right" src="https://apply.holbertonschool.com/holberton-logo.png" alt="Holberton School logo">

# AirBnB clone - MySQL

## 🔖 Table of contents
<details>
        <summary>
		CLICK TO ENLARGE 😇
        </summary>
	    📝 <a href="#description">Description</a>
        <br>
        🔨 <a href="#tech-stack">Tech stack</a>
        <br>
        📋 <a href="#requirements">Requirements</a>
        <br>
        🎓 <a href="#instructions">Instructions</a>
        <br>
        📂 <a href="#files-description">Files description</a>
        <br>
        💻 <a href="#installation">Installation</a>
        <br>
        📥 <a href="#examples">Examples</a>
        <br>
        ♥️ <a href="#thanks">Thanks</a>
        <br>
        👷 <a href="#authors">Authors</a>
</details>

## 📝 <span id="description">Description</span>

This repository is a fork of the following one: <a href="https://github.com/justinmajetich/AirBnB_clone">AirBnB_clone</a>.
<br>
It represents the initial stage of a student project to build a clone of the AirBnB website.
<br>
This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

## 🔨 <span id="tech-stack">Tech stack</span>

<p align="left">
    <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white&style=for-the-badge" alt="VIM badge">
    <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge" alt="VIM badge">
    <img src="https://img.shields.io/badge/JSON-000000?logo=json&logoColor=white&style=for-the-badge" alt="VIM badge">
    <img src="https://img.shields.io/badge/MYSQL-4479A1?logo=mysql&logoColor=white&style=for-the-badge" alt="VIM badge">
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" alt="Shell badge">
    <img src="https://img.shields.io/badge/UBUNTU-e95420?logo=ubuntu&logoColor=white&style=for-the-badge" alt="Ubuntu badge">
    <img src="https://img.shields.io/badge/VISUAL STUDIO CODE-007ACC?logo=visualstudiocode&logoColor=white&style=for-the-badge" alt="VIM badge">
<p>

## 📋 <span id="requirements">Requirements</span>

### Python Scripts
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version 3.8.5).
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- The code should use the `pycodestyle` (version 2.7.*).
- All your files must be executable.
- All the functions, classes, modules and scripts should have a documentation.
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose...

### Python Unit Tests
- You have to use the `unittest` module.
- All your test files should be inside a folder `tests`.
- All your test files should be python files (extension: `.py`).
- All your test files and folders should start by `test_`.
- Your file organization in the tests folder should be the same as your project.
- All your tests should be executed by using this command: `python3 -m unittest discover tests`.

### SQL Scripts
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version 3.8.5).
- Your files will be executed with `SQLAlchemy` (version 1.4.x).
- All your SQL queries should have a comment just before.
- All your files should start by a comment describing the task.
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…).

## 🎓 <span id="instructions">Instructions</span>

<details>
	<summary>
		<b>Task. 0. Fork me if you can!</b>
	</summary>
	<br>

In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might include:

- “Who did this code?”
- “How it works?”
- “Where are unittests?”
- “Where is this?”
- “Why did they do that like this?”
- “I don’t understand anything.”
- “…I will refactor everything…”

But the worst thing you could possibly do is to **redo everything**. Please don’t do that! **Note: the existing codebase might be perfect, or it might have errors. Don’t always trust the existing codebase!**.

For this project you will fork this codebase:

- Update the repository name (specified in the **section Repo**).
- Update the README.md with your information **but don’t delete the initial authors**.

#
**Repo:**
- GitHub repository: `holbertonschool-AirBnB_clone_v2`.
<hr>
</details>

## 📂 <span id="files-description">Files description</span>


| Tasks | Files | Description |
| ----- | ----- | ----------- |
| 0: Authors/README File | [AUTHORS]() | Project authors. |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests]() | All class-defining modules are unittested. |
| 3. Make BaseModel | [/models/base_model.py]() | Defines a parent class to be inherited by all model classes. |
| 4. Update BaseModel w/ kwargs | [/models/base_model.py]() | Add functionality to recreate an instance of a class from a dictionary representatio. |
| 5. Create FileStorage class | [/models/engine/file_storage.py]() [/models/_ _init_ _.py]() [/models/base_model.py]() | Defines a class to manage persistent file storage system. |
| 6. Console 0.0.1 | [console.py]() | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D. |
| 7. Console 0.1 | [console.py]() | Update the console with methods allowing the user to create, destroy, show, and update stored data. |
| 8. Create User class | [console.py]() [/models/engine/file_storage.py]() [/models/user.py]() | Dynamically implements a user class. |
| 9. More Classes | [/models/user.py]() [/models/place.py]() [/models/city.py]() [/models/amenity.py]() [/models/state.py]() [/models/review.py]() | Dynamically implements more classes. |
| 10. Console 1.0 | [console.py]() [/models/engine/file_storage.py]() | Update the console and file storage system to work dynamically with all  classes update file storage. |

## 💻 <span id="installation">Installation</span>

- First, clone this repository.

- Once the repository is cloned locate the "console.py" file and run it as follows:

```
/AirBnB_clone$ ./console.py
```

- When this command is run the following prompt should appear:

```
(hbnb)
```

- This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

### Commands

- `create`: creates an instance based on given class.
- `destroy`: destroys an object based on class and UUID.
- `show`: shows an object based on class and UUID.
- `all`: shows all objects the program has access to, or all objects of a given class.
- `update`: updates existing attributes an object based on class name and UUID.
- `quit`: exits the program (EOF will as well).

### Alternative Syntax

Users are able to issue a number of console command using an alternative syntax:

**Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])**

Advanced syntax is implemented for the following commands: 

- `all`: shows all objects the program has access to, or all objects of a given class.
- `count`: return number of object instances by class.
- `show`: shows an object based on class and UUID.
- `destroy`: destroys an object based on class and UUID.
- `update`: updates existing attributes an object based on class name and UUID.

## 📥 <span id="examples">Examples</span>

<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

## ♥️ <span id="thanks">Thanks</span>

A big thank you to all my Holberton School peers for their help and support throughout these projects.

## 👷 <span id="authors">Authors</span>

### Original authors:

**Ezra Nobrega**
- Github: [@eNobreg](https://github.com/eNobreg)

**Justin Majetich**
- Github: [justinmajetich](https://github.com/justinmajetich)

### Fork authors:

**Fabien CHAVONET**
- Github: [@fchavonet](https://github.com/fchavonet)

**Xavier Bertin**
- Github: [@Erkenoss](https://github.com/Erkenoss)
