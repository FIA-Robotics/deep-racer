import math
def gauss(distance_from_center, sigma):
    return math.exp(-(distance_from_center)**2/sigma**2)

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    sigma = track_width/2
    reward = gauss(distance_from_center,sigma)
    return reward