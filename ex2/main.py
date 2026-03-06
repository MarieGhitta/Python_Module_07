from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    arcane_warrior = EliteCard("Arcane Warrior", 5, "Epic", 5, 10, 8)
    print("- Card:", ["play", "get_card_info", "is_playable"])
    print("- Combatable:", ["attack", "defend", "get_combat_stats"])
    print("- Magical:", ["cast_spell", "channel_mana", "get_magic_stats"])
    print("\nPlaying Arcane Warrior (Elite Card)\n")
    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}")
    print("\nMagic phase:")
    enemies = ['Enemy1', 'Enemy2']
    print(f"Spell cast: {arcane_warrior.cast_spell('Fireball', enemies)}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()