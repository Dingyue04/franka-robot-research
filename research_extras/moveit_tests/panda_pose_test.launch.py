from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder(
            robot_name="panda",
            package_name="moveit_resources_panda_moveit_config",
        )
        .robot_description(file_path="config/panda.urdf.xacro")
        .robot_description_semantic(file_path="config/panda.srdf")
        .robot_description_kinematics(file_path="config/kinematics.yaml")
        .planning_pipelines(pipelines=["ompl"])
        .to_moveit_configs()
    )

    return LaunchDescription(
        [
            Node(
                executable="python3",
                name="panda_pose_test",
                output="screen",
                arguments=["/home/vuser/moveit_tests/panda_pose_test.py"],
                parameters=[
                    moveit_config.to_dict(),
                    "/home/vuser/moveit_tests/moveit_py.yaml",
                ],
            )
        ]
    )
