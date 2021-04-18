from robot_control_class import RobotControl

class MoveRobot:
    def __init__(self, motion, clockwise, speed, time):
        self.robotcontrol = RobotControl(robot_name="summit")
        self.motion = motion
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 7.0 # This is an estimate time in which the robot will rotate 90 degrees

    def do_square(self):

        i = 0

        while (i < 4):
            self.move_straight()
            self.turn()
            i+=1

    def move_straight(self):
        self.robotcontrol.move_straight_time(self.motion, self.speed, self.time)

    def turn(self):
        self.robotcontrol.turn(self.clockwise, self.speed, self.time_turn)


mr1 = MoveRobot('forward', 'clockwise', 0.3, 4)
mr1.do_square()
mr2 = MoveRobot('forward', 'clockwise', 0.3, 8)
mr2.do_square()
















'''----my_solution----
from robot_control_class import RobotControl
rc = RobotControl(robot_name="summit")

class square:
    def __init__(self, size):
        self.size_of_side = size
    
    def perform_square(self):
        rc.move_straight_time("forward", 0.3, self.size_of_side)
        rc.turn("clockwise", 0.2, 12.9)
        rc.move_straight_time("forward", 0.3, self.size_of_side)
        rc.turn("clockwise", 0.2, 12.9)
        rc.move_straight_time("forward", 0.3, self.size_of_side)
        rc.turn("clockwise", 0.2, 12.9)
        rc.move_straight_time("forward", 0.3, self.size_of_side)
        rc.move_straight_time("forward", 0.3, self.size_of_side)
        rc.turn("clockwise", 0.2, 12.9)
        rc.move_straight_time("forward", 0.3, 2*self.size_of_side)
        rc.turn("clockwise", 0.2, 12.9)
        rc.move_straight_time("forward", 0.3, 2*self.size_of_side)
        rc.turn("clockwise", 0.2, 12.9)
        rc.move_straight_time("forward", 0.3, 2*self.size_of_side)
        rc.turn("clockwise", 0.2, 12.9)
        rc.move_straight_time("forward", 0.3, 2*self.size_of_side)
        
rc.move_straight_time("forward", 0.3, 3)
costas = square(4)
costas.perform_square()
move_straight_time'''