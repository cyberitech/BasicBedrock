"""
the basicbedrock module contains basicbedrock.BasicBedrock, the top-level class for all of the module's functionality.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from .basicbedrock import BasicBedrock
from .guardrails import Guardrails
from .models import *

__version__ = '0.2.2'
