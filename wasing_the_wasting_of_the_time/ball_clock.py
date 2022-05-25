class Ball:
    def __init__(self, number):
        self.number = number
    
    def __str__(self):
        return str(self.number)
    

class Rack:
    def __init__(self, capacity, base = None, next = None):
        self.capacity = capacity
        self.base = base
        self.next = next
        self.track = []
    
    def add_ball(self, ball):
        if len(self.track) == self.capacity:
            if self.next:
                self.next.add_ball(ball)
            else:
                self.base.add_ball(ball)
            self.clear()
        else:
            self.track.append(ball)
    
    def clear(self):
        while len(self.track) > 0:
            ball = self.track.pop(0)
            if self.base:
                self.base.add_ball(ball)
    
    def pop(self):
        return self.track.pop(0)

    def __str__(self):
        ret = str(len(self.track)) + ": "
        for ball in self.track:
            ret += str(ball) + " "
        return ret


class Ball_Clock:
    def __init__(self, capacity = 100):
        if capacity < 100:
            capacity = 100
        self.base = Rack(capacity)
        self.hours = Rack(23, base=self.base)
        self.fives = Rack(11, base = self.base, next = self.hours)
        self.ones = Rack(4, base = self.base, next = self.fives)
        self.seconds = Rack(59, base = self.base, next = self.ones)

        for i in range(1,capacity+1):
            self.base.add_ball(Ball(i))
    
    def __str__(self):
        ret = ""

        ret += "Base\n"
        ret += str(self.base)

        ret += "\n\nHours:\n"
        ret += str(self.hours)

        ret += "\n\nFives:\n"
        ret += str(self.fives)

        ret += "\n\nOnes:\n"
        ret += str(self.ones)

        ret += "\n\nSeconds:\n"
        ret += str(self.seconds)

        return ret

    def tick(self):
        self.seconds.add_ball(self.base.pop())
    
    def order(self):
        order = list()
        for ball in self.base.track:
            order.append(ball.number * 7)
        
        for ball in self.hours.track:
            order.append(ball.number * 5)
        
        for ball in self.fives.track:
            order.append(ball.number * 3)

        for ball in self.ones.track:
            order.append(ball.number * 2)
        
        for ball in self.seconds.track:
            order.append(ball.number)
        
        return order
    

if __name__ == "__main__":
    import time
    import os
    SLEEP_TIME = 1 - 0.00500001633
    NUM_TICKS = 25000

    clock = Ball_Clock(1000)
    
    start = time.time()
    for i in range(NUM_TICKS):
        os.system("clear")
        print(i)
        clock.tick()
        print(clock)
        time.sleep((i/NUM_TICKS)**100)
        
    
    print(f"{NUM_TICKS} ticks took {time.time()-start} sec")

        
        
