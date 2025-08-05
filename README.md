# Custom Quadruped Walking Policy Training with Reinforcement Learning (IsaacLab)
This repository contains a custom configuration for training a quadruped robot (Spot) to walk on flat/Rough terrain using IsaacLab. The project leverages reinforcement learning with the RSL RL algorithm, with modifications to enhance stability and reduce jumping. After training for over 35,000 iterations on Flat terrain, the robot demonstrates a stable walking policy, as evidenced by the checkpoint videos.

## Overview
- **Platform**: IsaacLab (integrated with NVIDIA Isaac Sim)
- **Task**: Train a quadruped robot to walk on flat/Rough terrain
- **Training Duration**: Over 35,000 iterations (approximately 53 million timesteps).. Training Crash Due to RuntimeError: normal expects all elements of std >= 0.0
 
	```bash
	RuntimeError: normal expects all elements of std >= 0.0
	```
 Notice: The training Took around 8 Hours to reach 35,403 iterations before it stopped. with harware specification: NVIDIA GeForce RTX 4060(8 Cores).
- **Status**: Successfully learned a stable walking policy with a mean reward of 44.74 and no fall terminations

## Modifications
The following key changes were made to the configuration to improve the robot's performance:
- **flat_env_cfg.py**: Adjusted reward weights to reduce the incentive for jumping and emphasize stable walking. Specifically:
  - Reduced `feet_air_time` weight to 0.05 (from 0.25) to discourage excessive jumping.
  - Increased `track_lin_vel_xy_exp` weight to 2.0 (from 1.5) and `track_ang_vel_z_exp` to 1.0 (from 0.75) to prioritize velocity tracking.
  - Lowered `flat_orientation_l2` weight to -1.0 (from -2.5) to reduce over-penalty on orientation.
- **custom_quad.py**: Tuned actuator settings(on Isaacsim, when configuring the USD) for better control:
  - Reduced stiffness to 40 (from 60) and increased damping to 3.0 (from 1.5) to smooth movements.
  - Adjusted initial joint positions to a more stable upright stance (e.g., `F[L,R]_thigh_joint` to -π/36 from -5π/18).
- **rough_env_cfg.py**: Reward weights adjusted similarly to `flat_env_cfg.py` for consistency, with terrain-specific settings unchanged.

## Usage
To replicate or resume the training:
1. **Install IsaacLab**: Follow the official IsaacLab installation guide[](https://isaaclab-docs.xai.org/).
2. **Clone this Repository**: 
   ```bash
   git clone https://github.com/yayabash/CustomQuadrupedRobotTraining.git
   cd CustomQuadrupedRobotTraining
   ```
## Run Training

	```bash
	./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Velocity-Flat-Custom-Quad-v0 --num_envs 64 --video
	```
	
## Monitor Progress: Use TensorBoard for real-time metrics:

	```bash
	tensorboard --logdir=/path/to/logs/rsl_rl/custom_quad_flat/ --port=your_port
	```
	
## To play training

	```bash
	./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py   --task=Isaac-Velocity-Flat-Custom-Quad-v0   --num_envs 64 --checkpoint /path/to/last_checkpoint
	```
	
