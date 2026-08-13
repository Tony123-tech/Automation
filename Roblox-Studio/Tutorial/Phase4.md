# Game Architecture: Client-Server (Remotes), Player Data, & GUI

## 1. The Network Boundary (Client vs. Server)
* **The Server**: Runs one global secure instance in the cloud. It manages authorization, backend logic, and overall game data persistence.
* **The Client**: Runs independently on individual local devices. It renders graphic views, handles user inputs, and displays custom user interfaces.
* **Replication Rule**: Changes made inside local client scripts do not automatically copy over to the server, protecting against exploits.

## 2. Remote Events & Remote Functions
* **RemoteEvent (`:FireServer()` / `.OnServerEvent`)**: A one-way communication bridge used to send operational alerts across the client-server dividing line.
* **RemoteFunction (`:InvokeServer()` / `.OnServerInvoke`)**: A two-way communication bridge that requests data from the opposite side and forces the code to wait for a returned response.
* **Security Notice**: Always locate Remote targets safely within the `ReplicatedStorage` engine container so both sides can see them.

### Server Script (`ServerScriptService`)
```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local GivePointsEvent = ReplicatedStorage:WaitForChild("GivePointsEvent")

local function onPointsRequested(player, amount)
	-- Always validate values on the server to prevent cheating!
	if amount <= 100 then
		local leaderstats = player:FindFirstChild("leaderstats")
		if leaderstats then
			local points = leaderstats:FindFirstChild("Points")
			if points then
				points.Value += amount
			end
		end
	end
end

GivePointsEvent.OnServerEvent:Connect(onPointsRequested)
```

### Client LocalScript (Inside a Screen Gui Button)
```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local GivePointsEvent = ReplicatedStorage:WaitForChild("GivePointsEvent")

local clickButton = script.Parent

local function onClicked()
	-- Tell the server to award 50 points
	GivePointsEvent:FireServer(50)
end

clickButton.MouseButton1Click:Connect(onClicked)
```

## 3. Server-Side Player Leaderboards
* **`leaderstats` Rule**: Creating a folder named exactly `"leaderstats"` inside a `Player` instance tells Roblox to render a top-right leaderboard interface.
* **Value Objects**: IntValue, NumberValue, and StringValue objects house the exact stat totals inside the folder configuration.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = "leaderstats"
	leaderstats.Parent = player
	
	local points = Instance.new("IntValue")
	points.Name = "Points"
	points.Value = 0
	points.Parent = leaderstats
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

## 4. User Interfaces (GUI)
* **StarterGui**: The layout template workspace. All structures placed inside clone directly into the player's personal local `PlayerGui` space upon spawning.
* **Core Elements**: Use `ScreenGui` as a root canvas, `Frame` objects to group sections, and `TextButton`/`TextBox` interfaces for user interaction.
* **Layout Design**: Use scale metrics (`{0.5, 0}`) instead of fixed offset pixels (`{0, 500}`) to keep your design responsive across mobile devices and monitors.
