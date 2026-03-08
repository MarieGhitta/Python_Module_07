from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    try:
        platform = TournamentPlatform()
        fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 1200)
        ice_wizard = TournamentCard("Ice Wizard", 4, "Rare", 5, 6, 1150)
        dragon_id = platform.register_card(fire_dragon)
        wizard_id = platform.register_card(ice_wizard)
        print("\n=== DataDeck Tournament Platform ===\n")
        print("Registering Tournament Cards...\n")
        print(f"{fire_dragon.name} (ID: {dragon_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {fire_dragon.rating}")
        print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}\n")
        print(f"{ice_wizard.name} (ID: {wizard_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {ice_wizard.rating}")
        print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}\n")
        print("Creating tournament match...")
        match_result = platform.create_match(dragon_id, wizard_id)
        print("Match result:", match_result)
        print("\nTournament Leaderboard:")
        leaderboard = platform.get_leaderboard()
        for i, card in enumerate(leaderboard, start=1):
            print(f"{i}. {card["name"]} - Rating: {card["rating"]}"
                  f"({card["wins"]}-{card["losses"]})")
        print("\nPlatform Report:")
        print(platform.generate_tournament_report())
        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
