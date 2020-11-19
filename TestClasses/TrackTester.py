import itertools
import math

from FileReader import FileReader
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

def test_track_finder(analysis, mod):
    filename_list = []
    for i in range(1,6):
        filename_list.append("TestData/Mod %d - trackIDEvent%d.txt" % (mod, i))
    expected_list = ["1 has one track", "2 has two tracks", "3 has three tracks", "4 has three tracks", "5 has 20 tracks"]
    extract_function = lambda filename : get_event(filename).tracker_hits
    run_function = lambda data :analysis.track_finder.identify_tracks(data)
    process_function = lambda tracks : "%d tracks" % len(tracks)
    test_component(filename_list, expected_list, extract_function, run_function, process_function)


def test_vertex_finder(analysis, mod):
    filename_list = []
    for i in range(1,6):
        filename_list.append("TestData/Mod %d - trackIDseparateParticles%d.txt" % (mod, i))
    expected_list = ["vertex z = 0", "vertex z = .3", "vertex z = -.2", "vertex z = .4", "vertex z = -.3"]
    reader = FileReader()
    extract_function = lambda filename : reader.get_all_tracks(filename)
    run_function = lambda data : analysis.vertex_finder.find_vertex(data)
    process_function = lambda vertex : "z = %d" % vertex.z
    test_component(filename_list, expected_list, extract_function, run_function, process_function)

def convert_theta_to_eta(theta):
    return -math.log(math.tan(theta / 2))

def get_true_vertex():
    return [0, .3, -.2, .4, -.3]

def get_true_phi_eta():
    phi_true_values = [[0], [math.pi / 2, 3 * math.pi / 2], [math.pi / 4, 3 * math.pi / 4, 7 * math.pi / 4], [math.pi / 4, math.pi / 4 + .01, math.pi / 4 - .01]]
    theta_true_values = [[math.pi / 2], [math.pi / 4, math.pi / 4], [math.pi / 2, math.pi / 4, 3 * math.pi / 4], [5 * math.pi / 8, 5 * math.pi / 8 + .01, 5 * math.pi / 8 - .01]]
    last_phi_vals = []
    last_theta_vals = []

    for i in range(20):
        phi = 2 * math.pi / 20 * i
        last_phi_vals.append(phi)
        theta = math.pi / 4 + 3 * math.pi / 4 / 20 * i
        last_theta_vals.append(theta)
    phi_true_values.append(last_phi_vals)
    theta_true_values.append(last_theta_vals)

    eta_true_values = []
    for event_theta in theta_true_values:
        particle_etas = []
        for particle_theta in event_theta:
            particle_etas.append(convert_theta_to_eta(particle_theta))
        eta_true_values.append(particle_etas)

    return phi_true_values, eta_true_values

def get_true_pT():
    true_phi, true_eta = get_true_phi_eta()
    energies = [[300], [400, 200], [100, 200, 300], [500, 250, 350]]
    masses = [[.000511], [.106, .106], [.13957, .13957, .13957], [.000511, .000511, .000511]]
    last_energy = []
    last_mass = []
    for i in range(20):
        energy = 100 + 400 / 20 * i
        last_energy.append(energy)
        if i % 3 == 0:
            last_mass.append(.000511)
        elif i % 3 == 1:
            last_mass.append(.106)
        else:
            last_mass.append(.493677)

    energies.append(last_energy)
    masses.append(last_mass)

    pTs = []

    for i in range(5):
        event_pT = []
        for i_track in range(len(energies[i])):
            energy = energies[i][i_track]
            mass = masses[i][i_track]
            momentum = math.sqrt(energy ** 2 - mass ** 2)
            eta = true_eta[i][i_track]
            theta = 2 * math.atan(math.exp(-eta))
            pT = momentum * math.sin(theta)
            event_pT.append(pT)
        pTs.append(event_pT)

    return pTs

def test_track_phi_eta_finder(analysis, mod):
    filename_list = []
    for i in range(1,6):
        filename_list.append("TestData/Mod %d - trackIDseparateParticles%d.txt" % (mod, i))
    expected_list = ["event 1", "event 2", "event 3", "event 4", "event 5"]
    vertex_list = get_true_vertex()
    phis, etas = get_true_phi_eta()

    reader = FileReader()
    for i in range(5):
        print("Now testing event %d:" % (i + 1))
        tracks = reader.get_all_tracks(filename_list[i])
        for i_track in range(len(tracks)):
            tracks[i_track].set_vertex(vertex_list[i])
            phi, eta = analysis.track_phi_eta_finder.find_phi_eta(tracks[i_track])

            print("True phi: %f\tTrue eta: %f" % (phis[i][i_track], etas[i][i_track]))
            print("Your phi: %f\tYour eta: %f" % (phi, eta))
            print("")

def test_track_pT_finder(analysis, mod):
    filename_list = []
    for i in range(1,6):
        filename_list.append("TestData/Mod %d - trackIDseparateParticles%d.txt" % (mod, i))
    expected_list = ["event 1", "event 2", "event 3", "event 4", "event 5"]
    vertex_list = get_true_vertex()
    phis, etas = get_true_phi_eta()
    pTs = get_true_pT()

    reader = FileReader()
    for i in range(5):
        print("Now testing event %d:" % (i + 1))
        tracks = reader.get_all_tracks(filename_list[i])
        for i_track in range(len(tracks)):
            tracks[i_track].set_vertex(vertex_list[i])
            tracks[i_track].set_phi(phis[i][i_track])
            tracks[i_track].set_eta(etas[i][i_track])
            pT = analysis.track_pT_finder.find_pT(tracks[i_track])
           
            print("True pT: %f GeV" % pTs[i][i_track])
            print("Your pT: %f GeV" % pT)
            print("")

def read_track_values(filename):
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
    pT = momentum * math.sin(theta)
    return phi, theta, pT

def get_true_tracks_for_cluster_matching(mod):
    filename_list = ["Mod %d - trackIDseparateParticles1.txt" % mod, "Mod %d - trackIDseparateParticles2.txt" % mod, "Mod %d - clusterIDseparateParticles3.txt" % mod, "Mod %d - clusterIDseparateParticles5.txt" % mod, "Mod %d - trackIDseparateParticles5.txt" % mod]
    vertex_list = get_true_vertex()
    phis, etas = get_true_phi_eta()
    pTs = get_true_pT()

    final_tracks = []
    reader = FileReader()
    for i in range(5):
        tracks = reader.get_all_tracks("TestData/" + filename_list[i])
        if (i == 2 or i == 3):
            if (i == 2):
                true_tracks = read_track_values("TestData/Mod %d - clusterIDTrueValues3.txt" % mod)
            else:
                true_tracks = read_track_values("TestData/Mod %d - clusterIDTrueValues5.txt" % mod)

            for i_track in range(len(tracks)):
                tracks[i_track].set_vertex(vertex_list[i])
                phi, eta, pT = get_values_from_vector(true_tracks[i_track])
                tracks[i_track].set_phi(phi)
                tracks[i_track].set_eta(eta)
                tracks[i_track].set_pT(pT)
            final_tracks.append(tracks)
        else:
            for i_track in range(len(tracks)):
                tracks[i_track].set_vertex(vertex_list[i])
                tracks[i_track].set_phi(phis[i][i_track])
                tracks[i_track].set_eta(etas[i][i_track])
                tracks[i_track].set_pT(pTs[i][i_track])
            final_tracks.append(tracks)
    return final_tracks
   

def get_true_tracks_for_muon_stub_matching(mod):
    filename_list = []
    for i in range(1,6):
        filename_list.append("TestData/Mod %d - muonIDseparateParticles%d.txt" % (mod, i))
    vertex_list = get_true_vertex()
    phis, etas = get_true_phi_eta()
    pTs = get_true_pT()

    reader = FileReader()
    true_tracks = []
    for i in range(5):
        tracks = reader.get_all_tracks(filename_list[i])
        for i_track in range(len(tracks)):
            tracks[i_track].set_vertex(vertex_list[i])
            tracks[i_track].set_phi(phis[i][i_track])
            tracks[i_track].set_eta(etas[i][i_track])
            tracks[i_track].set_pT(pTs[i][i_track])
        true_tracks.append(tracks)

    return true_tracks