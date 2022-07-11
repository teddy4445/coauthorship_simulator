# library imports
import os
import numpy as np
from random import random

# project imports
from ploter import Ploter
from simulator import Simulator
from simulator_generator import SimulatiorGenerator


class Main:
    """
    Single entry point of the project
    """

    # CONSTS #
    SAVE_PATH = os.path.join(os.path.dirname(__file__), "results")
    # END - CONSTS #

    def __init__(self):
        pass

    @staticmethod
    def run():
        """
        make all the simulations for the paper and the plots
        """
        Main._io_prepare()
        # Main.simple_exp()
        Main.case_anaylsis()

    @staticmethod
    def simple_exp():
        """
        Run the most simple configuration
        """
        sim = SimulatiorGenerator.random()
        sim.run()
        Ploter.single_sim_report(sim=sim,
                                 save_path=os.path.join(Main.SAVE_PATH))

    @staticmethod
    def case_anaylsis():
        """
        Run the most simple configuration
        """
        x_range = [1 + val*0.25 for val in range(4*4+1)]
        y_range = [1 + val*0.25 for val in range(4*4+1)]
        for agents_count in range(2, 9):
            data = []
            for contribute_spectrum in x_range:
                row_answer = []
                for importance_spectrum in y_range:
                    # alert the user about the progress
                    print("Working on ac={}, cs={}, is={}".format(agents_count,
                                                                  contribute_spectrum,
                                                                  importance_spectrum))
                    case_result_list = []
                    for repeat in range(1000):
                        # build and run simulation
                        sim = SimulatiorGenerator.case_random(agents_count=agents_count,
                                                              contribute_spectrum=contribute_spectrum,
                                                              importance_spectrum=importance_spectrum,
                                                              time=round(random()*50))
                        # run simulation and recored it
                        case_result_list.append(np.asarray(sim.run_single_chicken()))
                    row_answer.append(list(np.asarray(case_result_list).mean(axis=0)))
                data.append(row_answer)
            print("Saving plots... \n\n\n")
            Ploter.case_analysis(data=data,
                                 eges=False,
                                 x_range=x_range,
                                 y_range=y_range,
                                 save_path=os.path.join(Main.SAVE_PATH, "3d_case_{}.pdf".format(agents_count)))
            Ploter.case_analysis(data=data,
                                 eges=True,
                                 x_range=x_range,
                                 y_range=y_range,
                                 save_path=os.path.join(Main.SAVE_PATH, "3d_case_edges_{}.pdf".format(agents_count)))

    @staticmethod
    def _io_prepare():
        """
        Make sure we have all the folders we need
        """
        try:
            os.mkdir(os.path.join(os.path.dirname(__file__), "results"))
        except:
            pass


if __name__ == '__main__':
    Main.run()
