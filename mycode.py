# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%

# %% [markdown]
#     Modern Physics Particle Tracking Modeling Software
#     Copyright (C) 2020 Dev Singh
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt, cm, colors
from math import sqrt, pi
from lsc import lsc


# %%
df = pd.read_csv("data.csv")
x_data = df["x"].to_numpy()
y_data = df["y"].to_numpy()
z_data = df["z"].to_numpy()
xy_data = np.vstack(([x_data.T], [y_data.T])).T # combine individual points into points/vectors
data = np.vstack(([x_data.T], [y_data.T], [z_data.T])).T


# %%
# visualize data
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x_data, y_data, z_data)
plt.title('All detector data', fontsize=12)
plt.show()
xy_plot = plt.figure()
ax_xy = plt.axes()
ax_xy.scatter(x_data, y_data)
plt.title('x-y data', fontsize=12)
plt.show()
xy_plot = plt.figure()
ax_xy = plt.axes()
ax_xy.scatter(z_data, y_data)
plt.title('z-y data', fontsize=12)
plt.show()


# %%
xc,yc,radius,v = lsc(xy_data)
print("Center is at: ({}, {}) with radius of {}, variance {}".format(xc, yc, radius, v))
circle1 = plt.Circle((xc, yc), radius, color='g')
fig2, ax2 = plt.subplots()
plt.grid(linestyle='--')
plt.xlim(-175,10)
plt.ylim(-100,100)
ax2.set_aspect('equal')
ax2.add_artist(circle1)
ax2.annotate('{}, {}'.format(round(xc, 1), round(yc,1)), xy=(xc , yc), arrowprops=dict(facecolor='black', shrink=0.01))
ax2.annotate('{}, {}'.format(round(xc+radius, 1), round(yc,1)), xy=(xc + radius, yc), arrowprops=dict(facecolor='black', shrink=0.01))
ax2.annotate('{}, {}'.format(round(xc - radius, 1), round(yc,1)), xy=(xc - radius, yc), arrowprops=dict(facecolor='black', shrink=0.01))
plt.scatter(x_data, y_data)
plt.title('Least Squares Circle model of movement', fontsize=12)
plt.show()
pos_charge = True
if np.polyfit(x_data,y_data,1)[0] < 0: # if the slope of the data plotted on the xy axis is roughly negative
    print("Negatively charged particle (charge -1)")
    pos_charge = False
else:
    print("Positively charged particle (charge 1)")


# %%
# Common ops functions
def angle_between(v1, v2):
    """Calculates the angle between two vectors in radians"""
    dot_pr = v1.dot(v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.arccos(dot_pr / norms)
def calc_mse(real, pred):
    return np.square(np.subtract(real,pred)).mean() 


# %%
# Calculate thetas
thetas = []
for v1 in data:
    # vector in form <x, y, z>, angle to z-axis
    theta = angle_between(v1, np.array([0,0,1]))
    thetas.append(theta)
thetas = np.array(thetas)
df['Center-of-Mass Scattering Angle (radians)'] = thetas


# %%
# Calculate pseudo-rapidity η
df['Psuedo-Rapidity η'] = -1 * np.log(np.tan(thetas/2))


# %%
# Calculate Azimuthal angle (Phi)
phis = []
for v1 in data:
    # vector in form <x, y, z>, angle to x-axis
    phi = angle_between(v1, np.array([1,0,0]))
    phis.append(phi)    
df['Azimuthal Angle (radians)'] = phis


# %%
# Calculate Transverse Momentum (convert to GeV/c in Wolfram Alpha for accuracy)
electric_charge = 1.6e-19 # coulumbs
magnetic_field = 10 # Tesla
p_t = electric_charge * radius * magnetic_field
print("Transverse momentum is {} kg m/s and charge is {}. ".format(p_t, "positive" if pos_charge else "negative"))


# %%
df.to_excel("calcdata.xlsx")


# %%
prediction = []
h = xc
k = yc
r = radius
for val in x_data:
    def calc_prediction(x):
        return k + sqrt((-h**2+r**2+2*h*x-x**2))
    prediction.append(calc_prediction(val))
print("Mean Squared Error is {}".format(calc_mse(y_data, prediction)))


# %%
# Visualising the variation in all the data points. Not part of calculation.
# theta
plt.plot(np.linspace(0, len(df['Center-of-Mass Scattering Angle (radians)']), len(df['Center-of-Mass Scattering Angle (radians)'])), df['Center-of-Mass Scattering Angle (radians)'])
plt.show()


# %%
# eta
plt.plot(np.linspace(0, len(df['Psuedo-Rapidity η']), len(df['Psuedo-Rapidity η'])), df['Psuedo-Rapidity η'])
plt.show()


# %%
# phi
plt.plot(np.linspace(0, len(df['Azimuthal Angle (radians)']), len(df['Azimuthal Angle (radians)'])), df['Azimuthal Angle (radians)'])
plt.show()


