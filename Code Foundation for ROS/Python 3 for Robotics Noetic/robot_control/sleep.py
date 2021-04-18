from robot_control_class import RobotControl
import time 
rc=RobotControl(robot_name="summit")

def move_x_seconds(secs):
    rc.move_straight()
    time.sleep(secs)
    rc.stop_robot()

move_x_seconds(5)