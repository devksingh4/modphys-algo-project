from Track import Track
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt, cm, colors
import math

def angle_between(vector_1, vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    if math.isnan(angle): 
        return 0 
    else: 
        return angle
def calc_mse(real, pred):
    return np.square(np.subtract(real,pred)).mean() 
# def plot_3d_data(x,y,z):
#     fig = plt.figure()
#     ax = fig.add_subplot(projection='3d')
#     ax.scatter(x, y, z)
#     plt.title('All detector data', fontsize=12)
#     plt.show()
class TrackPhiEtaFinderDevSingh():
    
    def find_phi_eta(self, track):
        # The track variable is of type Track
        # Of the Track variables, only points and vertex will be filled at this point
        vertex = np.array(track.vertex)
        data = list(map(lambda point: np.array([point.x, point.y, point.z]), track.points))
        x_data = np.array(data).T[0]
        y_data = np.array(data).T[1]
        # Calculate etas
        thetas = []
        for v1 in data:
            # vector in form <x, y, z>, find angle to z-axis
            theta = angle_between(np.array([v1[0], v1[1], v1[2] - vertex]), np.array([0,0,1]))
            thetas.append(theta)
        thetas = np.array(thetas)
        phis = []
        for v1 in data:
            # vector in form <x, y>, find angle to x-axis
            phi = angle_between(np.array([v1[0], v1[1]]), np.array([1,0]))
            phis.append(phi)  
        phi = phis[0] # np.interp(vertex, z_data, phis) # linear interpolation to vertex (doesn't actually seem to bring much benefit)
        theta_pred = np.array(thetas).mean() # np.interp(vertex, z_data, thetas) (doesn't actually seem to bring much benefit)
        # Not using the interpolations because it adds uncertainty if the vertex is too far away, and it doesn't bring much benefit
        eta = -1 * np.log(np.tan(theta_pred/2))
        if (np.average(x_data[0]) < 0  and np.average(y_data) < 0): # account for range of arccos() being from 0 to pi and not 2 pi
            phi += np.pi
        if (np.average(x_data) > 0 and np.average(y_data) < 0 and phi != 0):
            phi = -1 * phi
        if phi < 0:
            phi += 2 * np.pi
        # Just return them, like this:
        return phi, eta

