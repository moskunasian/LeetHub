class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        # iterate over plants
        # if we dont have enough water, simulate retrieving more (2 * i - 1) and water 
        # if we do have enough, just water and adjust steps 
        
        totalSteps = 0
        water = capacity
        for i in range(len(plants)):
            if water < plants[i]:
                totalSteps += (2 * i + 1)
                water = capacity - plants[i]
            else:
                totalSteps += 1
                water -= plants[i]
        return totalSteps
        