import itertools

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        all_values = list(itertools.chain.from_iterable(mat))
        if len(all_values) / r == c:
            all_values = iter(all_values)
            test = [list(itertools.islice(all_values, elem))
                    for elem in [c] * r]
            return test
        else:
            return mat

test = Solution()
print(test.matrixReshape([[1,2],[3,4]],4,1))