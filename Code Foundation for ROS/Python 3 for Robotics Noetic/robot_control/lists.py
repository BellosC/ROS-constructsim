from robot_control_class import RobotControl

rc = RobotControl()

happy_list = []
happy_list = rc.get_laser_full()

print(happy_list[0], happy_list[360], happy_list[719])
