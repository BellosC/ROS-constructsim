from robot_control_class import RobotControl
rc = RobotControl(robot_name="summit")

rc.move_straight_time("forward", 2, 5)
rc.turn("clockwise", 2, 7)
