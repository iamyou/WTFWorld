cmake_minimum_required(VERSION 3.21)
project(OdysseyWorld)

set(CMAKE_CXX_STANDARD 14)

include_directories(SDK/source/FrameLibPoint)

add_executable(OdysseyWorld
        SDK/source/FrameLibPoint/FrameLibPoint.cpp)
