# library imports
import json

# project imports
from agent import Agent
from utils import Utils


class ChickenEvent:
    """
    Store a chicken game event
    """

    def __init__(self,
                 contributes: list,
                 ids: list,
                 initial_agent_id: int,
                 wanted_position: int):
        self.initial_agent_id = initial_agent_id
        self.ids = ids
        self.contributes = contributes
        self.wanted_position = wanted_position
        self.pop_responses = None
        self.added_value = 0
        self.is_game_over = False

    def add_pop_responses(self,
                          pop_responses: list):
        self.pop_responses = pop_responses

    def count_added_value(self,
                          added_value: float):
        self.added_value = added_value

    def mark_game_over(self):
        self.is_game_over = True

    def to_json(self):
        return {
            "initial_agent_id": self.initial_agent_id,
            "wanted_position": self.wanted_position,
            "pop_responses": self.pop_responses,
            "added_value": self.added_value,
            "is_game_over": self.is_game_over,
            "ids": self.ids,
            "contributes": self.contributes
        }