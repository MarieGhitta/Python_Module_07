from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack_points: int,
                 health: int, rating: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_points = attack_points
        self.health = health
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        return {"attacker": self.name, "target": target,
                "damage": self.attack_points}

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = 2
        damage_taken = max(0, incoming_damage - damage_blocked)

        self.health -= damage_taken
        still_alive = self.health > 0

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": still_alive
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_points, "health": self.health}

    def calculate_rating(self) -> int:
        if self.wins > self.losses:
            self.rating += 16
        elif self.wins < self.losses:
            self.rating -= 16
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "attack": self.attack_points,
            "health": self.health,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
