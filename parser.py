from typing import Union
from types import NoneType

JsonValue = Union["JsonObject", "JsonArray", str, int, float, bool, NoneType]
JsonObject = dict[str, JsonValue]
JsonArray = list[JsonValue]

def parse(input: str) -> JsonValue:
    pass