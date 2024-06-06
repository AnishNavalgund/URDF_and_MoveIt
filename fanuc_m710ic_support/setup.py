from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'fanuc_m710ic_support'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),  # Automatically find all packages
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include launch directory
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # Include urdf files
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        # Include visual and collision meshes for m710ic45m
        (os.path.join('share', package_name, 'meshes', 'm710ic45m', 'visual'), glob('meshes/m710ic45m/visual/*.stl', recursive=True)),
        (os.path.join('share', package_name, 'meshes', 'm710ic45m', 'collision'), glob('meshes/m710ic45m/collision/*.stl', recursive=True)),
        # Include visual and collision meshes for m710ic50
        (os.path.join('share', package_name, 'meshes', 'm710ic50', 'visual'), glob('meshes/m710ic50/visual/*.stl', recursive=True)),
        (os.path.join('share', package_name, 'meshes', 'm710ic50', 'collision'), glob('meshes/m710ic50/collision/*.stl', recursive=True)),
        # Include any other directories or files as necessary
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='administrator',
    maintainer_email='st157476@stud.uni-stuttgart.de',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Add any executable scripts here if you have any node executables
            'publish_joint_states = fanuc_m710ic_support.publish_joint_states:main'
        ],
    },
)

