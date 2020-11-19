from Track import Track
import numpy as np
def angle_between(v1, v2):
    """Calculates the angle between two vectors in radians"""
    dot_pr = v1.dot(v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.arccos(dot_pr / norms)
def calc_mse(real, pred):
    return np.square(np.subtract(real,pred)).mean() 
class TrackPhiEtaFinderDevSingh():
    
    def find_phi_eta(self, track):
        # The track variable is of type Track

        # Of the Track variables, only points and vertex will be filled at this point
        vertex = np.array(track.vertex)

        # points is an array of vectors
        data = []
        for point in track.points:
            asVec = np.array([point.x, point.y, point.z])
            data.append(asVec)
        data = np.array(data)
        # Calculate etas
        thetas = []
        for point in data:
            theta = np.array(angle_between(point, vertex))
            thetas.append(theta)
        thetas = np.array(thetas)
        etas = -1 * np.log(np.tan(thetas/2))
        print(etas)
        # One way or another, you should find your phi and eta for the track
        phi = 1
        eta = etas[0]

        # Just return them, like this:
        return phi, eta

