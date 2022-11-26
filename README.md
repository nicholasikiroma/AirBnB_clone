## Description

HBnB is a complete web application, integrating database storage, 
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

## Classes

HolbertonBnB utilizes the following classes:

BaseModel  FileStorage  User  State  City  Amenity  Place  Review 

## Storage

The classes are handled by the abstracted storage engine defined in the 
FileStorage class.

## Console 

The console is a command line interpreter that permits management of the backend 
of HolbertonBnB. It can be used to handle and manipulate all classes utilized by 
the application (achieved by calls on the storage object defined above).

### Using the Console

To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file console.py at the command line.


### Console Commands

The HolbertonBnB console supports the following commands:

* **create**

Creates a new instance of a given class. The class' ID is printed and 
the instance is saved to the file `file.json`.


* **show**

Prints the string representation of a class instance based on a given id.
 
 
* **destroy**

Deletes a class instance based on a given id. The storage file `file.json` 
is updated accordingly.

* **all**

Prints the string representations of all instances of a given class. If no 
class name is provided, the command prints all instances of every class.

* **count**

Retrieves the number of instances of a given class.

* **update**

Updates a class instance based on a given id with a given key/value attribute 
pair or dictionary of attribute pairs. If `update` is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by 
providing a dictionary.


## Testing

Unittests for the HolbertonBnB project are defined in the tests
folder.

Alternatively, you can specify a single test file to run at a time:


## Authors
* **Nicholas Ikiroma** <[nicholasikiroma](https://github.com/nicholasikiroma/)>
* **Getachew Yazie** <[Getachew7](https://github.com/Getachew7/)>
