from Track import Track
import numpy as np

def angle_between(vector_1, vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    return np.arccos(dot_product)
def calc_mse(real, pred):
    return np.square(np.subtract(real,pred)).mean() 
class TrackPhiEtaFinderDevSingh():
    
    def find_phi_eta(self, track):
        # The track variable is of type Track
        # Of the Track variables, only points and vertex will be filled at this point
        vertex = np.array(track.vertex)
        data = list(map(lambda point: np.array([point.x, point.y, point.z]), track.points))
        # Calculate etas
        thetas = []
        for v1 in data:
            # vector in form <x, y, z>, angle to z-axis
            theta = angle_between(np.array([v1[2], v1[0]]), np.array([1,0]))
            thetas.append(theta)
        thetas = np.array(thetas)
        etas = -1 * np.log(np.tan(thetas/2))
        eta = etas[0]
        phis = []
        for v1 in data:
            # vector in form <x, y>, angle to x-axis
            phi = angle_between(np.array([v1[0], v1[1]]), np.array([1,0]))
            phis.append(phi)    
        phi = phis[0]
        while eta > np.pi:
            eta = eta - (np.pi)
        # Just return them, like this:
        return phi, eta

