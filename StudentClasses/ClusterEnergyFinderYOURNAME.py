from Track import Track

class ClusterEnergyFinderYOURNAME():
    
    def find_energy(self, cluster):
        # The cluster variable is of type Cluster

        # cal_hits is an array of CalorimeterHits
        if len(cluster.cal_hits) > 0:
            hit1 = cluster.cal_hits[0]

        # You can loop through all the points
        for point in cluster.cal_hits:

            # Each cluster contains a position...
            position = point.position

            # ...And an energy
            energy = point.energy

            # You can also see if it has been marked as a jet
            if cluster.is_jet():
                return 200

            # Each position is a vector with components
            x = position.x

            # Also some member functions
            r = position.magnitude()

            # Look in Vector.py for all the functions

        # One way or another, you should find your energy for the cluster
        energy = 20

        # Just return it, like this:
        return energy

