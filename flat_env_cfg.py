from isaaclab.utils import configclass

from .rough_env_cfg import CustomQuadRoughEnvCfg


@configclass
class CustomQuadFlatEnvCfg(CustomQuadRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # override rewards
        self.rewards.flat_orientation_l2.weight = -1.0  # Reduced from -2.5 to lessen orientation penalty
        self.rewards.feet_air_time.weight = 0.05  # Reduced from 0.25 to discourage excessive jumping
        self.rewards.track_lin_vel_xy_exp.weight = 2.0  # Increased from 1.5 to prioritize velocity tracking
        self.rewards.track_ang_vel_z_exp.weight = 1.0  # Increased from 0.75 to balance angular control

        # change terrain to flat
        self.scene.terrain.terrain_type = "plane"
        self.scene.terrain.terrain_generator = None
        # no height scan
        self.scene.height_scanner = None
        self.observations.policy.height_scan = None
        # no terrain curriculum
        self.curriculum.terrain_levels = None


class CustomQuadFlatEnvCfg_PLAY(CustomQuadFlatEnvCfg):
    def __post_init__(self) -> None:
        # post init of parent
        super().__post_init__()

        # make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        # disable randomization for play
        self.observations.policy.enable_corruption = False
        # remove random pushing event
        self.events.base_external_force_torque = None
        self.events.push_robot = None
