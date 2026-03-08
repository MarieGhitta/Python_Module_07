from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        name = card.name.split()
        ID = f"{name[-1].lower()}_001"
        self.cards[ID] = card
        return ID

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        if card1.attack_points >= card2.attack_points:
            winner = card1
            winner_id = card1_id
            loser = card2
            loser_id = card2_id
        elif card2.attack_points > card1.attack_points:
            winner = card2
            winner_id = card2_id
            loser = card1
            loser_id = card1_id
        winner.update_wins(1)
        loser.update_losses(1)
        winner.calculate_rating()
        loser.calculate_rating()
        self.matches_played += 1
        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_rating(self, card):
        return card.rating

    def get_leaderboard(self) -> list:
        sorted_cards: list[TournamentCard] = sorted(self.cards.values(),
                                                    key=self.get_rating,
                                                    reverse=True)
        return [{
            "name": card.name,
            "rating": card.rating,
            "wins": card.wins,
            "losses": card.losses
        } for card in sorted_cards]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        avg_rating = sum(card.rating for card in self.cards.values()
                         ) // total_cards
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
