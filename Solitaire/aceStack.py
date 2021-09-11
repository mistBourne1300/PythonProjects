from SolitaireStack import SolitaireStack

class AceStack(SolitaireStack):
    def __str__(self):
        return str(self.faceUpStack[-1])