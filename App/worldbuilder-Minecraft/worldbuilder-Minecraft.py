import ctypes

dll_FrameLibPoint = ctypes.cdll.LoadLibrary("FrameLibPoint.dll")
dllPath = ""
dll_FrameLibPoint.dllPath("FolderPoint",ctypes.c_string(dllPath))
print(dllPath.value)