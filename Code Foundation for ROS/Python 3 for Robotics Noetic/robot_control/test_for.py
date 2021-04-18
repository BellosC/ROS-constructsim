from robot_control_class import RobotControl

rc = RobotControl()

readings = []
readings = rc.get_laser_full()  

bigger = 0
for metrisi in readings:
    if metrisi > bigger:
        bigger=metrisi

print("THe higher value is: ", bigger)