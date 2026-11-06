import os
import time

import rclpy
from geometry_msgs.msg import PoseStamped
from moveit.planning import MoveItPy


def main():
    rclpy.init()

    panda = MoveItPy(node_name="panda_pose_test")
    panda_arm = panda.get_planning_component("panda_arm")

    panda_arm.set_start_state_to_current_state()

    pose_goal = PoseStamped()
    pose_goal.header.frame_id = "panda_link0"

    pose_goal.pose.orientation.x = 0.0
    pose_goal.pose.orientation.y = 0.0
    pose_goal.pose.orientation.z = 0.0
    pose_goal.pose.orientation.w = 1.0

    # Probing approach pose: safe point above the sample.
    pose_goal.pose.position.x = 0.40
    pose_goal.pose.position.y = 0.00
    pose_goal.pose.position.z = 0.45

    panda_arm.set_goal_state(
        pose_stamped_msg=pose_goal,
        pose_link="panda_link8",
    )

    plan_result = panda_arm.plan()

    if plan_result:
        print("Plan succeeded, executing approach pose...")
        panda.execute(plan_result.trajectory, controllers=[])
        print("Approach pose reached.")
    else:
        print("Planning failed.")

    time.sleep(1.0)

    # Temporary workaround for the MoveItPy shutdown crash in this demo.
    os._exit(0)


if __name__ == "__main__":
    main()
