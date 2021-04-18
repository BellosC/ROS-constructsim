def get_highest_lowest():
    from robot_control_class import RobotControl
    rc = RobotControl()

    lr_list = []
    lr_list = rc.get_laser_full()
    max_val = 0
    min_val = 100000000000000000000000
    max_pos = 0
    min_pos = 0

    for item in range(0,720):
        if lr_list[item] > max_val and lr_list[item] != float("inf"):
            max_val = lr_list[item]
            max_pos = item
        
        if  lr_list[item] < min_val:
            min_val = lr_list[item]
            min_pos = item
   
    return max_pos, min_pos

