include("/opt/ros/jazzy/share/tl_expected/cmake/tl_expectedConfig.cmake")

if(NOT TARGET tl::expected)
  add_library(tl::expected INTERFACE IMPORTED)
  set_target_properties(tl::expected PROPERTIES
    INTERFACE_INCLUDE_DIRECTORIES "/opt/ros/jazzy/include"
  )
endif()
