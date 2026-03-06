from ex0.Creature import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendery", 7, 5)
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(6)}")
    game_state = {
        'ctruc': 'bizarre'
    }
    print(f"Play result: {fire_dragon.play(game_state)}")
    print("\nFire Dragon attacks Goblin Warrior:")
    target = "Goblin Warrior"
    print(f"Attack_result: {fire_dragon.attack_target(target)}")
    print("\nTesting insufficient mana(3 available)")
    print(f"Playable: {fire_dragon.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")

if __name__ == '__main__':
    main()