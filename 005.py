# -*- coding: utf-8 -*-

class Solution:
    def replaceSpace1(self, s):
        if not isinstance(s, str):
            return

        temp = ''
        for c in s:
            if c == ' ':
                temp += '%20'
            else:
                temp += c
        return temp

    def replaceSpace2(self, s):
        if not isinstance(s, str):
            return

        return s.replace(' ', '%20')

    def replaceSpace3(self, s):
        if not isinstance(s, str):
            return

        num_space = 0
        for c in s:
            if c == ' ':
                num_space += 1

        len_of_newstr = len(s) + 2 * num_space
        newstr = [None] * len_of_newstr
        old_idx = len(s) - 1
        new_idx = len_of_newstr - 1
        while old_idx >= 0 and new_idx >= old_idx:
            if s[old_idx] != ' ':
                newstr[new_idx] = s[old_idx]
                new_idx -= 1
                old_idx -= 1
            else:
                newstr[(new_idx-2):(new_idx+1)] = ['%', '2', '0']
                old_idx -= 1
                new_idx -= 3

        return ''.join(newstr)


# test case
s1 = 'happy new year'
s2 = ' happy new year'
s3 = 'happy new year '
s4 = 'happynewyear'

s = Solution()
print(s.replaceSpace3(s1))
print(s.replaceSpace3(s2))
print(s.replaceSpace3(s3))
print(s.replaceSpace3(s4))
