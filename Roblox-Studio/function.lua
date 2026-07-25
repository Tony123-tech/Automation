-- 1. Sit with ProximityPrompt 

local seat = script.Parent.Parent -- Adjust path to target the Seat object
local proximityPrompt = script.Parent

proximityPrompt.Triggered:Connect(function(player)
    local character = player.Character
    if character then
        local humanoid = character:FindFirstChildOfClass("Humanoid")
        
        -- Double-check that a humanoid exists and the seat isn't already occupied
        if humanoid and not seat.Occupant then
            seat:Sit(humanoid) -- Snaps the character perfectly into the seat object
        end
    end
end)

seat:GetPropertyChangedSignal("Occupant"):Connect(function()
    if seat.Occupant then
        proximityPrompt.Enabled = false -- Hide prompt if seat is full
    else
        proximityPrompt.Enabled = true -- Show prompt if seat is empty
    end
end)

-- 2. Pick a Item 
local tool = script.Parent -- Put this script directly inside the Tool

local function onTouch(otherPart)
	-- Check if whatever touched the item belongs to a human player
	local character = otherPart.Parent
	local humanoid = character:FindFirstChildOfClass("Humanoid")
	local player = game.Players:GetPlayerFromCharacter(character)
	
	-- If it is a real player and they aren't dead, put it in their Backpack
	if humanoid and player and humanoid.Health > 0 then
		tool.Parent = player.Backpack
		print(player.Name .. " picked up the item!")
	end
end

-- Connect the function to the handle's touch event
tool.Handle.Touched:Connect(onTouch)
