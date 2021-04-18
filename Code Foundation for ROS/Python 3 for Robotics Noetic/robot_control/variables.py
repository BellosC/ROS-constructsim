from robot_control_class import RobotControl

rc = RobotControl()

laser1 = rc.get_laser(180)
print(laser1)

laser2 = rc.get_laser(400)
print(laser2)

laser2 = rc.get_laser(700)
print(laser2)

