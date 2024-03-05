import numpy as np

class DBSCAN:
    def __init__(self, eps, min_pts):
        self.eps = eps
        self.min_pts = min_pts

    def fit(self, D):
        self.labels = [0] * len(D)
        self.cluster = 0

        for i in range(len(D)):
            if self.labels[i] != 0:
                continue
            
            neighbors = self.get_neighbors(D, i)
            
            if len(neighbors) < self.min_pts:
                self.labels[i] = -1
            else:
                self.cluster += 1
                self.expand_cluster(D, i, neighbors, self.cluster)

    def expand_cluster(self, D, i, neighbors, cluster):
        self.labels[i] = cluster

        for neighbor in neighbors:
            if self.labels[neighbor] == 0:
                self.labels[neighbor] = cluster
                neighbor_neighbors = self.get_neighbors(D, neighbor)
                
                if len(neighbor_neighbors) >= self.min_pts:
                    neighbors.extend(neighbor_neighbors)

            elif self.labels[neighbor] == -1:
                self.labels[neighbor] = cluster

    def get_neighbors(self, D, i):
        neighbors = []
        for j in range(len(D)):
            if np.linalg.norm(D[i] - D[j]) < self.eps:
                neighbors.append(j)
        return neighbors

# Main
if __name__ == "__main__":
    np.random.seed(0)
    D = np.array([
    [0, 0],
    [1, 3],
    [2, 0],
    [3, 0],
    [0, 1],
    [1, 1],
    [2, 1],
    [0, 3],
    [1, 2],
    ])
    dbscan = DBSCAN(eps=2, min_pts=3)
    dbscan.fit(D)
    print("Cluster labels:", dbscan.labels)