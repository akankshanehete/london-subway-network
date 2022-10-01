ID = int
Priority = float


class PriorityQueue(object):
    def __init__(self):
        self.queue = list()

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, node: ID, priority: Priority):
        self.queue.append([node, priority])

    # priority queue returns the lowest value as having higher priority
    # shorter distance = lower value = higher priority
    def pop(self):
        try:
            low = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] <= self.queue[low][1]:
                    low = i
                lowest = self.queue[low]
            del self.queue[low]
            return lowest
        except IndexError:
            print()
            exit()

    def print(self):
        print(self.queue)
