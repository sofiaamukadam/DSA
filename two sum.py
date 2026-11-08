def twoSum(self, nums, target):
  nums=[1,12,56,78]
    target:12
    for i in range (len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            return[i,j]        