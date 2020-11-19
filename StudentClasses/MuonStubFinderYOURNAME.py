from MuonStub import MuonStub

class MuonStubFinderYOURNAME():
    
    def identify_muon_stubs(self, hits):
        # hits is an unsorted list of all points
        # That includes both central tracker and muon detector points
        # You'll probably want to use a cut on distance from the origin to find the muon detector

        # Each point is a vector you can access
        my_hit = hits[0]
        
        # You can access different coordinates
        my_hit.x

        # You can also look at the magnitude of the vector, or other operations in Vector.py
        my_hit.magnitude()

        # You can loop over all the points in a vector if you want
        for hit in hits:
            hit.azimuthal()

        # This function needs to return a set of stubs, like so:
        final_muon_stubs = []

        # When you have decided which points go in a muon stub, you can do it like this:
        my_muon_stub = MuonStub()

        # Here are three of the points I have decided go with this muon stub
        my_muon_stub.add_point(hits[0])
        my_muon_stub.add_point(hits[2])
        my_muon_stub.add_point(hits[4])

        # Now add the muon_stub to the overall collection
        final_muon_stubs.append(my_muon_stub)

        # To add another muon_stub
        muon_stub2 = MuonStub()
        muon_stub2.add_point(hits[1])
        muon_stub2.add_point(hits[3])
        muon_stub2.add_point(hits[5])
        final_muon_stubs.append(muon_stub2)
        
        # Make sure to keep this line here!
        return final_muon_stubs


