import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetMLPCfg, DCMotorCfg, ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
import os
from math import pi

CUSTOM_QUAD_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=os.environ['HOME'] + "/IsaacLab/source/isaaclab_tasks/isaaclab_tasks/manager_based/locomotion/velocity/config/custom_quadruped/robot.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.719),
        joint_pos={
            ".*L_hip_joint": pi/90,  # Reduced from pi/45 for a straighter stance
            ".*R_hip_joint": pi/90,  # Reduced from pi/45
            "F[L,R]_thigh_joint": -pi/36,  # Reduced from -5*pi/18 for less crouch
            "R[L,R]_thigh_joint": -pi/36,  # Reduced from -5*pi/18
            ".*_calf_joint": pi/3,  # Reduced from 5*pi/9 for a more upright leg
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*_hip_joint", ".*_thigh_joint", ".*_calf_joint"],
            effort_limit=45,
            saturation_effort=45,
            velocity_limit=21.0,
            stiffness=40,  # Reduced from 60 to smooth movements
            damping=3.0,  # Increased from 1.5 to improve stability
            friction=0.0,
        ),
    },
)
