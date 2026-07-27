-- 1. Sit with ProximityPrompt
local seat = script.Parent
local proximityPrompt = seat:FindFirstChildOfClass("ProximityPrompt")

-- Function that triggers when a player interacts with the prompt
local function onPromptTriggered(player)
	local character = player.Character
	if not character then return end
	
	local humanoid = character:FindFirstChildOfClass("Humanoid")
	
	-- Check if the humanoid exists and the seat is empty
	if humanoid and not seat.Occupant then
		seat:Sit(humanoid)
	end
end

-- Connect the function to the prompt's Triggered event
proximityPrompt.Triggered:Connect(onPromptTriggered)
