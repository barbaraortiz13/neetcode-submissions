class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS= "".join(c.lower() for c in s if c.isalnum())
            
        current = 0
        biggest = len(newS)-1
        while (current<(len(newS)/2)):
            if (newS[current]!= newS[biggest]):
                return False
            else:
                current += 1
                biggest -= 1
        return True


