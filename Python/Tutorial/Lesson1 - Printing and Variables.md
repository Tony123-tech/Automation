# 🟢 Lesson 1: Printing & Variables

Welcome to your very first Python lesson! In this module, you will learn how to make Python talk to you using output statements and how to store information using variables.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
1. Print text and values to the terminal using the `print()` function.
2. Create and name variables following Python syntax rules.
3. Understand basic data types: **Strings**, **Integers**, **Floats**, and **Booleans**.
4. Use **f-strings** to combine text and variables smoothly.

---

## 1️⃣ Outputting Text with `print()`

The `print()` function tells Python to display whatever is inside its parentheses.

```python
# Displaying text on the screen
print("Hello, World!")
print("Welcome to Python programming!")
```

## 2️⃣ What is a Variable?
Think of a variable as a labeled box stored in memory. You place a piece of data inside the box, give it a name, and refer back to it whenever you need it.

Creating a Variable
In Python, creating a variable is simple—just choose a name and assign a value using the = operator:

```python
# Assigning values to variables
character_name = "Alex"
character_age = 25

print(character_name)
print(character_age)
```
## 3️⃣ Core Data Types

Python automatically determines what type of data you are storing based on how you write it.

# Python Data Types Reference Guide

| Data Type | Description | Mutability | Example |
| :--- | :--- | :--- | :--- |
| **String (`str`)** | Text enclosed in quotes | **Immutable** | `"Alice"`, `'Python'` |
| **Integer (`int`)** | Whole numbers (positive or negative) | **Immutable** | `42`, `-7` |
| **Float (`float`)** | Decimal numbers | **Immutable** | `3.14`, `19.99` |
| **Boolean (`bool`)** | Logical truth values (`True` or `False`) | **Immutable** | `True`, `False` |
| **NoneType (`NoneType`)** | Represents the absence of a value | **Immutable** | `None` |
| **Tuple (`tuple`)** | Ordered, unchangeable sequence of items | **Immutable** | `(1, 2, "three")` |
| **List (`list`)** | Ordered, changeable sequence of items | **Mutable** | `[1, 2, "three"]` |
| **Dictionary (`dict`)** | Unordered collection of key-value pairs | **Mutable** | `{"name": "Alice", "age": 25}` |
| **Set (`set`)** | Unordered collection of unique items | **Mutable** | `{1, 2, 3}` |

## Key Concepts

* **Mutable**: The data can be changed or updated in place after creation (`list`, `dict`, `set`).
* **Immutable**: The data cannot be changed after creation. Any modification creates a new object in memory (`str`, `int`, `float`, `bool`, `NoneType`, `tuple`).
* **Dictionary Keys**: Only **immutable** types can be used as dictionary keys or stored in a set.

# Comprehensive Python Data Types Reference

This guide covers Python's core data types, their properties, and a complete code example demonstrating how to declare and use each one.

## Core Data Types Table

| Data Type | Description | Mutability | Declaration Example |
| :--- | :--- | :--- | :--- |
| **String (`str`)** | Text data | **Immutable** | `text = "Hello World"` |
| **Integer (`int`)** | Whole numbers | **Immutable** | `num = -42` |
| **Float (`float`)** | Fractional/decimal numbers | **Immutable** | `price = 99.95` |
| **Boolean (`bool`)** | Truth values (`True`/`False`) | **Immutable** | `is_active = True` |
| **NoneType (`NoneType`)** | Absence of a value | **Immutable** | `data = None` |
| **List (`list`)** | Ordered, modifiable sequence | **Mutable** | `items = [1, 2, 3]` |
| **Tuple (`tuple`)** | Ordered, static sequence | **Immutable** | `point = (4, 5)` |
| **Dictionary (`dict`)** | Key-value mapping | **Mutable** | `user = {"id": 101}` |
| **Set (`set`)** | Unordered, unique items | **Mutable** | `unique_ids = {1, 2, 3}` |

---
