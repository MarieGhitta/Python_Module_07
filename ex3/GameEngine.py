from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        
    def configure_engine(self, factory: CardFactory, 
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        new_hand = self.factory.create_themed_deck(3)
        hand = new_hand["deck"]
        battlefield = []
        turn = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated += 1
        self.total_damage += turn["damage_dealt"]
        return turn

    def get_engine_status(self) -> dict:
        status = {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.turns_simulated * 3
        }
        return status
