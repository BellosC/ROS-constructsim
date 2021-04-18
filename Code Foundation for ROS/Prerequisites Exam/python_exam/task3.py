from robot_control_class import RobotControl

class ExamControl:
    
    def __init__(self):
        self.rc = RobotControl()

    def get_laser_readings(self,left=719, right=0):
        self.rc.get_laser(left)
        self.rc.get_laser(right)
        return self.rc.get_laser(left), self.rc.get_laser(right)

    def main(self, left=719, right=0):
        while self.rc.get_laser(left) != float("inf") or self.rc.get_laser(right) != float("inf"):
            self.rc.move_straight()
          
        self.rc.stop_robot()
        self.rc.get_laser(right)
 


