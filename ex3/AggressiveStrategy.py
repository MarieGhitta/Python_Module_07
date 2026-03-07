from ex0.Card import Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list[Card], battlefield) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        for card in hand:
            if card.cost <= 3:
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += 4
        targets_attacked = ["Enemy Player"]
        resume = {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }
        return resume

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
