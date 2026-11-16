class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #default dict used to create key if value not in dictionary

        for s in strs: #go through the list of words
            count = [0]*26 # create complete list for the 26 possible letters in the abc

            for c in s: # go through each letter in the word
                count[ord(c)-ord("a")] += 1 # calculate the index for each letter and then add 1 
            
            res[tuple(count)].append(s) # add the count to the dictionary and to is list add the string that matched the count 
        return list(res.values()) #we can simply return the values of the dictionary as they are a list of the words with the same counts