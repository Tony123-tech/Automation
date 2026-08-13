# Master the Editor: Roblox Studio UI, Parts, & Physics

## 1. Navigating the Roblox Studio UI
* **Explorer Window**: Manage game hierarchy, services, and objects.
* **Properties Window**: Modify object appearances, attributes, and behaviors.
* **Toolbox**: Access community models, audio, images, and meshes.
* **Output Log**: Debug code and monitor runtime errors or print statements.
* **Command Bar**: Execute Luau code instantly without running the game.

## 2. Working with Parts
* **Creation**: Instantiate Blocks, Spheres, Wedges, and Cylinders.
* **Transformation Tools**: Master Select (1), Move (2), Scale (3), and Rotate (4).
* **Materials & Colors**: Change surfaces using SmoothPlastic, Neon, or Custom Materials.
* **Grouping**: Combine multiple parts into a single **Model** (`Ctrl + G`).

### Automating Part Generation (Luau Script)
Paste this script into a `Script` object inside `Workspace` to automatically spawn a tower of physical parts:

```lua
-- Services
local Workspace = game:GetService("Workspace")

-- Configuration
local SPAWN_COUNT = 10
local START_HEIGHT = 5

-- Spawn Loop
for i = 1, SPAWN_COUNT do
	local newPart = Instance.new("Part")
	newPart.Name = "AutoSpawnedPart_" .. i
	newPart.Size = Vector3.new(4, 4, 4)
	newPart.Position = Vector3.new(0, START_HEIGHT + (i * 5), 0)
	newPart.Color = Color3.fromHSV(i / SPAWN_COUNT, 1, 1) -- Rainbow colors
	newPart.Material = Enum.Material.Neon
	
	-- Physics Setup
	newPart.Anchored = false
	newPart.CanCollide = true
	
	-- Parent to Workspace to render it
	newPart.Parent = Workspace
	task.wait(0.2) -- Small delay between spawns
end
```

## 3. Physics & Constraints
* **Anchoring**: Toggle `Anchored` to keep parts static in mid-air.
* **CanCollide**: Toggle physical collisions between players and objects.
* **Mass & Gravity**: Adjust custom physical properties via `CustomPhysicalProperties`.
* **Constraints**: Connect parts using Hinges, Springs, Ropes, and Welds.

## 4. Terrain Editing Tools
* **Generate Tool**: Create procedurally generated landscapes with mountains, water, and hills.
* **Add / Subtract**: Manually paint voxel material onto the map or carve chunks out of it.
* **Grow / Erode**: Smoothly expand terrain surfaces or wear them down for realistic cliffs.
* **Smooth / Flatten**: Level out uneven ground to create perfect building foundations.
* **Paint Tool**: Swap terrain textures (e.g., changing Grass to Rock) without changing the shape.

## 5. Essential Roblox Services (game:GetService)
Every Roblox developer must know these foundational built-in singletons to handle game logic, networking, and data storage.

```lua
-- Core Environment & Hierarchy
local Workspace = game:GetService("Workspace") -- Handles 3D world physics, parts, and terrain.
local Players = game:GetService("Players") -- Manages online users, character spawning, and account data.

-- Networking & State Management
local ReplicatedStorage = game:GetService("ReplicatedStorage") -- Shared assets/modules accessible by both Server and Client.
local ServerStorage = game:GetService("ServerStorage") -- Secure server-side assets completely hidden from clients/exploiters.
local ReplicatedFirst = game:GetService("ReplicatedFirst") -- Loads first; perfect for custom loading screens and initial client scripts.
local ServerScriptService = game:GetService("ServerScriptService") -- House for secure server-side scripts.

-- User Interface & Input
local StarterGui = game:GetService("StarterGui") -- Clones screen UI elements into a player's interface when they spawn.
local UserInputService = game:GetService("UserInputService") -- Detects keystrokes, mouse movement, touches, and controller inputs (Client-only).
local ContextActionService = game:GetService("ContextActionService") -- Binds contextual actions to keys across multiple devices easily.

-- Cloud Services & Data
local DataStoreService = game:GetService("DataStoreService") -- Saves player data permanently (leaderstats, inventories, cash) across game sessions.
local MemoryStoreService = game:GetService("MemoryStoreService") -- High-throughput, low-latency cross-server storage for matchmaker or transient data.
local HttpService = game:GetService("HttpService") -- Connects your game to external web APIs (JSON parsing, fetching data from websites).
local MessagingService = game:GetService("MessagingService") -- Broadcasts text data live across different running servers of the same game.

-- Gameplay Systems & Engine Utilities
local TweenService = game:GetService("TweenService") -- Animates smoothly moving parts, changing colors, or fading UI gradients.
local SoundService = game:GetService("SoundService") -- Coordinates 3D environmental sound effects and background ambient tracks.
local RunService = game:GetService("RunService") -- Manages frame-by-frame loops (`Heartbeat`, `RenderStepped`) and identifies environment context (Studio vs Live game).
local PolicyService = game:GetService("PolicyService") -- Ensures player monetization compliance with global regional laws (like paid random items restriction).
```
