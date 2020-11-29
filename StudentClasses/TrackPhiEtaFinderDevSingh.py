from Track import Track
import numpy as np
import math

def angle_between(vector_1, vector_2):
    """Get the angle between 2 vectors"""
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    if math.isnan(angle): 
        return 0 
    else: 
        return angle

def calc_mse(real, pred):
    """Calculate the Mean Squared Error"""
    return np.square(np.subtract(real,pred)).mean() 

class TrackPhiEtaFinderDevSingh():

    def find_phi_eta(self, track):
        
        # Get data into numpy format
        vertex = np.array(track.vertex)
        data = np.array(list(map(lambda point: np.array([point.x, point.y, point.z]), track.points)))
        x_data = data.T[0]
        y_data = data.T[1]

        # Calculate etas
        thetas = []
        for vec in data:
            # vector in form <x, y, z>, find angle to z-axis and adjust for vertex
            theta = angle_between(np.array([vec[0], vec[1], vec[2] - vertex]), np.array([0,0,1]))
            thetas.append(theta)
        thetas = np.array(thetas)

        # Calculate phis
        phis = []
        for vec in data:
            # vector in form <x, y>, find angle to x-axis
            phi = angle_between(np.array([vec[0], vec[1]]), np.array([1,0]))
            phis.append(phi)  
        
        # Choose best measurement to report
        phi = phis[0]
        theta = np.array(thetas).mean() # I don't know why but theta is consistently more accurate when using mean rather than first element
        # Not using linear interpolations because it adds uncertainty if the vertex 
        # is too far away from known values, and it doesn't bring much benefit to error

        # Calculate eta using formula
        eta = -1 * np.log(np.tan(theta/2))

        # Account for range of arccos() not including Quadrants 3 and 4
        # Replace negative values with their positive equivalents
        if (np.average(x_data[0]) < 0  and np.average(y_data) < 0 and phi != 0): 
            phi += np.pi
        if (np.average(x_data) > 0 and np.average(y_data) < 0 and phi != 0):
            phi = -1 * phi
        while phi < 0:
            phi += 2 * np.pi

        return phi, eta

