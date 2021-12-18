class Rule:
    def __init__(self):
        pass

    def get_winners(self, participants, move):
        half = (len(participants) - 1) // 2
        winners = participants[move+1:move+1+half]
        if len(winners) < half:
            [winners.append(i) for i in participants[1:1+half-len(winners)]]
        return winners
