from os import PathLike
import string
from typing import IO, Any, Iterator
from . import DEFAULT_LANG as DEFAULT_LANG, Genre as Genre, ID3_ANY_VERSION as ID3_ANY_VERSION, ID3_DEFAULT_VERSION as ID3_DEFAULT_VERSION, ID3_V1 as ID3_V1, ID3_V1_0 as ID3_V1_0, ID3_V1_1 as ID3_V1_1, ID3_V2 as ID3_V2, ID3_V2_2 as ID3_V2_2, ID3_V2_3 as ID3_V2_3, ID3_V2_4 as ID3_V2_4, frames as frames, versionToString as versionToString
from .. import Error as Error, core as core
from ..core import ALBUM_TYPE_IDS as ALBUM_TYPE_IDS, ArtistOrigin as ArtistOrigin, TXXX_ALBUM_TYPE as TXXX_ALBUM_TYPE, TXXX_ARTIST_ORIGIN as TXXX_ARTIST_ORIGIN, CountAndTotalTuple, Date
from .headers import ExtendedTagHeader as ExtendedTagHeader, TagHeader as TagHeader
from _typeshed import Incomplete
from collections.abc import Generator

ID3_V1_COMMENT_DESC: str
ID3_V1_MAX_TEXTLEN: int
ID3_V1_STRIP_CHARS: bytes
DEFAULT_PADDING: int

class TagException(Error): ...

_VersionTuple = tuple[int | None, int | None, int | None]

class Tag(core.Tag):
    file_info: Incomplete
    header: TagHeader
    extended_header: ExtendedTagHeader
    frame_set: frames.FrameSet
    version: _VersionTuple
    def __init__(self, version: _VersionTuple = ..., *, title: str | None = None, artist: str | None = None, album: str | None = None, album_artist: str | None = None, track_num: str | None = None) -> None: ...
    def clear(self, *, version: _VersionTuple=...) -> None: ...
    def parse(self, fileobj: str | PathLike[str] | IO[Any], version: _VersionTuple=...) -> bool: ...
    def isV1(self) -> bool: ...
    def isV2(self) -> bool: ...
    def setTextFrame(self, fid: bytes, txt: str) -> None: ...
    def getTextFrame(self, fid: bytes) -> str | None: ...
    @property
    def composer(self) -> str: ...
    @composer.setter
    def composer(self, v: str) -> None: ...
    @property
    def comments(self) -> CommentsAccessor: ...
    bpm: Incomplete
    @property
    def play_count(self) -> int | None: ...
    @play_count.setter
    def play_count(self, count: int | None) -> None: ...
    publisher: Incomplete
    @property
    def cd_id(self) -> bytes: ...
    @cd_id.setter
    def cd_id(self, toc: bytearray) -> None: ...
    @property
    def unknown_frame_ids(self) -> set[Incomplete]: ...
    @property
    def images(self) -> ImagesAccessor: ...
    encoding_date: Date | None
    @property
    def best_release_date(self) -> Date | None: ...
    def getBestDate(self, prefer_recording_date: bool = False) -> Date | None: ...
    release_date: Date | None
    original_release_date: Date | None
    recording_date: Date | None
    tagging_date: Date | None
    @property
    def lyrics(self) -> LyricsAccessor: ...
    @property
    def disc_num(self) -> CountAndTotalTuple: ...
    @disc_num.setter
    def disc_num(self, val: CountAndTotalTuple) -> None: ...
    @property
    def objects(self) -> ObjectsAccessor: ...
    @property
    def privates(self) -> PrivatesAccessor: ...
    @property
    def popularities(self) -> PopularitiesAccessor: ...
    genre: int | None
    non_std_genre: Genre | None
    @property
    def user_text_frames(self) -> UserTextsAccessor: ...
    @property
    def commercial_url(self) -> str | None: ...
    @commercial_url.setter
    def commercial_url(self, url: str | None) -> None: ...
    @property
    def copyright_url(self) -> str | None: ...
    @copyright_url.setter
    def copyright_url(self, url: str | None) -> None: ...
    @property
    def audio_file_url(self) -> str | None: ...
    @audio_file_url.setter
    def audio_file_url(self, url: str | None) -> None: ...
    @property
    def audio_source_url(self) -> str | None: ...
    @audio_source_url.setter
    def audio_source_url(self, url: str | None) -> None: ...
    @property
    def artist_url(self) -> str | None: ...
    @artist_url.setter
    def artist_url(self, url: str | None) -> None: ...
    @property
    def internet_radio_url(self) -> str | None: ...
    @internet_radio_url.setter
    def internet_radio_url(self, url: str | None) -> None: ...
    @property
    def payment_url(self) -> str | None: ...
    @payment_url.setter
    def payment_url(self, url: str | None) -> None: ...
    @property
    def publisher_url(self) -> str | None: ...
    @publisher_url.setter
    def publisher_url(self, url: str | None) -> None: ...
    @property
    def user_url_frames(self) -> UserUrlsAccessor: ...
    @property
    def unique_file_ids(self) -> UniqueFileIdAccessor: ...
    @property
    def terms_of_use(self) -> str: ...
    @terms_of_use.setter
    def terms_of_use(self, tos: str | tuple[str, str]) -> None: ...
    copyright: Incomplete
    encoded_by: Incomplete
    def save(self, filename: str | PathLike[str] | None = None, version: _VersionTuple | None = None, encoding: str | None = None, backup: bool = False, preserve_file_time: bool = False, max_padding: int | None = None) -> None: ...
    @staticmethod
    def remove(filename: str | PathLike[str], version: _VersionTuple=..., preserve_file_time: bool = False) -> bool: ...
    @property
    def chapters(self) -> ChaptersAccessor: ...
    @property
    def table_of_contents(self) -> TocAccessor: ...
    @property
    def album_type(self) -> str | None: ...
    @album_type.setter
    def album_type(self, t: str | None) -> None: ...
    @property
    def artist_origin(self) -> ArtistOrigin: ...
    @artist_origin.setter
    def artist_origin(self, origin: ArtistOrigin) -> None: ...
    def frameiter(self, fids: Incomplete | None = None) -> Generator[Incomplete]: ...
    @property
    def original_artist(self) -> str: ...
    @original_artist.setter
    def original_artist(self, name: str) -> None: ...

class FileInfo:
    name: Incomplete
    tag_size: Incomplete
    tag_padding_size: Incomplete
    def initStatTimes(self) -> None: ...
    def touch(self, times: Incomplete) -> None: ...

class AccessorBase:
    def __iter__(self) -> Iterator[frames.Frame]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i: Incomplete) -> Incomplete: ...
    def get(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def remove(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

class DltAccessor(AccessorBase):
    FrameClass: Incomplete
    def __init__(self, FrameClass: Incomplete, fid: Incomplete, fs: Incomplete) -> None: ...
    def set(self, text: str, description: str = '', lang: str | bytes =...) -> Incomplete: ...
    def remove(self, description: str, lang: str | bytes =...) -> Incomplete: ...
    def get(self, description: str, lang: str | bytes=...) -> Incomplete: ...

class CommentsAccessor(DltAccessor):
    def __init__(self, fs: Incomplete) -> None: ...

class LyricsAccessor(DltAccessor):
    def __init__(self, fs: Incomplete) -> None: ...

class ImagesAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def __iter__(self) -> Iterator[frames.ImageFrame]: ...
    def set(self, type_: Incomplete, img_data: Incomplete, mime_type: Incomplete, description: str = '', img_url: Incomplete | None = None) -> Incomplete: ...
    def remove(self, description: Incomplete) -> Incomplete: ...
    def get(self, description: Incomplete) -> Incomplete: ...

class ObjectsAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def set(self, data: Incomplete, mime_type: Incomplete, description: str = '', filename: str = '') -> Incomplete: ...
    def remove(self, description: Incomplete) -> Incomplete: ...
    def get(self, description: Incomplete) -> Incomplete: ...

class PrivatesAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def set(self, data: Incomplete, owner_id: Incomplete) -> Incomplete: ...
    def remove(self, owner_id: Incomplete) -> Incomplete: ...
    def get(self, owner_id: Incomplete) -> Incomplete: ...

class UserTextsAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def set(self, text: str, description: str = '') -> Incomplete: ...
    def remove(self, description: str) -> Incomplete: ...
    def get(self, description: str) -> Incomplete: ...
    def __contains__(self, description: str) -> bool: ...

class UniqueFileIdAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def set(self, data: Incomplete, owner_id: Incomplete) -> Incomplete: ...
    def remove(self, owner_id: Incomplete) -> Incomplete: ...
    def get(self, owner_id: Incomplete) -> Incomplete: ...

class UserUrlsAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def set(self, url: str, description: str = '') -> Incomplete: ...
    def remove(self, description: str) -> Incomplete: ...
    def get(self, description: str) -> Incomplete: ...

class PopularitiesAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def set(self, email: str, rating: Incomplete, play_count: Incomplete) -> Incomplete: ...
    def remove(self, email: str) -> Incomplete: ...
    def get(self, email: str) -> Incomplete: ...

class ChaptersAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def set(self, element_id: Incomplete, times: Incomplete, offsets: tuple[int | None, int | None] = (None, None), sub_frames: Incomplete | None = None) -> Incomplete: ...
    def remove(self, element_id: Incomplete) -> Incomplete: ...
    def get(self, element_id: Incomplete) -> Incomplete: ...
    def __getitem__(self, elem_id: Incomplete) -> Incomplete: ...

class TocAccessor(AccessorBase):
    def __init__(self, fs: Incomplete) -> None: ...
    def __iter__(self) -> Incomplete: ...
    def set(self, element_id: Incomplete, toplevel: bool = False, ordered: bool = True, child_ids: Incomplete | None = None, description: str = '') -> Incomplete: ...
    def remove(self, element_id: Incomplete) -> Incomplete: ...
    def get(self, element_id: Incomplete) -> Incomplete: ...
    def __getitem__(self, elem_id: Incomplete) -> Incomplete: ...

class TagTemplate(string.Template):
    def __init__(self, pattern: Incomplete, path_friendly: str = '-', dotted_dates: bool = False) -> None: ...
    def substitute(self, tag: Incomplete, zeropad: bool = True) -> str: ... # type: ignore # TODO: fix
    safe_substitute = substitute # type: ignore
