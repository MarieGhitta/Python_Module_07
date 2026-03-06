from ex0.Card import Card
from ex0.Creature import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

def main():
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendery", 7, 5)
    lightning_bolt = SpellCard("Lightning Bolt", 3, "commun",
                               "Deal 3 damage to target")
    mana_crystal = ArtifactCard("Mana Crystal", 4, "rare", "Permanent",
                                "+1 mana per turn")
    deck = Deck()
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)
   
    print(deck.get_deck_stats())
    mana_crystal.cost = 2

    print("\nDrawing and playing cards")
    game_stat = {"c'est": "débile"}
    while deck.cards:
        card = deck.draw_card()

        if isinstance(card, SpellCard):
            card_type = "Spell"
        elif isinstance(card, ArtifactCard):
            card_type = "Artifact"
        else:
            card_type = "Creature"

        print(f"\nDrew: {card.name} ({card_type})")
        print("Play result:", card.play(game_stat))

        print("\nPolymorphism in action: Same interface,"
              "different card behaviors!")


if __name__ == '__main__':
    main()