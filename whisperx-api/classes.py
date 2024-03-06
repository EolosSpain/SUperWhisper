from enum import Enum
from pydantic import BaseModel


class DeviceType(str, Enum):
    cpu = "cpu"
    cuda = "cuda"


class ModelSize(str, Enum):
    tiny_en = "tiny.en"
    tiny = "tiny"
    base_en = "base.en"
    base = "base"
    small_en = "small.en"
    small = "small"
    medium_en = "medium.en"
    medium = "medium"
    large_v2 = "large-v2"
    large_v3 = "large-v3"


class Languages(str, Enum):
    auto = "auto"
    ar = "ar"
    be = "be"
    bg = "bg"
    bn = "bn"
    ca = "ca"
    cs = "cs"
    cy = "cy"
    da = "da"
    de = "de"
    el = "el"
    en = "en"
    es = "es"
    fr = "fr"
    it = "it"
    ja = "ja"
    nl = "nl"
    pl = "pl"
    pt = "pt"
    ru = "ru"
    sk = "sk"
    sl = "sl"
    sv = "sv"
    tk = "tk"
    tr = "tr"
    zh = "zh"
