from ex0.Card import Card
from ex0.Creature import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import shuffle


class Deck():
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            drawn_card = self.cards.pop(0)
            return drawn_card
        return None

    def get_deck_stats(self) -> dict:
        count_creature = 0
        count_spell = 0
        count_artifact = 0
        for card in self.cards:
            if isinstance(card, CreatureCard):
                count_creature += 1
            elif isinstance(card, SpellCard):
                count_spell += 1
            elif isinstance(card, ArtifactCard):
                count_artifact += 1        
        total_cost = sum(card.cost for card in self.cards)
        if self.cards:
            avg_cost = total_cost / len(self.cards)
        else:
            avg_cost = 0
        deck_stats = {
            "total_cards": len(self.cards),
            "creatures": count_creature,
            "spells": count_spell,
            "artifacts": count_artifact,
            "avg_cost": avg_cost
        }
        return deck_stats
