from Cluster import Cluster

class ClusterFinderYOURNAME():
    
    def identify_clusters(self, cal_hits):
        # cal_hits is an unsorted list of all calorimeter readings

        # Each point is a CalorimeterHit object you can access
        my_hit = cal_hits[0]
        
        # Each cal_hit has a position vector...
        position = my_hit.position

        # ...and an energy
        energy = my_hit.energy

        # You can access different coordinates
        x = position.x

        # You can also look at the magnitude of the vector, or other operations in Vector.py
        mag = position.magnitude()

        # You can loop over all the points in a vector if you want
        for hit in cal_hits:
            hit.position.azimuthal()

        # This function needs to return a set of clusters, like so:
        final_clusters = []

        # When you have decided which points go in a cluster, you can do it like this:
        my_cluster = Cluster()

        # Here are three of the points I have decided go with this track
        my_cluster.add_hit(cal_hits[0])
        my_cluster.add_hit(cal_hits[2])
        my_cluster.add_hit(cal_hits[4])

        # Now add the cluster to the overall collection
        final_clusters.append(my_cluster)

        # To add another cluster
        cluster2 = Cluster()
        cluster2.add_hit(cal_hits[1])
        cluster2.add_hit(cal_hits[3])
        cluster2.add_hit(cal_hits[5])
        final_clusters.append(cluster2)

        # If the cluster is a jet (instead of an electron or photon or muon), mark it:
        cluster2.mark_jet()
        
        # Make sure to keep this line here!
        return final_clusters


