# Complete Guide to Control Flow

Control flow structures dictate the order in which individual logic statements are executed based on conditions, loops, and state changes.

---

### 1. Conditional Statements
Conditional statements act as decision gates, directing the program down distinct execution paths based on binary evaluations.
* **`if`**: The foundational entry point that executes its nested block only if the evaluated condition is `true`.
* **`elif`** *(Else If)*: Checks alternative sequential conditions when all preceding validation checks return `false`.
* **`else`**: The final fallback block that executes only if every single preceding condition evaluates to `false`.

---

### 2. Loops & Iteration Structures
Loops automate repetitive operations by running blocks of code multiple times over a sequence or while a state is maintained.
* **`for` loops**: Iterates over a predetermined, finite sequence (such as a string, list, or fixed numeric range).
* **`while` loops**: Repeats a code block indefinitely as long as a target condition remains continuously `true`.

---

### 3. Loop Control Statements
Loop controls modify the standard execution behavior of active loops, allowing manual termination or step skipping.
* **`break`**: Immediately terminates the active loop entirely and forces execution to the next line of code outside the loop.
* **`continue`**: Skips the rest of the current iteration block and jumps directly to the beginning of the next cycle.
* **`pass`**: A structural placeholder that does absolutely nothing; used to avoid syntax errors in empty code blocks.

---

### 4. Control Flow Reference Matrix

| Control Type | Core Keyword | Structural Objective | Execution Result |
| :--- | :--- | :--- | :--- |
| **Conditional** | `if` | Check initial boundary state | Runs block if `true` |
| **Conditional** | `elif` | Check secondary alternative state | Runs block if preceding fails & current is `true` |
| **Conditional** | `else` | Handle all remaining unmapped states | Runs block as a final catch-all fallback |
| **Looping** | `for` | Traverse finite ranges/sequences | Executes once per item in sequence |
| **Looping** | `while` | Maintain continuous repetition | Loops until conditional check returns `false` |
| **Loop Control** | `break` | Force instant loop cancellation | Aborts loop immediately |
| **Loop Control** | `continue` | Skip remaining active instructions | Jumps immediately to next iteration cycle |
| **Loop Control** | `pass` | Maintain valid empty code blocks | Does nothing (Null operation placeholder) |
