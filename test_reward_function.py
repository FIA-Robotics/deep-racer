import reward_functions.utils
import unittest
import reward_functions.follow_center as fc
import reward_functions.improved_follow_center as ifc
import reward_functions.go_to_waypoint as gtw


class TestBasicRewardfunctionAttributes(unittest.TestCase):
    def test_straight_better(self):
        """This test should check if the reward is higher by going straight on a straight road
            than heading crookedly, provided that all other values are constant. 
            Observe that some simple reward functions may fail this test 
        """
        self.params = {}
        self.params["distance_from_center"] = 0
        self.params["track_width"] = 3
        self.params["x"] = 5
        self.params["y"] = 5
        self.params["heading"] = -15
        self.params["closest_waypoints"] = (7,5)
        reward_not_straight = gtw.reward_function(self.params)
        self.params["heading"] = 0
        reward_straight = gtw.reward_function(self.params)
        self.assertGreater(reward_straight,reward_not_straight)
    

if __name__ == '__main__':
    unittest.main()
