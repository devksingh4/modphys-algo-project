from Track import Track

class TrackPhiEtaFinderDevSingh():
    
    def find_phi_eta(self, track):
        # The track variable is of type Track

        # Of the Track variables, only points and vertex will be filled at this point
        vertex = track.vertex

        # points is an array of vectors
        point1 = track.points[0]

        # You can loop through all the points
        for point in track.points:

            # Each point is a vector with components
            x = point.x

            # Also some member functions
            r = point.magnitude()

            # Look in Vector.py for all the functions

        # One way or another, you should find your phi and eta for the track
        phi = 1
        eta = 2

        # Just return them, like this:
        return phi, eta

