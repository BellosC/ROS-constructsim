from robot_control_class import RobotControl

rc = RobotControl()

apostasi_apo_empodio = rc.get_laser(360)

while apostasi_apo_empodio > 1:
    rc.move_straight()
    apostasi_apo_empodio = rc.get_laser(360)
    print("current distance from wall: ", apostasi_apo_empodio)

rc.stop_robot()