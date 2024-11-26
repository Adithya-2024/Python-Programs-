class Solution:#program to solve two sum # class in python is to solve the whole in a single modularity 
    def twoSum(self, nums: List[int], target: int) -> List[int]:#here nums:List[int]- is a parameter which excepts the list 
        for i in range(len(nums)):                  #->List[int] - is a return type 
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    return [i,j]