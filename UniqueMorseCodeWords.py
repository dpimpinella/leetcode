class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        dictionary = dict(zip(letters, morse))

        count = 0
        morseWords = []

        for word in words:
            tempWord = ''

            for letter in word:
                tempWord += dictionary[letter]            

            if tempWord not in morseWords:
                morseWords.append(tempWord)
                count += 1           

        print(count)
        return count


          
run = Solution().uniqueMorseRepresentations(['digs', 'begs', 'test', 'word', 'word', 'another', 'another'])