class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                li.append(i)
        return li





sol=Solution().intersect([4,9,5],[9,4,9,8,4])
print(sol)
