from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex2.EliteCard import EliteCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None
                        ) -> Card:
        return EliteCard("Fire Dragon", 5, "Legendary", 7, 5,)

    def create_spell(self, name_or_power: str | int | None = None
                     ) -> Card:
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(self, name_or_power: str | int | None = None
                        ) -> Card:
        return ArtifactCard("Mana Crystal", 2, "Common", 5,
                            "Permanent: +1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        if size >= 1:
            deck.append(EliteCard("Fire Dragon", 5, "Legendary", 7, 5, 3))
        if size >= 2:
            deck.append(EliteCard("Goblin Warrior", 2, "Common", 2, 2, 2))
        if size >= 3:
            deck.append(SpellCard("Lightning Bolt", 3, "Rare", "damage"))
        return {"deck": deck}

    def get_supported_types(self) -> dict:
        types = {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
        return types
