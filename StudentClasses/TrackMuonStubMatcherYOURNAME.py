from MatchedObjects import MatchedObjects

class TrackMuonStubMatcherYOURNAME():
    
    def match_tracks_and_muon_stubs(self, tracks, muon_stubs):
        # Tracks and muon_stubs are stored in these two lists

        # Your job is to pair them together

        # Track objects are in a list:
        track1 = tracks[0]

        # So are muon stub objects
        # You can loop over them if you want:
        for muon_stub in muon_stubs:
            if len(muon_stub.hits) > 0:
                position = muon_stub.hits[0]

        # Tracks include their raw hits but also their calculated vertex, phi, eta, and pT
        pT = track1.pT

        # muon_stubs include their raw hits only
        if len(muon_stubs) > 0 and len(muon_stubs[0].hits) > 0:
            z_position = muon_stubs[0].hits[0].z

        # This function needs to return a set of matched objects, like so:
        final_matched_objects = []

        # Create a new matched object for each track or muon stub:
        matched_objects_1 = MatchedObjects()
        matched_objects_1.add_track(tracks[0])

        # If a muon stub matches a track, add it to the same matched_object
        matched_objects_1.add_muon_stub(muon_stubs[0])

        # If nothing matches, the matched object can only contain a track or a muon stub
        matched_objects_2 = MatchedObjects()
        if (len(tracks) > 1):
            matched_objects_2.add_track(tracks[1])

        matched_objects_3 = MatchedObjects()
        if (len(muon_stubs) > 1):
            matched_objects_3.add_muon_stub(muon_stubs[1])

        # Each matched object should be added to the final list:
        final_matched_objects.append(matched_objects_1)
        final_matched_objects.append(matched_objects_2)
        final_matched_objects.append(matched_objects_3)
        
        # Make sure to keep this line here!
        return final_matched_objects


