# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library; if not, see <http://www.gnu.org/licenses/>.


"""
Faux RPM -- lookalike rpm package which does nothing

:author: Christopher O'Brien <obriencj@preoccupied.net>
:license: GPL v3
"""


from ._rpm import *
from .transaction import *

from typing import Tuple

__version_info__: Tuple[str, str, str] = ('4', '18', '2')

ts = TransactionSet

def headerLoad(*args, **kwds): ...
def readHeaderListFromFD(file_desc, retrofit: bool = ...): ...
def readHeaderListFromFile(path, retrofit: bool = ...): ...
def readHeaderFromFD(file_desc): ...
def signalsCaught(siglist): ...
def dsSingle(TagN, N, EVR: str = ..., Flags=...): ...


# The end.
