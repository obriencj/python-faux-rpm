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


from ._rpm import ts as TransactionSetCore


class TransactionSet(TransactionSetCore):
    def setVSFlags(self, flags):
        pass

    def getVSFlags(self):
        pass

    def setVfyFlags(self, flags):
        pass

    def getVfyFlags(self):
        pass

    def getVfyLevel(self):
        pass

    def setVfyLevel(self, flags):
        pass

    def setColor(self, color):
        pass

    def setPrefColor(self, color):
        pass

    def setFlags(self, flags):
        pass

    def setProbFilter(self, ignoreSet):
        pass

    def parseSpec(self, specfile):
        pass

    def getKeys(self):
        pass

    def addInstall(self, item, key, how: str = ...) -> None:
        pass

    def addReinstall(self, item, key) -> None:
        pass

    def addErase(self, item) -> None:
        pass

    def addRestore(self, item) -> None:
        pass

    def run(self, callback, data):
        pass

    def check(self, *args, **kwds):
        pass

    def hdrCheck(self, blob) -> None:
        pass

    def hdrFromFdno(self, fd):
        pass


# The end.
