# library imports
import os
import json
import numpy as np
import matplotlib.pyplot as plt

# project imports
from simulator import Simulator


class Ploter:
    """
    Hold all the ploting logic of the project
    """

    # COLORS #
    COLORS = ["#00FFFF", "#458B74", "#E3CF57", "#8B7D6B", "#00008B",
              "#8A2BE2", "#FFD39B", "#98F5FF", "#FF6103", "#66CD00",
              "#3D59AB", "#CAFF70", "#FFFAF0", "#838B83", "#FFD700"]
    # END - COLORS #

    def __init__(self):
        pass

    @staticmethod
    def case_analysis(data: list,
                      eges: bool,
                      x_range: list,
                      y_range: list,
                      save_path: str):
        """
        3D scatter plot of chicken played or not
        """
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(projection='3d')
        for x_index, row in enumerate(data):
            for y_index, col in enumerate(row):
                for z_index, val in enumerate(col):
                    ax.scatter(x_range[x_index],
                               y_range[y_index],
                               1+z_index,
                               alpha=0.5,
                               marker="o" if not eges else "x" if val >= 0.5 else "o",
                               color=np.array([val, 1-val, 0]) if not eges else np.array([1, 0, 0]) if val >= 0.5 else np.array([0, 1, 0]))

        ax.scatter(x_range[0],
                   y_range[0],
                   -100,
                   alpha=1,
                   marker="o" if not eges else "x",
                   color="red",
                   label="100% Ultimatum")

        ax.scatter(x_range[0],
                   y_range[0],
                   -100,
                   alpha=1,
                   marker="o",
                   color="green",
                   label="0% ultimatum")
        ax.set_xlabel('Contribute spectrum', fontsize=18)
        ax.set_ylabel('Importance spectrum', fontsize=18)
        ax.set_zlabel('Author position', fontsize=18)
        ax.set_zlim(1, len(data[0][0]))
        plt.xticks([min(x_range), max(x_range)])
        plt.yticks([min(y_range), max(y_range)])
        ax.set_zticks(range(1,1+len(data[0][0])))
        plt.legend(prop={'size': 18})
        plt.tight_layout()
        plt.savefig(save_path, dpi=500)
        plt.close()

    @staticmethod
    def single_sim_report(sim: Simulator,
                          save_path: str):
        """
        Give the basic report of a single simulation and save it 
        """
        # save chicken games
        with open(os.path.join(save_path, "chicken_events.json"), "w") as chicken_file:
            json.dump([event.to_json() for event in sim.chicken_game_events],
                      chicken_file,
                      indent=2)
        # plot the dist over time
        plt.imshow(np.array(sim.author_list).T.tolist(),
                   cmap="Blues",
                   aspect=2,
                   interpolation="nearest")
        plt.yticks(range(len(sim.population.agents)), [i+1 for i in range(len(sim.population.agents))])
        plt.xticks(list(range(len(sim.author_list)))[::max([round(len(sim.author_list)/10),1])])
        #plt.colorbar()
        plt.savefig(os.path.join(save_path, "author_list.png"), dpi=600)
        plt.close()
