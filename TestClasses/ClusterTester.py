import itertools
import math

from FileReader import FileReader

from Cluster import Cluster
from Vector import Vector

def get_event(filename):
    reader = FileReader()
    event = reader.get_event(filename)
    return event

def test_event(filename, expected_string, function_to_extract, function_to_run, function_to_process):
    print("Event %s:" % expected_string)
    data = function_to_extract(filename)
    result = function_to_run(data)
    output = function_to_process(result)
    print("You found %s" % output)
    print("")

def test_component(filename_list, expected_list, function_to_extract, function_to_run, function_to_process):
    for filename, expected_string in zip(filename_list, expected_list):
        test_event(filename, expected_string, function_to_extract, function_to_run, function_to_process)

def test_cluster_finder(analysis, mod):
    filename_list = []
    for i in range(1,6):
        filename_list.append("TestData/Mod %d - clusterIDEvent%d.txt" % (mod, i))
    expected_list = ["1 has one electron", "2 has two muons", "3 has one jet", "4 has two jets", "5 has three jets and one electron"]
    extract_function = lambda filename : get_event(filename).calorimeter_hits
    run_function = lambda data : analysis.cluster_finder.identify_clusters(data)
    process_function = lambda tracks : "%d clusters" % len(tracks)
    test_component(filename_list, expected_list, extract_function, run_function, process_function)

def convert_theta_to_eta(theta):
    return -math.log(math.tan(theta / 2))

def get_jet_vals():
    return [[316.045, 163.373, -311.695, 473.000, 0.330], [-246.201, 426.435, 86.825, 500.000, 0.330], [426.434, 246.202, -86.823, 500.000, 0.330], [-1000.006, -1732.047, 0.003, 2000.000, 0.330], \
            [1000.002, 1732.050, 0.003, 2000.000, 0.330], [-318.962, 0.001, -1156.832, 1200.000, 1.500]]

def get_true_phi_eta():
    jet_phi = []
    jet_eta = []
    for jet in get_jet_vals():
        jet_phi.append(math.atan2(jet[1], jet[0]))
        jet_r = math.sqrt(jet[0] ** 2 + jet[1] ** 2 + jet[2] ** 2)
        jet_theta = math.acos(jet[2] / jet_r)
        jet_eta.append(convert_theta_to_eta(jet_theta))

    phi_true_values = [0, math.pi / 2, 3 * math.pi / 2, jet_phi[0], jet_phi[1], jet_phi[2], jet_phi[3], jet_phi[4], jet_phi[5], math.pi / 2]
    eta_true_values = [convert_theta_to_eta(math.pi / 2), convert_theta_to_eta(math.pi / 4), convert_theta_to_eta(math.pi / 4), jet_eta[0], jet_eta[1], jet_eta[2], jet_eta[3], jet_eta[4], jet_eta[5], convert_theta_to_eta(math.pi / 4)]

    return phi_true_values, eta_true_values

def get_true_energy():
    jets = get_jet_vals()
    return [300, 400, 200, jets[0][3], jets[1][3], jets[2][3], jets[3][3], jets[4][3], jets[5][3], 500]

def test_cluster_phi_eta_finder(analysis, mod):
    filename_list = []
    for i in range(1, 6):
        filename_list.append("TestData/Mod %d - clusterID - SeparateParticlesEvent%d.txt" % (mod, i))
    for i in range(1, 6):
        filename_list.append("TestData/Mod %d - clusterID - SeparateParticles2Event%d.txt" % (mod, i))
    is_jet_list = [False, False, False, True, True, True, True, True, True, False]
    phis, etas = get_true_phi_eta()

    reader = FileReader()
    for i in range(10):
        print("Now testing cluster %d:" % (i + 1))
        event = reader.get_event(filename_list[i])
        cluster = Cluster()
        for hit in event.calorimeter_hits:
            cluster.add_hit(hit)
        if is_jet_list[i]:
            cluster.mark_jet()
        phi, eta = analysis.cluster_phi_eta_finder.find_phi_eta(cluster)

        print("True phi: %f\tTrue eta: %f" % (phis[i], etas[i]))
        print("Your phi: %f\tYour eta: %f" % (phi, eta))
        print("")

def test_cluster_energy_finder(analysis, mod):
    filename_list = []
    for i in range(1, 6):
        filename_list.append("TestData/Mod %d - clusterID - SeparateParticlesEvent%d.txt" % (mod, i))
    for i in range(1, 6):
        filename_list.append("TestData/Mod %d - clusterID - SeparateParticles2Event%d.txt" % (mod, i))
    is_jet_list = [False, False, False, True, True, True, True, True, True, False]
    phis, etas = get_true_phi_eta()
    energies = get_true_energy()

    reader = FileReader()
    for i in range(10):
        print("Now testing cluster %d:" % (i + 1))
        event = reader.get_event(filename_list[i])
        cluster = Cluster()
        for hit in event.calorimeter_hits:
            cluster.add_hit(hit)
        if is_jet_list[i]:
            cluster.mark_jet()
        cluster.set_phi(phis[i])
        cluster.set_eta(etas[i])
        energy = analysis.cluster_energy_finder.find_energy(cluster)

        print("True energy: %f" % energies[i])
        print("Your energy: %f" % energy)
        print("")

def read_cluster_values(filename):
    with (open(filename, "r")) as file:
        positions = []
        while (True):
            line = file.readline()
            if (not line):
               break
            tokens = line.split()
            position = Vector(float(tokens[1].strip(", ")), float(tokens[2].strip(", ")), float(tokens[3].strip(", ")))
            positions.append(position)
    return positions

def get_values_from_vector(vector):
    phi = vector.azimuthal()
    theta = vector.polar()
    eta = convert_theta_to_eta(theta)
    momentum = vector.magnitude()
    energy = momentum
    return phi, theta, energy

def get_true_clusters(mod):
    filename_list = ["Mod %d - trackIDseparateParticles1.txt" % mod, "Mod %d - trackIDseparateParticles2.txt" % mod, "Mod %d - clusterIDseparateParticles3.txt" % mod, "Mod %d - clusterIDseparateParticles5.txt" % mod , "Mod %d - trackIDseparateParticles5.txt" % mod]
    phis, etas = get_true_phi_eta()
    energies = get_true_energy()

    final_clusters = []
    reader = FileReader()
    for i in range(5):
        clusters = []
        if i == 2 or i == 3:
            if i == 2:
                min = 3
                max = 4
            elif i == 3:
                min = 6
                max = 10
            for i_cluster in range(min, max):
                cluster = Cluster()
                cluster.set_phi(phis[i_cluster])
                cluster.set_eta(etas[i_cluster])
                cluster.set_energy(energies[i_cluster])
                cluster.mark_jet()
                clusters.append(cluster)
        else:
            clusters = reader.get_all_clusters("TestData/" + filename_list[i])
            true_clusters = read_cluster_values("TestData/Mod %d - clusterIDTrueValues%d.txt" % (mod, i + 1))
            for i_cluster in range(len(clusters)):
                phi, eta, energy = get_values_from_vector(true_clusters[i_cluster])
                clusters[i_cluster].set_phi(phi)
                clusters[i_cluster].set_eta(eta)
                clusters[i_cluster].set_energy(energy)
        final_clusters.append(clusters)
    return final_clusters
