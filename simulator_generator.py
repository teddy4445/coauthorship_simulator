# library imports
import math
import random

# project imports
from agent import Agent
from population import Population
from simulator import Simulator


class SimulatiorGenerator:
    """
    This class generate simulators 
    """

    def __init__(self):
        pass

    @staticmethod
    def case_random(agents_count: int,
                    contribute_spectrum: float,
                    importance_spectrum: float,
                    time: int):
        """
        Generate a random simulator with three properties:
        agents_count, contribute_spectrum, and importance_spectrum
        """
        return Simulator(population=Population.random_case_random(agents_count=agents_count,
                                                                  time=time,
                                                                  contribute_spectrum=contribute_spectrum,
                                                                  importance_spectrum=importance_spectrum),
                         chicken_punishment=0,
                         paper_ready_contribution=9999)  # inf

    @staticmethod
    def random():
        """
        Generate random instance of the simulator
        """
        agents_count = random.randint(2, 11)
        return Simulator(population=Population(agents=[Agent.random(id=id + 1,
                                                                    agent_count=agents_count) for id in range(agents_count)]),
                         chicken_punishment=100,
                         paper_ready_contribution=random.randint(round(100*math.pow(agents_count,1.33)), round(100*math.pow(agents_count,1.5))))
