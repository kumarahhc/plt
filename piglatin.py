
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
            # Move the first consonant to the end and append 'ay'
            return self.phrase[1:] + self.phrase[0] + 'ay'



