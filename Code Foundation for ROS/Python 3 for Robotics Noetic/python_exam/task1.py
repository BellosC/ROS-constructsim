def get_highest_lowest():
    from robot_control_class import RobotControl
    rc = RobotControl()

    laser_readings = []
    laser_readings = rc.get_laser_full()
    max = 0
    low = 1000000000000000000000
    for costas in range(0,720):
        if laser_readings[costas] > max and laser_readings[costas] != float("inf"):
            max = laser_readings[costas]
            max_pos = costas
        if laser_readings[costas] < low:
            min = laser_readings[costas]
            min_pos = costas

    
    
    return max_pos, min_pos
    
    

