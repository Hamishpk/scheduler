# python3

class Scheduler:
    """
    SUMMARY
    ----
    Simulates a program that processes a list of jobs in parallel.

    INPUT
    ----
    Reads a text input. First line first line containing two intergers:
    n - Number of machines
    m - Number of jobs
    The second line contains m integers ti — the times in seconds it
    takes any thread to process i-th job.

    OUTPUT
    ----
    m lines of 2 space seperated intigers. the 0-based index of the thread
    which will process the i-th job and the time in seconds when it will
    start processing that job.

    """

    def __init__(self):
        self.n_workers, self.m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.heap = [[0, 0] for i in range(self.n_workers)]
        self.workers = [None] * self.m
        self.times = [0] * self.m


    def initialise_queue(self):
        """
        Initialises the priority queue
        ----

        Takes the first m jobs and arranges them such that that the machines
        processing the smallest jobs are moved to the front of the array.

        Calls sift_down() in order to change priority.

        """
        worker = 0
        for i in range(min(self.n_workers, self.m)):
            self.heap[i] = [self.jobs[i], i]
            self.workers[i] = worker
            worker += 1
            self.times[i] = 0
        for i in range(self.n_workers // 2, -1, -1):
            self.sift_down(i)


    def sift_down(self, i):
        """
        Compares element with both it's childern. If element is larger it is swapped
        so that the heap property is maintained.
        ---

        Takes the index of the element to compare, i as a parameter.
        """
        min_index = i
        left = (2 * i) + 1 if ((2 * i) + 1 < self.n_workers) else -1
        right = (2 * i) + 2 if ((2 * i) + 2 < self.n_workers) else -1

        if (left != -1) and ((self.heap[min_index][0] > self.heap[left][0]) or
            (self.heap[left][0] == self.heap[min_index][0] and
            self.heap[left][1] < self.heap[min_index][1])):
            min_index = left

        if (right != -1) and ((self.heap[min_index][0] > self.heap[right][0]) or
            (self.heap[right][0] == self.heap[min_index][0] and
            self.heap[right][1] < self.heap[min_index][1])):
            min_index = right

        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.sift_down(min_index)


    def assign_jobs(self):
        """
        Assigns the remaining jobs to the next available machine. Adding the
        time required to process the ith job to the total time of the next available
        machine.

        Records which machine takes the job at what time and records these as
        workers[i] and times[i].
        """
        self.initialise_queue()
        last_time = 0
        if self.m > self.n_workers:
            for i in range(self.n_workers, self.m):
                self.sift_down(0)
                last_time = self.heap[0][0]
                self.workers[i] = self.heap[0][1]
                self.times[i] = last_time
                self.heap[0][0] += self.jobs[i]


    def write_result(self):
        """
        Prints results of which machine takes the next job and the time it takes it.
        """
        for i in range(self.m):
            print(self.workers[i], self.times[i])

    def main(self):
        self.initialise_queue()
        self.assign_jobs()
        self.write_result()

if __name__ == '__main__':
    answer = Scheduler()
    answer.main()
