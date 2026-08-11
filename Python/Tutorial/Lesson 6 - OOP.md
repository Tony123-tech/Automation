# Complete Guide to Classes & Object-Oriented Programming

Classes act as structural blueprints used to create custom data objects, bundling data properties and executable behaviors together into a unified module.

---

### 1. Class Definition & Object Creation
The baseline structure used to declare custom types and instantiate real instances from them.
* **`class` Keyword**: The essential prefix statement used to signal the creation and naming of a new object blueprint.
* **Instance**: A concrete object created from a class template that possesses its own unique copies of attributes and data states.

---

### 2. Initialization & Data Attributes
Mechanisms used to configure an object's individual identity and state at the moment it is built.
* **`__init__` Method**: The initialization function that runs automatically every time a new instance is created from the class blueprint.
* **`self` Parameter**: The mandatory first parameter in class functions that represents the specific object instance currently being built or modified.
* **Attributes**: Internal variables attached to an instance that store its distinct data properties and state values.

---

### 3. Object Methods
Functions defined inside a class that govern the actions, logic, and behaviors an object can perform.
* **Instance Methods**: Custom functions that accept `self` as their first parameter, giving them direct access to read or update that object's unique attributes.
* **Encapsulation**: The grouping of related data attributes and behaviors inside a single class shell to hide internal complexity.

---

### 4. Classes & Objects Reference Matrix

| Object Concept | Core Element | Structural Objective | Execution Behavior / Boundaries |
| :--- | :--- | :--- | :--- |
| **Blueprint** | `class` | Define a new structural data type | Registers the custom type properties into memory |
| **Realization** | *Instance* | Create a physical object from a class | Reserves separate space in memory for an object |
| **Setup** | `__init__` | Initialize baseline object properties | Triggers automatically during object creation |
| **Reference** | `self` | Target the active object instance | Provides a direct link to the caller object's internal data |
| **State Data** | *Attribute* | Store data properties inside an object | Persists inside the object for its entire lifecycle |
| **Behavior** | *Method* | Execute functions bound to an object | Alters or computes data tracking the specific instance |
