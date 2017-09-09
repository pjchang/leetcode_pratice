class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):

            if target-nums[i] in dic:
                
                return [dic[target-nums[i]],i]
            else:
                dic[nums[i]]=i
        return []

if __name__ == '__main__':
    print Solution().twoSum((2, 7, 11, 15), 9)
    
            
