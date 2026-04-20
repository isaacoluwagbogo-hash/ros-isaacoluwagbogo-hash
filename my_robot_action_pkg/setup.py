from setuptools import setup

package_name = 'my_robot_action_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='emeka',
    maintainer_email='odiwebenedict@gmail.com',
    description='Custom ROS 2 action package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_server = scripts.action_server:main',
            'action_client = scripts.action_client:main',
        ],
    },
)