from robot_control_class import RobotControl

rc = RobotControl()

happy_list = []

happy_list = rc.get_laser_full()

happy_dictiionary = {
    "Position 0: ":happy_list[0], 
    "Position 100 ":happy_list[100],
    "Position 200 ":happy_list[200], 
    "Position 300 ":happy_list[300], 
    "Position 400 ":happy_list[400], 
    "Position 500 ":happy_list[500], 
    "Position 600 ":happy_list[600], 
    "Position 719 ":happy_list[719], 
}

print(happy_dictiionary)