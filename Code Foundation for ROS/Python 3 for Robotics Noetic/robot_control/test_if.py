from robot_control_class import RobotControl

rc = RobotControl()


apostasi_apo_empodio = rc.get_laser(360)

if apostasi_apo_empodio < 1:
    rc.stop_robot()
else: 
    rc.move_straight()

print("the laser value was: ", apostasi_apo_empodio)