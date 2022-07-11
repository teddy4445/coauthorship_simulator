# library imports
import random

# project imports


class Utils:
    """
    A set of useful functions
    """

    def __init__(self):
        pass
        
    @staticmethod
    def random_pick_order(length: int):
        l = list(range(length))
        random.shuffle(l)
        return l

    @staticmethod
    def author_list_after_chicken(author_list: list,
                                  chicken_agent: int,
                                  new_position: int):
        answer = []
        move_index = 0
        original_chiken_position = author_list.index(chicken_agent)
        for index in range(len(author_list)+1):
            if index == new_position:
                answer.append(chicken_agent)
                move_index = -1
            elif index + move_index == original_chiken_position:
                continue
            else:
                answer.append(author_list[index+move_index])
        return answer

    @staticmethod
    def chicken_contribute(contributes: list,
                           ids: list,
                           chicken_id: int,
                           wanted_location: int):
        min_contribute = contributes[wanted_location]
        current_contribute = contributes[ids.index(chicken_id)]
        return 1+min_contribute-current_contribute
