# Environment Interaction: Workspace Manipulation, Events, & Vector3

## 1. Game Hierarchy Navigation
* **Data Model Root**: The `game` keyword acts as the absolute parent boundary housing all background microservices.
* **The Dot Operator**: Dots (`.`) step down into child folders or instances nested inside the Explorer tree.
* **Safe Instance Finding**: Using `:WaitForChild("PartName")` halts script execution safely until an item replicates to prevent errors.

```lua
local Workspace = game:GetService("Workspace")
local lobbyModel = Workspace:WaitForChild("Lobby")
local basePlate = Workspace.Baseplate
```

## 2. Live Property Manipulation
* **Type Validation**: Modified properties must strictly match their intended data type formats (e.g., Vector3, Color3).
* **Color3 Allocations**: Colors are modified using `Color3.fromRGB(r, g, b)` (0-255 scale) or `Color3.fromHSV(h, s, v)`.
* **Vector3 Allocations**: Positional shifts and dimensions use structural vectors tracking `Vector3.new(X, Y, Z)`.

```lua
local neonPart = Workspace:WaitForChild("NeonPart")

neonPart.Transparency = 0.5
neonPart.Material = Enum.Material.Neon
neonPart.Color = Color3.fromRGB(255, 85, 0) -- Bright Orange
neonPart.Size = Vector3.new(10, 2, 10)
```

## 3. Events, Functions, & Connections
* **Event Listeners**: Capitalized built-in signals (like `.Touched`) flag unique real-time engine changes.
* **Connecting Logic**: The `:Connect()` method links active engine signals directly to specific executable callback functions.
* **Passed Arguments**: Signals pass default context variables (such as the object that touched a part) to event functions.

```lua
local killPart = Workspace:WaitForChild("LavaPart")

local function onPartTouched(otherPart)
	local character = otherPart.Parent
	local humanoid = character:FindFirstChildOfClass("Humanoid")
	
	-- If it has a Humanoid, it is a player/NPC
	if humanoid then
		humanoid.Health = 0
	end
end

killPart.Touched:Connect(onPartTouched)
```

## 4. Dynamic Generation (Instance.new)
* **Instance Factories**: Running `Instance.new("ClassName")` creates completely blank objects natively via script memory.
* **Parent Binding**: Newly created parts will never render visually until their `.Parent` property is explicitly tied to the `Workspace`.

```lua
local function spawnFallingSphere()
	local ball = Instance.new("Part")
	ball.Name = "DroppingSphere"
	ball.Shape = Enum.PartType.Ball
	ball.Size = Vector3.new(3, 3, 3)
	ball.Position = Vector3.new(0, 50, 0)
	ball.Color = Color3.fromRGB(0, 255, 120)
	
	ball.Anchored = false
	ball.CanCollide = true
	
	-- Render inside the world
	ball.Parent = Workspace
end

task.wait(5)
spawnFallingSphere()
```
