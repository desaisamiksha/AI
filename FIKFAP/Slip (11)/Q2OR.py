class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_position = 'A'
        self.box_position = 'B'
        self.bananas_position = 'B'
        self.box_climbed = False
    
    def move(self, position):
        print(f"Monkey moves from {self.monkey_position} to {position}.")
        self.monkey_position = position
    
    def push_box(self, position):
        if self.monkey_position == self.box_position:
            print(f"Monkey pushes box from {self.box_position} to {position}.")
            self.box_position = position
            self.monkey_position = position
        else:
            print("Monkey is not in the same position as the box to push it.")
    
    def climb_box(self):
        if self.monkey_position == self.box_position:
            self.box_climbed = True
            print("Monkey climbs the box.")
        else:
            print("Monkey is not at the box position to climb it.")
    
    def grab_bananas(self):
        if (self.monkey_position == self.bananas_position 
            and self.monkey_position == self.box_position 
            and self.box_climbed):
            print("Monkey grabs the bananas!")
            return True
        else:
            print("Monkey can't reach the bananas.")
            return False

def main():
    problem = MonkeyBananaProblem()
    
    
    problem.move('B')
    
    
    problem.push_box('B')
    
    
    problem.climb_box()
    
    
    if problem.grab_bananas():
        print("Success: Monkey has the bananas!")
    else:
        print("Failure: Monkey does not have the bananas.")

if __name__ == "__main__":
    main()