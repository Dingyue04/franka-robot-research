# Dingyue Franka Robot Research Archive

This private repository is a reproducible source snapshot of the summer Franka
FR3 / ROS 2 research workspace. It was assembled from
`/home/vuser/franka_ros2` before the original virtual machine is cleaned up.

## Included

- The complete local Franka ROS 2 source workspace
- Local FR3 MoveIt, Pilz LIN, fake-controller, URDF/SRDF, and ros2_control changes
- Vendored dependency source trees and robot/model assets
- Docker, compose, dependency, patch, and launch configuration
- `research_extras/moveit_tests`: early MoveIt experiments
- `research_extras/screenshots`: available research screenshots
- `external/mujoco_ros2_control`: the clean upstream MuJoCo ROS 2 dependency
  snapshot used during the work

## Intentionally excluded

- All original and nested `.git` metadata
- `.env` and other machine-local environment settings
- Generated `build`, `install`, and `log` directories
- Python bytecode, IDE state, and caches

To configure the Docker workspace, copy `.env.example` to `.env` and adjust
the UID, GID, and container name for the new machine.

Archive owner and commit identity: `Dingyue04`.
