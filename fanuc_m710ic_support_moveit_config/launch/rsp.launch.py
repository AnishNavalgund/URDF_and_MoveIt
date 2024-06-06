from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_rsp_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("fanuc_m710ic45m", package_name="fanuc_m710ic_support_moveit_config").to_moveit_configs()
    return generate_rsp_launch(moveit_config)
