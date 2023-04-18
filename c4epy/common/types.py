# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Common types."""
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

import betterproto

Primitive = Union[str, int, bool, float]
_JSONDict = Dict[Any, Any]  # temporary placeholder
_JSONList = List[Any]  # temporary placeholder
_JSONType = Optional[Union[Primitive, _JSONDict, _JSONList]]
# Added Dict[str, _JSONDict] as workaround to not properly resolving recursive types - _JSONDict should be subset of _JSONType
JSONLike = Union[Dict[str, _JSONType], Dict[str, _JSONDict]]

@dataclass(eq=False, repr=False)
class Any(betterproto.Message):
    type_url: str = betterproto.string_field(1)
    value: betterproto.Message = betterproto.message_field(2)

    def to_dict(
        self, casing: betterproto.Casing = betterproto.Casing.CAMEL, include_default_values: bool = False
    ) -> Dict[str, Any]:
        raw_dict = super().to_dict(casing, include_default_values)
        dict_: Dict[str, Any] = {}
        type_url = casing('type_url').rstrip("_") # type: ignore
        if type_url in raw_dict:
            dict_['@type'] = raw_dict[type_url]
        value = casing('value').rstrip("_") # type: ignore
        dict_.update(raw_dict.get(value, {}))
        return dict_