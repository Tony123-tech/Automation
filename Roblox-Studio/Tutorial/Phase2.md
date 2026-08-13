# Luau Foundations: Variables, Control Flow, Functions, & Tables

## 1. Log Printing & Variable Scoping
* **Output Logging**: The global `print()` command writes strings or variables directly into the Studio Output console.
* **Local Initialization**: Prefixing declarations with the `local` keyword restricts variable data visibility exclusively to the active script or code block.
* **Global Variables**: Omitting `local` registers data globally across the environment runtime, which risks namespace clutter.

```lua
print("Initializing system...")
local playerScore = 0
local playerName = "GuestPlayer"
local isVIP = false
```

## 2. Operators & Assignment Logic
* **Mathematical Operators**: Employs standard addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulus (`%`), and exponentiation (`^`) markers.
* **Relational Operators**: Validates comparisons using equality (`==`), inequality (`~=`), greater than (`>`), and less than (`<`) tokens.
* **Logical Connectives**: Chains conditional assessments together using written keywords: `and`, `or`, `not`.
* **Compound Math Assignments**: Modifies variable states directly using arithmetic shortcuts (`+=`, `-=`, `*=`, `/=`).

```lua
local totalItems = 5 + 3
local hasKey = true
local accessGranted = (totalItems > 5) and hasKey

playerScore += 10
local isNotEqual = (playerScore ~= 100)
```

## 3. Conditional Statements & Routing
* **`if` Statement**: Processes nested operations if the initial expression evaluates to `true`.
* **`elseif` Statement**: Evaluates alternate conditions sequentially if the preceding paths returned `false`.
* **`else` Statement**: Acts as the final catch-all branch when all prior validation blocks fail.
* **`end` Token**: Explicitly marks the terminal boundary of the conditional block structure.

```lua
if playerScore >= 100 then
	print("Grand Winner!")
elseif playerScore >= 50 then
	print("Runner Up!")
else
	print("Try Again!")
end
```

## 4. Looping & Iteration Structures
* **Numeric `for` Loop**: Executes code repeatedly across a fixed number range based on a start value, an end value, and an optional step interval.
* **Conditional `while` Loop**: Continuously repeats internal code operations until its tracking condition breaks and returns `false`.
* **Loop Yields**: Implements `task.wait()` inside continuous `while` blocks to prevent the game engine from freezing.

```lua
for i = 1, 5, 1 do
	print("Iteration step: " .. i)
end

local countdown = 3
while countdown > 0 do
	print("Time left: " .. countdown)
	countdown -= 1
	task.wait(1)
end
```

## 5. Custom Functions & Return Rules
* **Function Structure**: Declared using the `local function` keyword string followed by unique parameter names wrapped in parentheses.
* **Argument Passing**: Passes contextual data directly into localized script variables inside the function scope when called.
* **Return Values**: Uses the `return` keyword to instantly halt the function execution and pass calculated data back to the calling block.

```lua
local function calculateTax(price, taxRate)
	local finalTax = price * taxRate
	return finalTax
end

local shirtTax = calculateTax(20, 0.05)
print("Tax amount: \$" .. shirtTax) -- Output: Tax amount: \$1
```

## 6. Data Storage: Arrays & Dictionaries
* **Arrays**: Ordered list configurations defined with curly brackets `{}` that index items sequentially starting strictly at `1`.
* **Dictionaries**: Key-value data collections matching clear reference string names to explicit values instead of numbers.
* **Size Operator**: The hash operator (`#`) quickly calculates the total index length of basic sequential arrays.
* **Table Manipulation**: Use `table.insert()` to add elements and `table.remove()` to drop values from an array.

```lua
-- Array Definition
local toolsInventory = {"Sword", "Shield", "Potion"}
print("Total items: " .. #toolsInventory) -- Output: 3
print("First item: " .. toolsInventory[1]) -- Output: Sword

-- Modifying Arrays
table.insert(toolsInventory, "Bow") -- Adds to the end
table.remove(toolsInventory, 3) -- Removes "Potion"

-- Dictionary Definition
local playerStats = {
	Coins = 1500,
	Level = 12,
	Class = "Warrior"
}
print("Player level: " .. playerStats.Level) -- Output: 12

-- Updating Dictionaries
playerStats.Coins += 500
playerStats["Weapon"] = "Iron Blade" -- Dynamic key creation
```
