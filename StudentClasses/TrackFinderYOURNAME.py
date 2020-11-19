from Track import Track

class TrackFinderYOURNAME():
    
    def identify_tracks(self, hits):
        # hits is an unsorted list of all points

        # Each point is a vector you can access
        my_hit = hits[0]
        
        # You can access different coordinates
        my_hit.x

        # You can also look at the magnitude of the vector, or other operations in Vector.py
        my_hit.magnitude()

        # You can loop over all the points in a vector if you want
        for hit in hits:
            hit.azimuthal()

        # This function needs to return a set of tracks, like so:
        final_tracks = []

        # When you have decided which points go in a track, you can do it like this:
        my_track = Track()

        # Here are three of the points I have decided go with this track
        my_track.add_point(hits[0])
        my_track.add_point(hits[2])
        my_track.add_point(hits[4])

        # Now add the track to the overall collection
        final_tracks.append(my_track)

        # To add another track
        track2 = Track()
        track2.add_point(hits[1])
        track2.add_point(hits[3])
        final_tracks.append(track2)
        
        # Make sure to keep this line here!
        return final_tracks


