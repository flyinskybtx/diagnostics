cmake_minimum_required(VERSION 2.8.3)
project(diagnostic_analysis)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")


# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED diagnostic_msgs rosbag roslib)

catkin_package(DEPENDS diagnostic_msgs rosbag roslib)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  catkin_add_nosetests(test/bag_csv_test.py)
endif()

catkin_python_setup()

catkin_install_python(PROGRAMS scripts/export_csv.py scripts/sparse_csv.py
                        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
