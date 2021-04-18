from robot_control_class import RobotControl
rc = RobotControl(robot_name="summit")

def int3(x, y, z):
    num1=rc.get_laser_summit(x)
    num2=rc.get_laser_summit(y)
    num3=rc.get_laser_summit(z)
  
        
    return [num1, num2, num3]

j=int3(3, 34, 434)
print(j)

