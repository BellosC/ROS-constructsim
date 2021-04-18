from robot_control_class import RobotControl

rc = RobotControl()

users_number = int(input("Give me a number from 0 to 719: "))
users_laser = rc.get_laser(users_number)

print(users_laser)