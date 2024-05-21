# Overview

`preoccupied.faux-rpm` is a distribution providing an `rpm` python
package and associated sub-modules. This package has no functional
behavior, its callable members are no-ops. It exists for cases where a
tool needs to be run against a package with an rpm dependency, but
where it does not actually invoke any code paths that would trigger
the use of that dependency.

My personal use case is with [MyPy]'s `stubtest` and `stubgen` tools.
I have been writing stubs for a module which imports rpm. At no point
do I need to actually execute anything, I simply need the import to not
fail. This project allowed me to continue on a non-RPM host machine.

[MyPy]: https://mypylang.org


## Contact

Author: Christopher O'Brien  <obriencj@preoccupied.net>

Original Git Repository: <https://github.com/obriencj/python-faux-rpm>


## License

This library is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or (at
your option) any later version.

This library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this library; if not, see <http://www.gnu.org/licenses/>.
