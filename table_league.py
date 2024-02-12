from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
     
    def player_rank(self, rank):
        rank_index = rank - 1
        return self.get_sorted_players()[rank_index]

    def get_sorted_players(self):
        # score_bucket = (score, games_played)
        score_bucket = None
        score_buckets = []
        # rankings item = score_bucket : [arr of players]
        rankings = {}
        score = 0
        games_played = 0

        for player in self.standings:
            score = self.standings[player]['score']
            games_played = self.standings[player]['games_played']

            score_bucket = (score, games_played)

            if score_bucket not in rankings:
                rankings[score_bucket] = []
                score_buckets.append(score_bucket)

            rankings[score_bucket].append(player)

        score_buckets.sort(key=lambda score_bucket : (score_bucket[0], -score_bucket[1]))

        for score_bucket in score_buckets:
            rankings[score_bucket].sort(key=lambda player : list(self.standings).index(player), reverse=True)

        sorted_players = []

        for score_bucket in score_buckets:
            sorted_players.extend(rankings[score_bucket])

        sorted_players.reverse()

        return sorted_players

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))