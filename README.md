# Python Access Specifiers and Getter, Setter, and Deleter Methods

## 📌 Overview

This repository contains basic Python programs that demonstrate access specifiers, constructors, and data management using Getter, Setter, and Deleter methods.

The examples use classes such as `Student`, `Operator`, `Bank`, and `Amazon` to explain how to access, modify, and delete attributes in Python.

These concepts are useful for understanding **Object-Oriented Programming (OOP)** in Python.

## 🎯 Topics Covered

* Public Access Specifier
* Protected Access Specifier
* Constructors (`__init__`)
* Instance Variables and Class Variables
* Getter Methods
* Setter Methods
* Deleter Methods
* Modifying Object Attributes
* Using `getattr()` to Handle Deleted Attributes

---

## 1. Public Access Specifier

In Python, public attributes and methods can be accessed from inside and outside a class.

By default, attributes and methods are public unless their names follow Python's naming conventions for protected or private members.

### Example

```python
class Student:
    fee = 10000

    def data(self):
        print(f'Total student fee is {self.fee}')


s = Student()

print(s.fee)
s.data()
```

### Explanation

* `Student` is the class name.
* `fee` is a public class variable.
* `data()` is a public method.
* `s = Student()` creates an object of the class.
* `s.fee` accesses the fee.
* `s.data()` calls the method.

### Output

```text
10000
Total student fee is 10000
```

**Key Point:** Public attributes and methods can be accessed directly using an object.

---

## 2. Constructor (`__init__`)

A constructor is a special method that runs automatically when an object is created.

In Python, `__init__()` is commonly used to initialize an object's attributes.

### Example

```python
class Student:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

        print(f'Student Name is {self.name}\n'
              f'Student fee is {self.fee}')


s = Student("XYZ", 5000)

print(s.name)
print(s.fee)
```

### Explanation

* `__init__()` initializes the object's data.
* `name` and `fee` are parameters passed during object creation.
* `self.name` and `self.fee` store the values in the object.
* `Student("XYZ", 5000)` creates an object and passes the values to the constructor.

### Output

```text
Student Name is XYZ
Student fee is 5000
XYZ
5000
```

**Key Point:** The constructor initializes object attributes when an object is created.

---

## 3. Protected Access Specifier

In Python, an attribute or method beginning with a single underscore (`_`) is conventionally treated as protected.
It indicates that the member is intended for internal use within the class and its subclasses.
However, Python does not strictly prevent access to these members from outside the class.

### Example

```python
class Operator:
    _name = "ABC"

    def _Demo(self):
        print(f'Student Name is {self._name}')


o = Operator()

print(o._name)
o._Demo()
```

### Explanation

* `_name` is a protected-by-convention class variable.
* `_Demo()` is a protected-by-convention method.
* Both can still be accessed using an object.
* The underscore indicates that they are intended for internal use.

### Output

```text
ABC
Student Name is ABC
```

**Key Point:** A single underscore is a naming convention, not a strict access restriction.

**Note:** The correct object creation statement is `o = Operator()`, not `o = Operaton()`.

Also, `print(o._Demo())` would print `None` after the method's output because `_Demo()` does not return a value. Use `o._Demo()` when you only want to display the message.

---

## 4. Modifying Attributes in a Class

Python allows you to modify an object's attributes directly.

The following example demonstrates how a bank PIN can be changed.

### Example

```python
class Bank:
    _pin = 1234

    def _Pin_Data(self):
        print(f'Bank Pin Information Is {self._pin}')

    def _Modification(self, new_pin):
        self._pin = new_pin
        print(f'New Modified Pin Number {self._pin}')


b = Bank()

# Before modification
print(b._pin)

# After modification
b._pin = 4567
print(b._pin)
```

### Output

```text
1234
4567
```

### Explanation

* `_pin` is a class variable.
* `b._pin` initially accesses the class variable.
* `b._pin = 4567` creates or updates an instance attribute for the object `b`.
* The new instance attribute takes precedence over the class variable when accessed through `b`.

The class variable remains `1234`, but `b._pin` returns `4567`.

**Key Point:** Direct modification is possible, but controlled access can be useful when validation or additional logic is required.

**Security Note:** This example demonstrates attribute modification for learning purposes. Real banking PINs require secure storage and authentication; a simple class attribute is not secure.

---

## 5. Getter and Setter Methods

Getter and Setter methods provide a way to retrieve and update an object's attributes through methods.

* **Getter:** Retrieves attribute values.
* **Setter:** Updates attribute values.

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Getter(self):
        return self.name, self.age

    def Setter(self, name, age):
        self.name = name
        self.age = age


s = Student("A", 20)

s.Setter("B", 15)

print(s.Getter())
```

### Output

```text
('B', 15)
```

### Explanation

1. The constructor initializes the student with name `"A"` and age `20`.
2. `s.Setter("B", 15)` updates the name and age.
3. `s.Getter()` returns the updated values as a tuple.

### Important Correction

In the original code, the Setter method uses:

```python
self.namme = name
```

The correct statement is:

```python
self.name = name
```

The original spelling creates a separate attribute named `namme` instead of updating `name`.

**Key Point:** Getter and Setter methods allow you to control how attributes are retrieved and modified.

---

## 6. Getter, Setter, and Deleter Methods

This example demonstrates how to retrieve, modify, and delete attributes in a class.

### Example

```python
class Amazon:
    def __init__(self, color, add):
        self.c = color
        self._a = add

    def Getter(self):
        return (
            getattr(self, 'c', 'Color data deleted'),
            getattr(self, '_a', 'Address is deleted')
        )

    def Setter(self, color, add):
        self.c = color
        self._a = add

    def Deleter(self):
        del self.c
        del self._a


a = Amazon("Red", "Pune")

# Get original values
print(a.Getter())

# Update values
a.Setter("Blue", "Deccan")
print(a.Getter())

# Delete attributes
a.Deleter()
print(a.Getter())
```

### Output

```text
('Red', 'Pune')
('Blue', 'Deccan')
('Color data deleted', 'Address is deleted')
```

### Explanation

**Getter Method**

The `Getter()` method retrieves the current color and address.

The `getattr()` function checks whether an attribute exists. If it does not exist, the function returns the specified default message.

**Setter Method**

The `Setter()` method updates the object's color and address.

For example:

```python
a.Setter("Blue", "Deccan")
```

This changes the color to `"Blue"` and the address to `"Deccan"`.

**Deleter Method**

The `Deleter()` method removes both attributes from the object using the `del` statement.

After deletion, `Getter()` uses `getattr()` to display the default messages instead of raising an `AttributeError`.

**Key Point:** Getter, Setter, and Deleter methods demonstrate how an object's data can be retrieved, modified, and deleted.

---

## 7. PEP 8 Naming Convention

PEP 8 is the official Python style guide. It provides recommendations for writing readable and consistent Python code.

Some recommended naming conventions are:

| Element                           | Recommended Convention    | Example        |
| --------------------------------- | ------------------------- | -------------- |
| Class                             | PascalCase                | `Student`      |
| Variable                          | snake_case                | `student_name` |
| Method                            | snake_case                | `get_data()`   |
| Constant                          | UPPER_SNAKE_CASE          | `MAX_LIMIT`    |
| Protected-by-convention attribute | Single leading underscore | `_name`        |
| Name-mangled attribute            | Double leading underscore | `__name`       |

For example, instead of:

```python
def Getter(self):
    return self.name
```

Prefer:

```python
def get_name(self):
    return self.name
```

Similarly, use `set_name()` instead of `Setter()` and `delete_data()` instead of `Deleter()`.

**Note:** PEP 8 recommends naming conventions for readability. It does not require using Getter, Setter, and Deleter methods for every attribute.

---

## 8. Important Concepts to Remember

| Concept                 | Meaning                                                                |
| ----------------------- | ---------------------------------------------------------------------- |
| Public                  | Accessible from outside the class                                      |
| Protected-by-convention | A single underscore indicates intended internal use                    |
| Private-style naming    | A double leading underscore triggers name mangling                     |
| Constructor             | Initializes an object when it is created                               |
| Getter                  | Retrieves attribute values                                             |
| Setter                  | Updates attribute values                                               |
| Deleter                 | Removes attributes                                                     |
| `self`                  | Refers to the current object                                           |
| `getattr()`             | Retrieves an attribute and can return a default value if it is missing |
| `del`                   | Deletes an attribute                                                   |

### Public vs. Protected vs. Private-Style Naming

* `name`: Public attribute.
* `_name`: Attribute intended for internal use by convention.
* `__name`: Attribute subject to name mangling by Python.

Python does not enforce public, protected, and private access exactly as languages such as Java do. A single underscore does not prevent outside access, and double underscores provide name mangling rather than absolute privacy.

---

## 9. Learning Outcomes

After studying these examples, you should be able to:

* Create classes and objects in Python.
* Initialize attributes using constructors.
* Understand public and protected-by-convention naming.
* Access and modify object attributes.
* Write Getter and Setter methods.
* Delete attributes using the `del` statement.
* Handle missing attributes using `getattr()`.
* Follow basic PEP 8 naming conventions.

---

## Conclusion

These examples provide a beginner-friendly introduction to Python access specifiers and attribute management.

Understanding these concepts will help you write more organized Python programs and build a strong foundation in Object-Oriented Programming.

**Technologies Used:** Python 3

**Level:** Beginner

**Topics:** Object-Oriented Programming (OOP), Access Specifiers, Constructors, Getters, Setters, and Deleters.
