"""
This is an implementation of the K-means (or Lloyd's) algorithm using a 
simple initialization scheme of just selecting K random data points. 

As always, Wikipedia has a nice write-up for more information:
    https://en.wikipedia.org/wiki/K-means_clustering
"""
import matplotlib.pyplot as plt
import numpy as np

class KMeans:
    def __init__(self, data, k):
        self.data = data
        self.k = min(k, len(data))
        self.means = []
        self.clusters = [[] for i in range(self.k)]

    def compute_means(self, restart=False, num_iterations=1000):
        if restart or not self.means:
            # Initialize means to k random data points without replacement.
            self.means = np.take(self.data, np.random.choice(len(self.data) - 1, self.k, False), axis=0)

        prev_means = []
        for i in range(num_iterations):
            # Construct clusters.
            self.clusters = [[] for i in range(self.k)]

            for point in self.data:
                best_mean = 0
                min_dist = np.linalg.norm(point - self.means[best_mean])
                for j in range(1, self.k):
                    # Euclidean distance.
                    cur_dist = np.linalg.norm(point - self.means[j])
                    if cur_dist < min_dist:
                        best_mean = j
                        min_dist = cur_dist
                self.clusters[best_mean].append(point)

            # Update self.means.
            prev_means = self.means
            self.means = [np.average(self.clusters[j]) for j in range(self.k)]

            # Check for convergence.
            converged = True
            for j in range(self.k):
                if np.linalg.norm(prev_means[j] - self.means[j]) > 1e-7:
                    converged = False
                    break
            if converged:
                break

        return self.means, self.clusters

    def plot_clusters(self):
        plt.figure(figsize=(10, 10))
        cur = 0
        for cluster in np.asarray(self.clusters):
            # Only plot two dimensions.
            col = [[cur / self.k, cur / self.k, cur / self.k]]
            arr = np.asarray(cluster)
            plt.scatter(arr[:,0], arr[:,1], c=col)
            cur += 1
        plt.show()

def TEST_K_MEANS_WITH_2(num_tests=100):
    tests_passed = 0
    for i in range(num_tests):
        xs = np.random.normal(0, 0.1, 5)
        x2s = np.random.normal(2, 0.1, 5)
        ys = np.random.normal(0, 0.1, 5) 
        y2s = np.random.normal(2, 0.1, 5)
        data = np.column_stack((np.concatenate((xs, x2s)), np.concatenate((ys, y2s))))

        k_means = KMeans(data, 2)
        means, clusters = k_means.compute_means()
        if len(clusters[0]) == len(clusters[1]):
            tests_passed += 1
    
    print("TESTS PASSED: ", tests_passed)
    print("TOTAL TESTS: ", num_tests)
    print("Most Recent Means: ", means)
    k_means.plot_clusters()

if __name__ == '__main__':
    TEST_K_MEANS_WITH_2()
