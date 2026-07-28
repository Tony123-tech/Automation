# Comprehensive Programming Operations Guide

Operations form the core building blocks of computer logic, defining how data is processed, modified, and evaluated.

---

### 1. Arithmetic Operations
Used to perform standard mathematical calculations on numerical data.
* **Addition (`+`)**: Computes the sum of two values.
* **Subtraction (`-`)**: Subtracts the second value from the first to find the difference.
* **Multiplication (`*`)**: Multiplies two values to find the product.
* **Division (`/`)**: Divides the numerator by the denominator.
* **Floor Division (`//`)**: Divides two numbers and rounds down to the nearest integer.
* **Modulus (`%`)**: Returns the remaining remainder after a division check.
* **Exponentiation (`**`)**: Raises a base number to the power of an exponent.

---

### 2. Assignment Operations
Used to assign, initialize, or update values stored inside system variables.
* **Basic Assignment (`=`)**: Assigns the value from the right side directly to the left variable.
* **Add and Assign (`+=`)**: Adds the right value to the variable and saves the new total.
* **Subtract and Assign (`-=`)**: Subtracts the right value from the variable and saves the new total.
* **Multiply and Assign (`*=`)**: Multiplies the variable by the right value and saves the new total.
* **Divide and Assign (`/=`)**: Divides the variable by the right value and saves the new total.

---

### 3. Comparison (Relational) Operations
Used to test relationships between data points, returning either a `true` or `false` status.
* **Equality Check (`==`)**: Validates if two elements match exactly.
* **Inequality Check (`!=`)**: Confirms if two values are distinctly different.
* **Greater Than (`>`)**: Assesses if the left value exceeds the right value.
* **Less Than (`<`)**: Assesses if the left value is smaller than the right value.
* **Greater Than or Equal To (`>=`)**: Checks if the left value is larger than or equal to the right.
* **Less Than or Equal To (`<=`)**: Checks if the left value is smaller than or equal to the right.

---

### 4. Logical Operations
Used to chain multiple conditional evaluations together to dictate structural routing.
* **Conjunction (`AND`)**: Returns true only if **every** individual criteria passes.
* **Disjunction (`OR`)**: Returns true if **at least one** individual criteria passes.
* **Negation (`NOT`)**: Inverts the state, turning true to false and false to true.

---

### 5. Bitwise Operations
Used to manipulate raw binary data at the individual bit level (zeros and ones).
* **Bitwise AND (`&`)**: Sets each bit to 1 if both matching bits are 1.
* **Bitwise OR (`|`)**: Sets each bit to 1 if at least one matching bit is 1.
* **Bitwise XOR (`^`)**: Sets each bit to 1 only if the two matching bits are opposite.
* **Bitwise NOT (`~`)**: Flips all individual bits in the sequence.
* **Left Shift (`<<`)**: Shifts binary digits to the left, filling empty spaces with zeros.
* **Right Shift (`>>`)**: Shifts binary digits to the right, discarding overflowing ends.

---

### 6. Identity & Membership Operations
Used to validate the structural memory and sequence containment of data objects.
* **Identity Match (`is`)**: Checks if two separate variables reference the exact same memory location.
* **Identity Mismatch (`is not`)**: Checks if two variables point to different memory locations.
* **Membership Present (`in`)**: Checks if a specific sequence contains a target value.
* **Membership Absent (`not in`)**: Checks if a target value is completely missing from a sequence.

---

### 7. Operations Overview Matrix

| Operation Category | Primary Role | Core Syntax Symbols | Resulting Output |
| :--- | :--- | :--- | :--- |
| **Arithmetic** | Process raw mathematical data | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Numeric Value |
| **Assignment** | Initialize or update variables | `=`, `+=`, `-=`, `*=`, `/=` | Variable Update |
| **Comparison** | Analyze data-point relationships | `==`, `!=`, `>`, `<`, `>=`, `<=` | Boolean (`true`/`false`) |
| **Logical** | Build multi-step decision gates | `AND`, `OR`, `NOT` | Boolean (`true`/`false`) |
| **Bitwise** | Process binary digits directly | `&`, `\|`, `^`, `~`, `<<`, `>>` | Numeric / Binary |
| **Identity** | Verify object memory state | `is`, `is not` | Boolean (`true`/`false`) |
| **Membership** | Scan data sequence containers | `in`, `not in` | Boolean (`true`/`false`) |
