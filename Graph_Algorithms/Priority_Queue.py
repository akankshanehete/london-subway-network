class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, node, priority):
        self.queue.append([node, priority])

    def pop(self):
        try:
            high = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[high][1]:
                    high = i
                highest = self.queue[high]
                del self.queue[high]
                return highest
        except IndexError:
            print()
            exit()
