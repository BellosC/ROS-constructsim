from robot_control_class import RobotControl
rc = RobotControl()

while rc.get_laser(360) > 1:
    rc.move_straight()

rc.stop_robot()
rc.rotate(75)