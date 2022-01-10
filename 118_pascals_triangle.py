class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for row in range(1, numRows + 1):
            row_contents = []
            value = 1
            for element in range(1, row + 1):
                row_contents.append(value)
                value = value * (row - element) / element
            result.append(row_contents)

        return result

# solution modified from geeks for geeks article on printing pascals triangle
# time complexity is O(m) where m is sum(range(1,numRows+1))