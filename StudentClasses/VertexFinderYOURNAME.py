from Vector import Vector

class VertexFinderYOURNAME():
    
    def find_vertex(self, tracks):
        # Tracks is a set of Track objects, already identified

        # Access a particular track like this:
        track1 = tracks[0]

        # Hits are stored in a track like this:
        hits = track1.points

        # You can look at all the points with a for loop:
        for hit in hits:
            # Each point is a vector. You can look at each component
            y = hit.y

            # Or find the magnitude
            r = hit.magnitude()

            # Other functions can be seen in the Vector class

        # The vertex should not have an x or y component, only a z component
        # (positive or negative, with zero at the interaction point)

        vertex_z = hits[0].z

        # Once you settle on a vertex, you should return it like this:
        vertex = Vector(0, 0, vertex_z)

        return vertex
