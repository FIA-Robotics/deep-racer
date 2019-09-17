import math

def reward_function(params):
    '''
    Example of rewarding the agent to go to the next waypoint
    '''
    
    x, y = params['x'], params['y']
    wx, wy = params['closest_waypoints']
    heading = (params['heading'])*math.pi/180 if params['heading'] >= 0 else (360+params['heading'])*math.pi/180
    delta = [wx-x,wy-y]
    norm = math.sqrt(delta[0]**2+delta[1]**2)
    delta[0] /= norm
    delta[1] /= norm
    heading_vector = (math.cos(heading),math.sin(heading))
    reward = delta[0]*heading_vector[0]+delta[1]*heading_vector[1]
    print(reward)
    return reward