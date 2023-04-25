import os

from sys import platform
import mujoco_py

if platform == "linux" or platform == "linux2":
    os.environ["MUJOCO_PY_MUJOCO_PATH"] = os.path.join(mujoco_py.__path__[0], "binaries", "linux", "mujoco-2.1.3")
    LIBPATH = os.path.join(mujoco_py.__path__[0], "binaries", "linux", "mujoco-2.1.3", "bin")
    LIBPATH = ":".join(LIBPATH, os.path.join(mujoco_py.__path__[0], "binaries", "linux", "mujoco-2.1.3", "lib"))
elif platform == "darwin":
    os.environ["MUJOCO_PY_MUJOCO_PATH"] = os.path.join(mujoco_py.__path__[0], "binaries", "macos", "mujoco210")
    LIBPATH = os.path.join(mujoco_py.__path__[0], "binaries", "macos", "mujoco-2.1.3", "bin")
elif platform == "win32":
    os.environ["MUJOCO_PY_MUJOCO_PATH"] = os.path.join(mujoco_py.__path__[0], "binaries", "windows", "mujoco210")
    LIBPATH = os.path.join(mujoco_py.__path__[0], "binaries", "windows", "mujoco-2.1.3", "bin")
else:
    raise NotImplementedError(platform)

curr = os.environ.get('LD_LIBRARY_PATH', None)
if curr:
    os.environ["LD_LIBRARY_PATH"] = f"{curr}:{LIBPATH}"
else:
    os.environ["LD_LIBRARY_PATH"] = LIBPATH
#!/usr/bin/env python
import os
from mujoco_py.builder import cymj, ignore_mujoco_warnings, functions, MujocoException
from mujoco_py.generated import const
from mujoco_py.mjrenderpool import MjRenderPool
from mujoco_py.mjviewer import MjViewer, MjViewerBasic
from mujoco_py.version import __version__, get_version
import mujoco_py

load_model_from_path = cymj.load_model_from_path
load_model_from_xml = cymj.load_model_from_xml
load_model_from_mjb = cymj.load_model_from_mjb
MjSim = cymj.MjSim
MjSimState = cymj.MjSimState
MjRenderContext = cymj.MjRenderContext
MjRenderContextOffscreen = cymj.MjRenderContextOffscreen
MjRenderContextWindow = cymj.MjRenderContextWindow
MjBatchRenderer = cymj.MjBatchRenderer
GlfwContext = cymj.GlfwContext


# Public API:
__all__ = ['MjSim', 'MjSimState',
           'MjRenderContextOffscreen', 'MjRenderContextWindow',
           'MjRenderContext', 'MjViewer', 'MjViewerBasic',
           'MujocoException', 'MjRenderPool', 'MjBatchRenderer', 'GlfwContext',
           'load_model_from_path', 'load_model_from_xml',
           'load_model_from_mjb',
           'ignore_mujoco_warnings', 'const', "functions",
           "__version__", "get_version"]


# Print out a warning if we can't find the key.
# this is nicer than failing activation, which we can not do in python.
# The mujoco library exits the process forcibly, in a way we can't try/catch.
mujoco_py.builder.find_key()
if not os.environ.get('MUJOCO_PY_SKIP_ACTIVATE'):
    mujoco_py.builder.activate()
