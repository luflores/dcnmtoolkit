# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .__about__ import ( # noqa
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __uri__, __version__,
)

_about_exports = [
    "__author__", "__copyright__", "__email__", "__license__", "__summary__",
    "__title__", "__uri__", "__version__",
]

from .dcnmsession import Session, AutoConfigSettings
from .cableplan import CablePlan
from .autoconfig import Org, Partition, Network, Profile, AutoConfigSettings
from .vxlan import VTEP, VNI
from .config import ConfigTemplate
from .poap import Server, SwitchDefinition, PoapTemplate


import inspect as _inspect

__all__ = _about_exports + sorted(
    name for name, obj in locals().items()
    if not (name.startswith('_') or _inspect.ismodule(obj))
)
