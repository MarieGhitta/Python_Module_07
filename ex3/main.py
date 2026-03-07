from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print("\nSimulating aggressive turn...")
    new_hand = factory.create_themed_deck(3)
    hand = new_hand["deck"]
    print("Hand: "
          f"[{', '.join(f'{card.name} ({card.cost})' for card in hand)}]")
    print("\nTurn execution:")
    print(f"strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {engine.simulate_turn()}")
    print("\nGame Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: Maximum "
          "flexibility achieved!")


if __name__ == '__main__':
    main()
