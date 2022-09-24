class PriorityQueue(object):
    def __init__(self):
        self.queue = list()

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, node, priority):
        self.queue.append([node, priority])

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
