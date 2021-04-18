from robot_control_class import RobotControl
rc = RobotControl(robot_name="summit")

rc.move_straight_time("forward", 0.2, 5)
rc.turn("counter-clockwise", 0.2, 13)
rc.move_straight_time("forward", 0.2, 10)
rc.turn("counter-clockwise", 0.2, 11)
rc.move_straight_time("forward", 0.2, 10)

print("Bellos is my lord and savior")
