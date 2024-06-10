# Type Annotations in Python 3

## Overview
Type annotations are a feature introduced in Python 3.5 that allow developers to specify the expected types of variables, function parameters, and return values. This helps improve code readability and can assist in catching errors during development.

## How You Can Use Type Annotations

### Specifying Function Signatures
Type annotations can be used to specify the types of parameters and return values for functions. This is done by adding a colon `:` followed by the type after each parameter and an arrow `->` followed by the return type at the end of the function signature.

#### Example:
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this example, the `greet` function expects a `name` parameter of type `str` and returns a `str`.

### Specifying Variable Types
You can also use type annotations to specify the types of variables. This is done by adding a colon `:` followed by the type after the variable name.

#### Example:
```python
age: int = 25
height: float = 5.9
name: str = "Alice"
```

In this example, `age` is specified to be of type `int`, `height` is of type `float`, and `name` is of type `str`.

## Duck Typing
Python is a dynamically-typed language, which means that type checking occurs at runtime. Duck typing is a concept where the type or the class of an object is less important than the methods it defines. If an object implements the methods that are being called on it, it is considered to be of the right type.

#### Example:
```python
class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("Woof!")

def make_quack(animal):
    animal.quack()

make_quack(Duck())  # Output: Quack!
make_quack(Dog())   # Output: Woof!
```

In this example, both `Duck` and `Dog` classes have a `quack` method, so they can be passed to the `make_quack` function, demonstrating duck typing.

## How to Validate Your Code with mypy
`mypy` is a static type checker for Python that can be used to validate your type annotations. It checks the consistency of the types and helps catch potential errors before runtime.

### Installation
You can install `mypy` using `pip`:
```sh
pip install mypy
```

### Usage
To check a Python file with `mypy`, simply run the following command:
```sh
mypy yourfile.py
```

### Example:
Consider the following Python file `example.py`:
```python
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(10, "20")
```

Running `mypy example.py` will produce an error because `add_numbers` expects both parameters to be of type `int`, but the second argument is a `str`.

#### Output:
```sh
example.py:4: error: Argument 2 to "add_numbers" has incompatible type "str"; expected "int"
```

Using `mypy` in combination with type annotations can greatly enhance the robustness and maintainability of your Python code.

---

By incorporating type annotations and tools like `mypy` into your development process, you can catch errors early, improve code readability, and make your codebase more maintainable.
