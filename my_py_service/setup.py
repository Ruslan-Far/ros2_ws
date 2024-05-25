from setuptools import setup

package_name = 'my_py_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ruslan',
    maintainer_email='rfarhetdinov@mail.ru',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
			"server = my_py_service.pow_two_ints_server:main",
			"client = my_py_service.pow_two_ints_client:main",
        ],
    },
)
