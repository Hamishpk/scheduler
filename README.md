# Parallel Programming Scheduler

This is a scheduler for a program that processes a list of jobs in parallel. The problem came as part of a course on Data Structures. Usually for these problems you are provided with starter files to read, a text input, and occasionally an inefficient solution in which you have to optimise. As a number of functions were needed to solve this problem, I decided to write the program from scratch and make a class.

## Task

Given a number of machines, n, and a number of jobs, m, that each take a known time to complete; what is the most effective way to schedule the jobs, so that they are completed in the fastest time possible.

In order to efficiently solve this problem the program needs to continuously identify the machine processing the job with the lowest computational time. As this will be the machine that the next job will be allocated.

Input: Text file. First line contains integers, n and m. Second line contains m integers t - the time in seconds it takes any machine to process each job.

Output: m lines containing two space separated integers. The 0-based index of the machine which will process the i-th job and the time in seconds when it will start processing that job.

## Solution

The program uses a priority queue which takes the first n jobs, uses a sift down method on each element, so that the array has the qualities of a heap. The next job is added to the machine at index 0 and the priority is again changed using the sift down function.

Both the machine index and the time is added to an array which is then printed as two space separated integers on individual lines.

The time complexity of this solution is Omlogn.

## Setup

Program is built in Python 3.6 and no additional libraries are needed.

## Testing

Program has been tested on input sizes of n and m equal to 10,000 and t equal to 100,000,000.
