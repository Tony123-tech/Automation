# Production & Polish: Optimization, DataStores, Monetization, & Badges

## 1. Global Data Persistence (DataStoreService)
* **Persistent Engine Storage**: Saves critical state markers safely to cloud servers across separate gameplay instances.
* **Protected Execution**: Wrap calls in `pcall()` functions to capture external network faults without completely crashing your primary scripts.

```lua
local DataStoreService = game:GetService("DataStoreService")
local PlayerGoldStore = DataStoreService:GetDataStore("PlayerGoldSaveSystem_v1")
local Players = game:GetService("Players")

-- Loading Data
Players.PlayerAdded:Connect(function(player)
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = "leaderstats"
	leaderstats.Parent = player
	
	local gold = Instance.new("IntValue")
	gold.Name = "Gold"
	gold.Value = 0
	gold.Parent = leaderstats
	
	local dataKey = "Player_" .. player.UserId
	local success, savedData = pcall(function()
		return PlayerGoldStore:GetAsync(dataKey)
	end)
	
	if success and savedData then
		gold.Value = savedData
	end
end)

-- Saving Data
Players.PlayerRemoving:Connect(function(player)
	local dataKey = "Player_" .. player.UserId
	if player:FindFirstChild("leaderstats") then
		local goldValue = player.leaderstats.Gold.Value
		
		pcall(function()
			PlayerGoldStore:SetAsync(dataKey, goldValue)
		end)
	end
end)
```

## 2. Smooth Object Animation (TweenService)
* **Tween Engines**: Interpolates property changes over time for fluid visual motions (e.g., doors sliding, frames fading).
* **TweenInfo Package**: Takes configurations detailing execution time duration, easing styles, and movement directions.

```lua
local TweenService = game:GetService("TweenService")
local movingPart = game.Workspace:WaitForChild("SlidingDoor")

local targetProperties = {
	Position = Vector3.new(10, 5, 20),
	Transparency = 0.5
}

local tweenSettings = TweenInfo.new(
	3, -- Seconds duration
	Enum.EasingStyle.Quad,
	Enum.EasingDirection.Out,
	0, -- Repeat count
	false -- Reverses?
)

local movementTween = TweenService:Create(movingPart, tweenSettings, targetProperties)
movementTween:Play()
```

## 3. Modular Programming Frameworks (ModuleScripts)
* **Single Evaluation Principle**: Code blocks within a ModuleScript execute exactly once per architecture boundary and return a static table object.
* **Don't Repeat Yourself (DRY)**: Centralize universal game configurations or reusable calculations so you only have to write them once.

```lua
-- ModuleScript placed in ReplicatedStorage named "CombatMath"
local CombatMath = {}

function CombatMath.CalculateCriticalDamage(baseDamage, critMultiplier)
	local roll = math.random(1, 100)
	if roll > 80 then -- 20% Critical Chance
		return baseDamage * critMultiplier
	end
	return baseDamage
end

return CombatMath
```

## 4. Game Optimization & Lifecycle Cleanup
* **Memory Management**: Unused event connections accumulate over time. Always store connections in variables and drop them using `:Disconnect()` when an item is destroyed.
* **Garbage Collection**: Avoid memory leaks by cleaning up dynamically generated instances using `:Destroy()` instead of just setting their parent to nil.

```lua
local part = Instance.new("Part")
part.Parent = workspace

local connection
connection = part.Touched:Connect(function()
	print("Part touched!")
	-- Clean up connection and instance
	connection:Disconnect()
	part:Destroy()
end)
```

## 5. Monetization & Developer Products
* **Game Passes**: One-time purchases created via the Creator Dashboard that grant persistent, lifetime perks (e.g., Double Speed).
* **Developer Products**: Repeatable microtransactions purchased multiple times (e.g., buying 100 extra Gold).

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local GOLD_PRODUCT_ID = 0000000 -- Replace with your Developer Product ID

-- Handle Purchase Success
local function processReceipt(receiptInfo)
	local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
	if player then
		local leaderstats = player:FindFirstChild("leaderstats")
		if leaderstats then
			local gold = leaderstats:FindFirstChild("Gold")
			if gold then
				gold.Value += 500 -- Award gold reward
				return Enum.ProductPurchaseDecision.PurchaseGranted
			end
		end
	end
	return Enum.ProductPurchaseDecision.NotProcessedYet
end

MarketplaceService.ProcessReceipt = processReceipt
```

## 6. Retention, Engagement, & Badges
* **Social Proof**: Awarding custom Badges drives long-term play session loops, marks major profile accomplishments, and displays milestones on a player's Roblox profile.
* **Engine Callouts**: Award badges using `BadgeService:AwardBadge()`. Always check if the asset is valid and if the user already owns it.

```lua
local BadgeService = game:GetService("BadgeService")
local Players = game:GetService("Players")

local WELCOME_BADGE_ID = 00000000 -- Replace with your specific Badge ID

local function onPlayerAdded(player)
	-- Wrap network request in a pcall for safety
	local success, hasBadge = pcall(function()
		return BadgeService:UserHasBadgeAsync(player.UserId, WELCOME_BADGE_ID)
	end)
	
	if success and not hasBadge then
		-- Award badge securely on the server
		local awardSuccess, result = pcall(function()
			BadgeService:AwardBadge(player.UserId, WELCOME_BADGE_ID)
		end)
		
		if awardSuccess then
			print("Successfully awarded Welcome Badge to " .. player.Name)
		end
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```
