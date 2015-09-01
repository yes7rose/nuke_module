import os
import sys
from functools import partial

platform = sys.platform.rstrip('1234567890').lower()
if platform == 'darwin': # Use osx instead of darwin
    platform = 'osx'

nuke_path = os.path.dirname(__file__)
rel = partial(os.path.join, nuke_path)


nuke.pluginAddPath(nuke_path)
nuke.pluginAddPath(rel('python'))
nuke.pluginAddPath(rel('gizmos'))
nuke.pluginAddPath(rel('plugins', platform))
