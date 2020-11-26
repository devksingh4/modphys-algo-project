from Track import Track
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt, cm, colors

def angle_between(vector_1, vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    return np.arccos(dot_product)
def calc_mse(real, pred):
    return np.square(np.subtract(real,pred)).mean() 
def plot_3d_data(data):
    x_data = np.array(data).T[0]
    y_data = np.array(data).T[1]
    z_data = np.array(data).T[2]
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x_data, y_data, z_data)
    plt.title('All detector data', fontsize=12)
    plt.show()
class TrackPhiEtaFinderDevSingh():
    
    def find_phi_eta(self, track):
        # The track variable is of type Track
        # Of the Track variables, only points and vertex will be filled at this point
        vertex = np.array(track.vertex)
        data = list(map(lambda point: np.array([point.x, point.y, point.z]), track.points))
        x_data = np.array(data).T[0]
        y_data = np.array(data).T[1]
        z_data = np.array(data).T[2]
        # Calculate etas
        thetas = []
        for v1 in data:
            # vector in form <x, y, z>, angle to z-axis
            theta = angle_between(np.array(v1), np.array([0,0,1]))
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
        y_data = list(y_data)
        plt.plot(x_data, y_data)
        plt.show()
        if (np.average(x_data[0]) < 0  and np.average(y_data) < 0): # account for range of arccos() being from 0 to pi and not 2 pi
            phi += np.pi
        if (np.average(x_data) > 0 and np.average(y_data) < 0 and phi != 0):
            phi = -1 * phi
        while eta > np.pi:
            eta = eta - (np.pi)
        # Just return them, like this:
        # plot_3d_data(data)
        return phi, eta

