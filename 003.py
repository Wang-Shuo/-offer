# -*- coding:utf-8 -*-
class Solution1:
    def duplicate(self, numbers, duplication):
        if numbers is None or len(numbers) <= 0:
            return False
        for num in numbers:
            if num < 0 or num > len(numbers) - 1:
                return False

        num_set = set()
        for num in numbers:
            if num in num_set:
                duplication[0] = num
                return True
            else:
                num_set.add(num)

        return False


class Solution2:
    def duplicate(self, numbers, duplication):
        if numbers is None or len(numbers) <= 0:
            return False
        for num in numbers:
            if num < 0 or num > len(numbers) - 1:
                return False

        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    idx = numbers[i]
                    numbers[i] = numbers[idx]
                    numbers[idx] = idx

        return False


class Solution3:
    def duplicate(self, numbers):
        if numbers is None or len(numbers) <= 0:
            return -1
        for num in numbers:
            if num < 1 or num > len(numbers) - 1:
                return -1

        start = 1
        end = len(numbers) - 1
        while end >= start:
            middle = ((end - start) >> 1) + start
            count = self.countRange(numbers, start, middle)
            if end == start:
                if count > 1:
                    return start
                else:
                    break

            if count > (middle - start + 1):
                end = middle
            else:
                start = middle + 1

        return -1


    def countRange(self, numbers, start, end):
        count = 0
        for num in numbers:
            if num >= start and num <= end:
                count += 1
        return count

# test
test1 = [2, 3, 1, 0, 4, 2, 1]
test2 = [1, 2, 3, 4, 6, 8, 9]
test3 = [1, 2, 3]
test4 = [2, 3, 5, 4, 3, 2, 6, 7]
#s = Solution2()
#duplication = [0]
#print(s.duplicate(test1, duplication))

s1 = Solution3()
print(s1.duplicate(test4))
