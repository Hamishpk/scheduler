# python3

class Scheduller:
    """

    """
    def read_data(self):
        self.n_workers, self.m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.heap = [[0, 0] for i in range(self.n_workers)]
        self.workers = [None] * self.m
        self.times = [0] * self.m


    def initialise_queue(self):
        worker = 0
        for i in range(min(self.n_workers, self.m)):
            self.heap[i] = [self.jobs[i], i]
            self.workers[i] = worker
            worker += 1
            self.times[i] = 0
        for i in range(self.n_workers // 2, -1, -1):
            self.sift_down(i)

    def assign_jobs(self):
        self.initialise_queue()
        last_time = 0
        if self.m > self.n_workers:
            for i in range(self.n_workers, self.m):
                self.sift_down(0)
                last_time = self.heap[0][0]
                self.workers[i] = self.heap[0][1]
                self.times[i] = last_time
                self.heap[0][0] += self.jobs[i]

    def sift_down(self, i):
        min_index = i
        left = (2 * i) + 1 if ((2 * i) + 1 < self.n_workers) else -1
        right = (2 * i) + 2 if ((2 * i) + 2 < self.n_workers) else -1

        if (left != -1) and ((self.heap[min_index][0] > self.heap[left][0]) or (self.heap[left][0] == self.heap[min_index][0] and self.heap[left][1] < self.heap[min_index][1])):
            min_index = left
        if (right != -1) and ((self.heap[min_index][0] > self.heap[right][0]) or (self.heap[right][0] == self.heap[min_index][0] and self.heap[right][1] < self.heap[min_index][1])):
            min_index = right

        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.sift_down(min_index)



    def heapify(self):
        pass

    def write_result(self):
        for i in range(self.m):
            print(self.workers[i], self.times[i])

    def main(self):
        self.read_data()
        self.initialise_queue()
        self.assign_jobs()
        self.write_result()

if __name__ == '__main__':
    answer = Scheduller()
    answer.main()
