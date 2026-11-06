# Source Revisions at Archive Time

The source files are committed as ordinary files so that one clone restores
the full workspace. The original nested Git repositories were intentionally
removed, and their source revisions are recorded here.

| Source tree | Revision | Upstream |
| --- | --- | --- |
| Franka ROS 2 workspace | `29cb85a677b8` | `frankarobotics/franka_ros2` |
| `franka_description` | `4143b50061f8` | `frankarobotics/franka_description` |
| `gz_ros2_control` | `816891ae04cb` | `ros-controls/gz_ros2_control` |
| `libfranka` | `3cc708cafa1c` | `frankarobotics/libfranka` |
| `olvx_descriptions_module` | `c3444ed77423` | `olive-robotics/olvx_descriptions_module` |
| `ros2_control` | `6e50df38c97a` | `ros-controls/ros2_control` |
| `ros2_robotiq_gripper` | `3b6cf8ff9106` | `PickNikRobotics/ros2_robotiq_gripper` |
| `serial` | `d8d160678aa0` | `tylerjw/serial` |
| `zed_description` | `1aa88b319897` | `stereolabs/zed-ros2-description` |
| `external/mujoco_ros2_control` | `fa7dc13899ad` | `dfki-ric/mujoco_ros2_control` |

The working-tree modifications present at archive time are preserved in this
repository's initial commit, including changes under `franka_fr3_moveit_config`,
`franka_description`, and `ros2_control`.
