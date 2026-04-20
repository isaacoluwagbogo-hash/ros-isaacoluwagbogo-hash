cmake_minimum_required(VERSION 3.8)
project(my_robot_action_pkg)

# 1. Compiler flags
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 2. Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(action_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# 3. Generate the action interface
# NOTE: Interfaces should be generated BEFORE exporting or installing other targets
rosidl_generate_interfaces(${PROJECT_NAME}
  "action/DoTask.action"
  ADD_LINTER_TESTS
  DEPENDENCIES action_msgs
)

# 4. Export dependencies
# You must export rosidl_default_runtime so downstream packages can use your action
ament_export_dependencies(rosidl_default_runtime)

# 5. Install Python scripts
# Note: For rclpy scripts, you don't usually need find_package(ament_cmake_python) 
# unless you are building a hybrid C++/Python library. Simple scripts just need install().
install(PROGRAMS
  scripts/action_server.py
  scripts/action_client.py
  DESTINATION lib/${PROJECT_NAME}
)

# 6. Testing
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # The following line skips linter tests that check for copyright/etc. on generated files
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# 7. Finalize package
ament_package()