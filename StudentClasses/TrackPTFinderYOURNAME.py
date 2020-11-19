from Track import Track

class TrackPTFinderYOURNAME():
    
    def find_pT(self, track):
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

        # One way or another, you should find your pT for the track
        pT = 20

        # Just return it, like this:
        return pT

