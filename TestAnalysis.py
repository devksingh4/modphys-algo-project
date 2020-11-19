from FullAnalysis import FullAnalysis

from StudentClasses.ClusterEnergyFinderYOURNAME import ClusterEnergyFinderYOURNAME
from StudentClasses.ClusterFinderYOURNAME import ClusterFinderYOURNAME
from StudentClasses.ClusterPhiEtaFinderYOURNAME import ClusterPhiEtaFinderYOURNAME
from StudentClasses.MuonStubFinderYOURNAME import MuonStubFinderYOURNAME
from StudentClasses.TrackClusterMatcherYOURNAME import TrackClusterMatcherYOURNAME
from StudentClasses.TrackFinderYOURNAME import TrackFinderYOURNAME
from StudentClasses.TrackMuonStubMatcherYOURNAME import TrackMuonStubMatcherYOURNAME
from StudentClasses.TrackPhiEtaFinderYOURNAME import TrackPhiEtaFinderYOURNAME
from StudentClasses.TrackPTFinderYOURNAME import TrackPTFinderYOURNAME
from StudentClasses.VertexFinderYOURNAME import VertexFinderYOURNAME

class TestAnalysis(FullAnalysis):
    """Simple test of analysis"""

    def fill_all_finders(self):
        self.track_finder = TrackFinderYOURNAME()
        self.vertex_finder = VertexFinderYOURNAME()
        self.track_phi_eta_finder = TrackPhiEtaFinderYOURNAME()
        self.track_pT_finder = TrackPTFinderYOURNAME()
        self.cluster_finder = ClusterFinderYOURNAME()
        self.cluster_phi_eta_finder = ClusterPhiEtaFinderYOURNAME()
        self.cluster_energy_finder = ClusterEnergyFinderYOURNAME()
        self.muon_stub_finder = MuonStubFinderYOURNAME()
        self.track_cluster_matcher = TrackClusterMatcherYOURNAME()
        self.track_muon_stub_matcher = TrackMuonStubMatcherYOURNAME()


