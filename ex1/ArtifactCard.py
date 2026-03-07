from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        infos = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.durability}: {self.effect}"
        }
        return infos

    def activate_ability(self) -> dict:
        ability = {
            "artifact": self.name,
            "effect": self.effect,
            "durability": self.durability
        }
        return ability
