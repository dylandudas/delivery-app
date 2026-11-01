
# Convenient tool for taking address strings, determining indices in matrix
# and using them to search and determine distance between locations
class DistanceTool:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_index(self, address):
        i = 0
        for row in self.matrix:
            if address in row:
                return i
            i += 1
        return None

    def get_distances(self, address1, address2):
        index1 = self.get_index(address1)
        index2 = self.get_index(address2)

        if index1 is not None and index2 is not None:
            if index1 > index2:
                return float(self.matrix[index1][index2 + 1])

            return float(self.matrix[index2][index1 + 1])

        else:
            print("error getting distance for " + address1 + " and " + address2 + ". Index1: " + str(index1) + " Index2: " + str(index2))
            return None