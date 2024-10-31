
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase if phrase else "nil"

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "nil":
            return "nil"
        elif self.phrase.endswith('y'):
            return self.phrase + 'nay'
        elif self.phrase[0] in 'aeiou':
            if self.phrase[-1] in 'aeiou':
                return self.phrase + 'yay'
            else:
                return self.phrase + 'ay'
        else:
            vowels = 'aeiou'
            first_no_of_consonant= 0
            for i, char in enumerate(self.phrase):
                if char not in vowels:
                    first_no_of_consonant +=1
                else:
                    break
            if first_no_of_consonant==1:
                # Move the first consonant to the end and append 'ay'
                return self.phrase[1:] + self.phrase[0] + 'ay'
            elif first_no_of_consonant==2:
                # Move the first 2 consonant to the end and append 'ay'
                return self.phrase[2:] + self.phrase[0:2] + 'ay'



