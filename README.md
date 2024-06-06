# URDF and MoveIt
### Repository to Visualize Fanuc M-710iC/45M robot from URDF file and generate MoveIt configuration

Steps to execute: 
```
mkdir ros2_ws/src
cd ros2_ws
Clone the repo
colcon build
source install/setup.bash
```

To view the robot in Rviz:
```
ros2 launch fanuc_m710ic_support view_robot.launch.py
```

Once Rviz Open, follow the below steps:
1. Sep Map to base_link in the Global Options
2. Add Robot Model
3. Under Robot Model, set description to /robot_description
4. Then in another terminal, run  the below command
```
ros2 run fanuc_m710ic_support publish_joint_states
```

To open MoveIt Setup Assistant: 
```
ros2 launch moveit_setup_assistant setup_assistant.launch.py
```

To launch MoveIt: 
```
ros2 launch fanuc_m710ic_support_moveit_config demo.launch.py
```

Note: Error occurs while launching demo.launch.py (MoveIt) - Fix needed
