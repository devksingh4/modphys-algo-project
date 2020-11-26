#     Modern Physics Particle Tracking Modeling Software
#     Copyright (C) 2020 Dev Singh
#     This software is licensed under the BSD 3-Clause license.
#     For more information, see 
import pandas as pd
import numpy as np
from math import sqrt, pi

df = pd.read_csv("data.csv")
x_data = df["x"].to_numpy()
y_data = df["y"].to_numpy()
z_data = df["z"].to_numpy()
xy_data = np.vstack(([x_data.T], [y_data.T])).T # combine individual points into points/vectors
data = np.vstack(([x_data.T], [y_data.T], [z_data.T])).T

# Common ops functions
def angle_between(v1, v2):
    """Calculates the angle between two vectors in radians"""
    dot_pr = v1.dot(v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.arccos(dot_pr / norms)
def calc_mse(real, pred):
    return np.square(np.subtract(real,pred)).mean() 

# Calculate thetas
thetas = []
for v1 in data:
    # vector in form <x, y, z>, angle to z-axis
    theta = angle_between(np.array([v1[2], v1[0]]), np.array([1,0]))
    thetas.append(theta)
thetas = np.array(thetas)
df['Center-of-Mass Scattering Angle (radians)'] = thetas

# Calculate pseudo-rapidity η
df['Psuedo-Rapidity η'] = -1 * np.log(np.tan(thetas/2))

# Calculate Azimuthal angle (Phi)
phis = []
for v1 in xy_data:
    # vector in form <x, y>, angle to x-axis
    phi = angle_between(v1, np.array([1,0]))
    phis.append(phi)    
df['Azimuthal Angle (radians)'] = phis

df.to_excel("calcdata.xlsx")