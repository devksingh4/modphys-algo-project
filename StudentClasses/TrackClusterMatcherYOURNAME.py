from MatchedObjects import MatchedObjects

class TrackClusterMatcherYOURNAME():
    
    def match_tracks_and_clusters(self, tracks, clusters):
        # Tracks and clusters are stored in these two lists

        # Your job is to pair them together

        # Track objects are in a list:
        track1 = tracks[0]

        # So are cluster objects
        # You can loop over them if you want:
        for cluster in clusters:
            energy = cluster.energy

        # Tracks include their raw hits but also their calculated vertex, phi, eta, and pT
        pT = track1.pT

        # Clusters include their raw hits but also their calculated phi, eta, and energy, and whether they were marked as jets
        energy = clusters[0].energy

        # This function needs to return a set of matched objects, like so:
        final_matched_objects = []

        # Create a new matched object for each track or cluster:
        matched_objects_1 = MatchedObjects()
        matched_objects_1.add_track(tracks[0])

        # If a cluster matches a track, add it to the same matched_object
        matched_objects_1.add_cluster(clusters[0])

        # If nothing matches, the matched object can only contain a track or a cluster
        matched_objects_2 = MatchedObjects()
        if len(tracks) > 1:
            matched_objects_2.add_track(tracks[1])

        matched_objects_3 = MatchedObjects()
        if len(clusters) > 1:
            matched_objects_3.add_cluster(clusters[1])

        # Each matched object should be added to the final list:
        final_matched_objects.append(matched_objects_1)
        final_matched_objects.append(matched_objects_2)
        final_matched_objects.append(matched_objects_3)
        
        # Make sure to keep this line here!
        return final_matched_objects


