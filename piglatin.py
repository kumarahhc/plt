
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase if phrase else "nil"

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "nil":
            return "nil"
        elif self.phrase.endswith('y'):
            return self.phrase + 'nqy'
        elif self.phrase[-1] in 'aeiou':
            return self.phrase + 'yay'
        else:
            return self.phrase

