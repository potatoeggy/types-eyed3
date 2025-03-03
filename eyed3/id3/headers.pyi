from typing import IO, Any, Literal
from . import ID3_DEFAULT_VERSION as ID3_DEFAULT_VERSION, isValidVersion as isValidVersion, normalizeVersion as normalizeVersion
from .. import core as core
from ..utils.binfuncs import bin2bytes as bin2bytes, bin2dec as bin2dec, bin2synchsafe as bin2synchsafe, bytes2bin as bytes2bin, dec2bin as dec2bin
from _typeshed import Incomplete

NULL_FRAME_FLAGS: Incomplete

_VersionTuple = tuple[int | None, int | None, int | None]

class TagHeader:
    SIZE: int
    def __init__(self, version: _VersionTuple=...) -> None: ...
    tag_size: int
    unsync: bool
    extended: bool
    experimental: bool
    footer: bool
    def clear(self) -> None: ...
    @property
    def version(self) -> _VersionTuple: ...
    @version.setter
    def version(self, v: _VersionTuple) -> None: ...
    @property
    def major_version(self) -> int | None: ...
    @property
    def minor_version(self) -> int | None: ...
    @property
    def rev_version(self) -> int | None: ...
    def parse(self, f: IO[Any]) -> bool: ...
    def render(self, tag_len: Incomplete | None = None) -> Incomplete: ...

class ExtendedTagHeader:
    RESTRICT_TAG_SZ_LARGE: int
    RESTRICT_TAG_SZ_MED: int
    RESTRICT_TAG_SZ_SMALL: int
    RESTRICT_TAG_SZ_TINY: int
    RESTRICT_TEXT_ENC_NONE: int
    RESTRICT_TEXT_ENC_UTF8: int
    RESTRICT_TEXT_LEN_NONE: int
    RESTRICT_TEXT_LEN_1024: int
    RESTRICT_TEXT_LEN_128: int
    RESTRICT_TEXT_LEN_30: int
    RESTRICT_IMG_ENC_NONE: int
    RESTRICT_IMG_ENC_PNG_JPG: int
    RESTRICT_IMG_SZ_NONE: int
    RESTRICT_IMG_SZ_256: int
    RESTRICT_IMG_SZ_64: int
    RESTRICT_IMG_SZ_64_EXACT: int
    size: int
    def __init__(self) -> None: ...
    @property
    def update_bit(self) -> bool: ...
    @update_bit.setter
    def update_bit(self, v: bool) -> None: ...
    @property
    def crc_bit(self) -> bool: ...
    @crc_bit.setter
    def crc_bit(self, v: bool) -> None: ...
    @property
    def crc(self) -> bool: ...
    @crc.setter
    def crc(self, v: bool) -> None: ...
    @property
    def restrictions_bit(self) -> bool: ...
    @restrictions_bit.setter
    def restrictions_bit(self, v: bool) -> None: ...
    @property
    def tag_size_restriction(self) -> int: ...
    @tag_size_restriction.setter
    def tag_size_restriction(self, v: int) -> None: ...
    @property
    def tag_size_restriction_description(self) -> str: ...
    @property
    def text_enc_restriction(self) -> int: ...
    @text_enc_restriction.setter
    def text_enc_restriction(self, v: Literal[0, 1]) -> None: ...
    @property
    def text_enc_restriction_description(self) -> str: ...
    @property
    def text_length_restriction(self) -> int: ...
    @text_length_restriction.setter
    def text_length_restriction(self, v: Literal[0, 1, 2, 3]) -> None: ...
    @property
    def text_length_restriction_description(self) -> str: ...
    @property
    def image_enc_restriction(self) -> int: ...
    @image_enc_restriction.setter
    def image_enc_restriction(self, v: Literal[0, 1]) -> None: ...
    @property
    def image_enc_restriction_description(self) -> str: ...
    @property
    def image_size_restriction(self) -> int: ...
    @image_size_restriction.setter
    def image_size_restriction(self, v: Literal[0, 1, 2, 3]) -> None: ...
    @property
    def image_size_restriction_description(self) -> str: ...
    def render(self, version: _VersionTuple, frame_data: Incomplete, padding: int = 0) -> Incomplete: ...
    def parse(self, fp: Incomplete, version: _VersionTuple) -> None: ...

class FrameHeader:
    TAG_ALTER: Incomplete
    FILE_ALTER: Incomplete
    READ_ONLY: Incomplete
    COMPRESSED: Incomplete
    ENCRYPTED: Incomplete
    GROUPED: Incomplete
    UNSYNC: Incomplete
    DATA_LEN: Incomplete
    size: Incomplete
    id: Incomplete
    data_size: int
    def __init__(self, fid: Incomplete, version: _VersionTuple) -> None: ...
    def copyFlags(self, rhs: FrameHeader) -> None: ...
    @property
    def major_version(self) -> int: ...
    @property
    def minor_version(self) -> int: ...
    @property
    def version(self) -> _VersionTuple: ...
    @property
    def tag_alter(self) -> int: ...
    @tag_alter.setter
    def tag_alter(self, b: int) -> None: ...
    @property
    def file_alter(self) -> int: ...
    @file_alter.setter
    def file_alter(self, b: int) -> None: ...
    @property
    def read_only(self) -> int: ...
    @read_only.setter
    def read_only(self, b: int) -> None: ...
    @property
    def compressed(self) -> int: ...
    @compressed.setter
    def compressed(self, b: int) -> None: ...
    @property
    def encrypted(self) -> int: ...
    @encrypted.setter
    def encrypted(self, b: int) -> None: ...
    @property
    def grouped(self) -> int: ...
    @grouped.setter
    def grouped(self, b: int) -> None: ...
    @property
    def unsync(self) -> int: ...
    @unsync.setter
    def unsync(self, b: int) -> None: ...
    @property
    def data_length_indicator(self) -> int: ...
    @data_length_indicator.setter
    def data_length_indicator(self, b: int) -> None: ...
    def render(self, data_size: int) -> Incomplete: ...
    @staticmethod
    def parse(f: Incomplete, version: _VersionTuple) -> Incomplete: ...
