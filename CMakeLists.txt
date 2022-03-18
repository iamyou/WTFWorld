cmake_minimum_required(VERSION 3.5)
project(FrameLibPoint)

find_package(Python3 COMPONENTS Interpreter Development)

set(ARCHIVE_OUTPUT_NAME ${PROJECT_NAME})
set(LIBRARY_OUTPUT_NAME ${PROJECT_NAME})
set(ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/dev/app/worldbuider-Minecraft/)
set(LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/dev/app/worldbuider-Minecraft/)

add_library(${PROJECT_NAME} SHARED 
    ${PROJECT_SOURCE_DIR}/dev/frame/FolderPoint/FolderPoint.cpp
    ${PROJECT_SOURCE_DIR}/dev/frame/FrameLibPoint/FrameLibPoint.cpp
)
target_include_directories(${PROJECT_NAME} PUBLIC
    ${Python3_INCLUDE_DIRS}    
    ${PROJECT_SOURCE_DIR}/dev/WindowsRegistry/
)
target_link_libraries(${PROJECT_NAME} PUBLIC
    ${Python3_LIBRARIES}
)