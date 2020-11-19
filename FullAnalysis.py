from MatchedObjects import MatchedObjects

class FullAnalysis():
    """Base class for a full analysis suite"""

    def combine_match_sets(self, set1, set2):
        final_matches = []
        for match1 in set1:
            already_done = []
            for match2 in set2:
                if match2 in already_done:
                    continue
                if match1.can_merge(match2):
                    final_matches.append(match1.merge(match2))
                    already_done.append(match2)
                    break 
            else:
                final_matches.append(match1)

        for match2 in set2:
            if not match2 in already_done:
                final_matches.append(match2)

        return final_matches


    def run(self, event):
        tracks = self.track_finder.identify_tracks(event.tracker_hits)
        vertex = self.vertex_finder.find_vertex(tracks)

        for track in tracks:
            track.set_vertex(vertex)
            phi, eta = self.track_phi_eta_finder.find_phi_eta(track)
            track.set_phi(phi)
            track.set_eta(eta)
            pT = self.track_pT_finder.find_pT(track)
            track.set_pT(pT)

        clusters = self.cluster_finder.identify_clusters(event.calorimeter_hits)

        for cluster in clusters:
            phi,eta = self.cluster_phi_eta_finder.find_phi_eta(cluster)
            cluster.set_phi(phi)
            cluster.set_eta(eta)
            energy = self.cluster_energy_finder.find_energy(cluster)
            cluster.set_energy(energy)

        muon_stubs = self.muon_stub_finder.identify_muon_stubs(event.tracker_hits)

        simple_matches = []
        for track in tracks:
            temp_obj = MatchedObjects()
            temp_obj.add_track(track)
            simple_matches.append(temp_obj)
        for cluster in clusters:
            temp_obj = MatchedObjects()
            temp_obj.add_cluster(cluster)
            simple_matches.append(temp_obj)
        for muon_stub in muon_stubs:
            temp_obj = MatchedObjects()
            temp_obj.add_muon_stub(muon_stub)
            simple_matches.append(temp_obj)

        cluster_matches = self.track_cluster_matcher.match_tracks_and_clusters(tracks, clusters)
        muon_stub_matches = self.track_muon_stub_matcher.match_tracks_and_muon_stubs(tracks, muon_stubs)

        final_matches = []

        final_matches = self.combine_match_sets(simple_matches, cluster_matches)
        final_matches = self.combine_match_sets(final_matches, muon_stub_matches)

        pass
