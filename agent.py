# library imports
import random
import numpy as np

# project imports
from utils import Utils


class Agent:
    """
    A single writer of the paper (agent in the agent-based simulation)
    """

    # CONSTS #
    NO_GAME_VAL = -1
    # END - CONSTS #

    def __init__(self,
                 id: int,
                 contribute_willing_mean: float,
                 contribute_willing_std: float,
                 important_paper: float,
                 personal_utility: list,
                 contributed: float = 0,
                 chicken_contributed: float = 0):
        self._id = id
        self.contribute_willing_mean = contribute_willing_mean
        self.contribute_willing_std = contribute_willing_std
        self.important_paper = important_paper
        self.personal_utility = personal_utility
        self.contributed = contributed
        self.chicken_contributed = chicken_contributed

    @staticmethod
    def random(id: int,
               agent_count: int):
        """
        Generate an agent in random
        """
        contribute_willing_mean = random.random() * 10
        """
        further_drop_factor = round(random.random() / 5, 2)
        second_value = round(random.random()/2, 2)
        personal_utility = [1, second_value]
        for i in range(max([agent_count-2, 0])):
            personal_utility.append(max([second_value - further_drop_factor*(i+1), 0.05]))
        """
        reduce_factor = random.random()*0.2
        initial_reduce_factor = random.random()/4
        personal_utility = [(1-random.random()*initial_reduce_factor)/(i+1+reduce_factor) for i in range(max([agent_count, 0]))]
        return Agent(id=id,
                     contributed=0,
                     chicken_contributed=0,
                     contribute_willing_mean=contribute_willing_mean,
                     contribute_willing_std=0, #random.random()*3,
                     personal_utility=personal_utility,
                     important_paper=contribute_willing_mean*30*random.random())

    def get_id(self) -> int:
        """ getter for the id of the agent """
        return self._id

    def make_decision(self,
                      population,
                      author_list: list,
                      allow_chicken: bool) -> int:
        """
        Make a decision of how to contribute and if decides to play a chicken game this turn
        """
        # anyway, contribute to the paper
        self.contributed += np.random.normal(self.contribute_willing_mean, self.contribute_willing_std)
        if allow_chicken:
            return self.eval_chicken(population=population,
                                     author_list=author_list)
        return Agent.NO_GAME_VAL # like saying "no chicken game"

    def eval_chicken(self,
                     author_list: list,
                     population) -> int:
        """
        Eval the expected utility from chicken in this turn
        """
        possible_positions_to_improve = range(author_list.index(self._id))
        # test for each position in a brute-force manner
        for better_position in possible_positions_to_improve:
            author_list_after_chicken = Utils.author_list_after_chicken(author_list=author_list,
                                                                        chicken_agent=self._id,
                                                                        new_position=better_position)
            this_position_possible = True
            for agent in population.agents:
                if agent.get_id() != self._id:
                    if not agent.agree_to_proposed_chicken(author_list_after_chicken=author_list_after_chicken,
                                                           author_list=author_list):
                        this_position_possible = False
                        break
            if this_position_possible:
                return better_position
        return Agent.NO_GAME_VAL

    def agree_to_proposed_chicken(self,
                                  author_list: list,
                                  author_list_after_chicken: list) -> bool:
        """
        Eval the expected utility from each response to a chicken in this turn
        """
        # if it does not influence me, let it be
        my_location = author_list.index(self._id)
        my_new_location = author_list_after_chicken.index(self._id)
        return (my_new_location == my_location) or (self.personal_utility[my_location] - self.personal_utility[my_new_location]) * self.important_paper > self.contributed

    def withdraw_chicken(self,
                         author_list: list) -> bool:
        """
        Eval if withdraw is better or break game
        """
        return self.personal_utility[author_list.index(self._id)] * self.important_paper > self.contributed

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Agent #{}: contributed={:.2f}, personal paper utility = {:.2f}>, personal location utility = {}".format(
            self._id,
            self.contributed,
            self.important_paper,
            self.personal_utility
        )
