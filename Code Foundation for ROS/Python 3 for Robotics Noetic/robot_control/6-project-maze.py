from robot_control_class import RobotControl
rc = RobotControl()



while rc.get_laser(360) > 1:
    rc.move_straight()

rc.stop_robot()
rc.rotate(80)
rc.stop_robot()

while rc.get_laser(360) > 1:
    rc.move_straight()
rc.stop_robot()
rc.rotate(80)
rc.stop_robot()

while rc.get_laser(360) > 1:
    rc.move_straight()
rc.stop_robot()
rc.rotate(-90)
rc.stop_robot()
print (rc.get_laser_full())

rc.move_straight_time("forward", 0.5, 7)
rc.turn("clockwise", 0.2,2)
rc.move_straight_time("forward", 0.5, 7)