class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        intersection=nums1.intersection(nums2)
        return list(intersection)


sol=Solution().intersection([4,9,5],[9,4,9,8,4])
print(sol)