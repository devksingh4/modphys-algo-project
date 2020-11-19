import itertools
import math

from FileReader import FileReader
from MatchedObjects import MatchedObjects

from TestClasses.TrackTester import get_true_tracks_for_cluster_matching, get_true_tracks_for_muon_stub_matching
from TestClasses.ClusterTester import get_true_clusters

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

def test_muon_stub_finder(analysis, mod):
    filename_list = []
    for i in range(1,6):
        filename_list.append("TestData/Mod %d - muonIDEvent%d.txt" % (mod, i))
    expected_list = ["1 has one muon", "2 has one muon", "3 has two muons", "4 has one muon", "5 has 7 muons"]
    extract_function = lambda filename : get_event(filename).tracker_hits
    run_function = lambda data : analysis.muon_stub_finder.identify_muon_stubs(data)
    process_function = lambda tracks : "%d muons" % len(tracks)
    test_component(filename_list, expected_list, extract_function, run_function, process_function)

def get_true_muon_stubs(mod):
    filename_list = []
    for i in range(1,6):
        filename_list.append("TestData/Mod %d - muonIDseparateParticles%d.txt" % (mod, i))

    reader = FileReader()
    true_muon_stubs = []
    for i in range(5):
        muon_stubs = reader.get_all_muon_stubs(filename_list[i])
        true_muon_stubs.append(muon_stubs)

    return true_muon_stubs

def true_track_cluster_pairs():
    match_pairs = [[[0, 0]], [[0, 0], [1,1]], [], [[46, 3]]]
    final_pair = []
    for i in range(20):
        final_pair.append([i, i])
    match_pairs.append(final_pair)
    return match_pairs

def true_track_muon_stub_pairs():
    match_pairs = [[[0, 0]], [[1, 0]], [[0, 0], [1, 1]], [[2, 0]], [[1, 0], [4, 1], [7, 2], [10, 3], [13, 4], [16, 5], [19, 6]]]

    return match_pairs

def test_track_cluster_matcher(analysis, mod):
    tracks = get_true_tracks_for_cluster_matching(mod)
    clusters = get_true_clusters(mod)

    pairs = true_track_cluster_pairs()
    true_matches = []
    for i in range(5):
        mos = []
        for pair in pairs[i]:
            mo = MatchedObjects()
            mo.add_track(tracks[i][pair[0]])
            mo.add_cluster(clusters[i][pair[1]])
            mos.append(mo)
        true_matches.append(mos)


    for i in range(5):
        print ("\nProcessing event %d" % (i + 1))
        matches = analysis.track_cluster_matcher.match_tracks_and_clusters(tracks[i], clusters[i])
        print ("You matched: ")
        for match in matches:
            match.print_matches()
        print ("True matches:")
        for match in true_matches[i]:
            match.print_matches()



def test_track_muon_stub_matcher(analysis, mod):
    tracks = get_true_tracks_for_muon_stub_matching(mod)
    muon_stubs = get_true_muon_stubs(mod)

    pairs = true_track_muon_stub_pairs()
    true_matches = []
    for i in range(5):
        mos = []
        for pair in pairs[i]:
            mo = MatchedObjects()
            mo.add_track(tracks[i][pair[0]])
            mo.add_muon_stub(muon_stubs[i][pair[1]])
            mos.append(mo)
        true_matches.append(mos)


    for i in range(5):
        print ("\nProcessing event %d" % (i + 1))
        matches = analysis.track_muon_stub_matcher.match_tracks_and_muon_stubs(tracks[i], muon_stubs[i])
        print ("You matched: ")
        for match in matches:
            match.print_matches()
        print ("True matches:")
        for match in true_matches[i]:
            match.print_matches()

