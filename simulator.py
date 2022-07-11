# library imports

# project imports
from agent import Agent
from utils import Utils
from population import Population
from chicken_event import ChickenEvent


class Simulator:
    """
    The main simulator class
    """

    def __init__(self,
                 population: Population,
                 paper_ready_contribution: float,
                 chicken_punishment: float):
        self.population = population
        self.paper_ready_contribution = paper_ready_contribution
        self.chicken_punishment = chicken_punishment

        # graph data
        self.contributed_graph = []
        self.author_list = []
        self.chicken_game_events = []

    def run(self):
        """
        run the simulator
        """
        while self.population.total_contribution() < self.paper_ready_contribution:
            game_ended = self.run_step()
            if game_ended:
                break

    def run_single_chicken(self):
        """
        Run a single step game
        """
        # anyway everyone contributing in some level
        chicken_offer_agent_ids = self.population.make_decision(allow_chicken=True,
                                                                author_list=self.population.author_list(with_contributed=False))
        chicken_offer_agent_ids = [val[0] for val in chicken_offer_agent_ids]
        return [1 if agent in chicken_offer_agent_ids else 0
                for agent in self.population.author_list(with_contributed=False)]

    def run_step(self):
        """
        Run a single step
        """
        # anyway everyone contributing in some level
        chicken_offer_agent_ids = self.population.make_decision(allow_chicken=True,
                                                                author_list=self.population.author_list(with_contributed=False))
        # if someone wants to declare chicken
        game_ended = False
        if len(chicken_offer_agent_ids) > 0:
            # play chicken for each agent
            for chicken_agent_id, asked_position in chicken_offer_agent_ids:
                contributes, author_list = self.population.author_list(with_contributed=True)
                agent_of_intrest = self.population.get_by_id(id=chicken_agent_id)
                event = ChickenEvent(contributes=contributes,
                                     ids=author_list,
                                     initial_agent_id=chicken_agent_id,
                                     wanted_position=asked_position)
                author_list_after_chicken = Utils.author_list_after_chicken(author_list=author_list,
                                                                            chicken_agent=chicken_agent_id,
                                                                            new_position=asked_position)
                pop_responses = [agent.agree_to_proposed_chicken(author_list=author_list,
                                                                 author_list_after_chicken=author_list_after_chicken)
                                 for agent in self.population.agents if agent.get_id() != chicken_agent_id]
                event.add_pop_responses(pop_responses=pop_responses)
                pop_agree = all(pop_responses)
                # if all agree,
                if pop_agree:
                    added_value = Utils.chicken_contribute(contributes=contributes,
                                                           ids=author_list,
                                                           chicken_id=chicken_agent_id,
                                                           wanted_location=asked_position)
                    agent_of_intrest.chicken_contributed += added_value
                    event.count_added_value(added_value=added_value)
                else:  # if someone disagree
                    is_withdraw = agent_of_intrest.withdraw_chicken(author_list=author_list)
                    # if withdraw get punishment for trying
                    if is_withdraw:
                        agent_of_intrest.chicken_contributed -= self.chicken_punishment
                        event.count_added_value(added_value=self.chicken_punishment * -1)
                    else:  # dead-end the game is dead
                        game_ended = True
                        event.mark_game_over()
                        self.chicken_game_events.append(event)
                        break
                self.chicken_game_events.append(event)
        # anyway, record this turn results
        self.gather_state()
        # tell if the game ended
        return game_ended

    def gather_state(self):
        """
        Collect the data for the simulation's report later
        """
        self.contributed_graph.append(self.population.total_contribution())
        self.author_list.append(self.population.author_list(with_contributed=False))
