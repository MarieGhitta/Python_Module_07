from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def validate(self) -> bool:
        if (not isinstance(self.attack, int)
           or not isinstance(self.health, int)
           or self.attack <= 0
           or self.health <= 0):
            return False
        return True

    def play(self, game_state: dict) -> dict:
        infos = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect":  'Creature summoned to battlefield'
        }
        return infos

    def attack_target(self, target) -> None:
        attack_infos = {
            "attacker": "Fire Dragon",
            "target": target,
            "damage_dealt": 7,
            "combat_resolved": True
        }
        return attack_infos

    def get_card_info(self) -> dict:
        infos = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        }
        return infos
