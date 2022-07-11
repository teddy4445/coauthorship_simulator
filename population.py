# library imports
from random import random, choice

# project imports
from agent import Agent
from utils import Utils


class Population:
    """
    A list of agents that play in the game (writing an academic paper)
    """

    def __init__(self, agents: list):
        self.agents = agents

    @staticmethod
    def random_case_random(agents_count: int,
                           contribute_spectrum: float,
                           time: int,
                           importance_spectrum: float):
        """
        Generate a list of agents with property about their connections
        """
        agents = [Agent.random(id=id + 1,
                               agent_count=agents_count)
                  for id in range(agents_count)]
        min_contribute_index = choice(list(range(agents_count)))
        agents[min_contribute_index].contributed = time/importance_spectrum
        max_contribute_index = min_contribute_index
        while max_contribute_index == min_contribute_index:
            max_contribute_index = choice(list(range(agents_count)))
        agents[max_contribute_index].contributed = time * contribute_spectrum / importance_spectrum

        min_importance_index = choice(list(range(agents_count)))
        agents[min_contribute_index].important_paper = 50
        max_importance_index = min_importance_index
        while max_importance_index == min_importance_index:
            max_importance_index = choice(list(range(agents_count)))
        agents[max_importance_index].important_paper = 50*importance_spectrum

        for index, agent in enumerate(agents):
            agent.contribute_willing_mean = 0  # make sure it does not change the contribution
            agent.contribute_willing_std = 0  # make sure it does not change the contribution
            if index not in [min_contribute_index, max_contribute_index]:
                agent.contributed = time * (1 + random()*contribute_spectrum)
            if index not in [min_importance_index, max_importance_index]:
                agent.important_paper = time * (1 + 100*random()*importance_spectrum)

        return Population(agents=agents)

    def make_decision(self,
                      author_list: list,
                      allow_chicken: bool):
        """
        Make a decision of how to contribute and if decides to play a chicken game this turn
        and if so, what is the place the agents asks for
        """
        sample_order = Utils.random_pick_order(len(self.agents))
        chicken_offer_agent_ids = []
        for agent_index in sample_order:
            played_chicken_position = self.agents[agent_index].make_decision(population=self,
                                                                             author_list=author_list,
                                                                             allow_chicken=allow_chicken)
            if played_chicken_position != Agent.NO_GAME_VAL:
                if played_chicken_position == author_list.index(self.agents[agent_index].get_id()):
                    raise Exception("Just to make sure strange stuff does not happen")
                chicken_offer_agent_ids.append((self.agents[agent_index].get_id(), played_chicken_position))
        return chicken_offer_agent_ids

    def get_by_id(self,
                  id: int):
        """
        Get an agent by its id
        """
        for agent in self.agents:
            if agent.get_id() == id:
                return agent

    def total_contribution(self):
        """
        Calc the total real contribution of the authors
        """
        return sum([agent.contributed for agent in self.agents])

    def author_list(self,
                    with_contributed: bool = False):
        """
        Compute the author list based on the contribution and historical chicken games
        """
        contributed_authors = [(agent.contributed + agent.chicken_contributed, agent.get_id()) for agent in self.agents]
        contributed_authors = sorted(contributed_authors, key=lambda x: x[0], reverse=True)
        if with_contributed:
            return [val[0] for val in contributed_authors], [val[1] for val in contributed_authors]
        return [val[1] for val in contributed_authors]

