import TestClasses.TrackTester

from StudentClasses.TrackPhiEtaFinderDevSingh import *

from FullAnalysis import FullAnalysis

analysis = FullAnalysis()
mod = 2

analysis.track_phi_eta_finder = TrackPhiEtaFinderDevSingh()

TestClasses.TrackTester.test_track_phi_eta_finder(analysis, mod)