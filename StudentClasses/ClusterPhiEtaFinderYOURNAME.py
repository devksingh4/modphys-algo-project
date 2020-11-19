from Track import Track

class ClusterPhiEtaFinderYOURNAME():
    
    def find_phi_eta(self, cluster):
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
                return -1, -2

            # Each position is a vector with components
            x = position.x

            # Also some member functions
            r = position.magnitude()

            # Look in Vector.py for all the functions

        # One way or another, you should find your phi and eta for the cluster
        phi = 1
        eta = 2

        # Just return them, like this:
        return phi, eta

