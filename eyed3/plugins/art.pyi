from _typeshed import Incomplete
from eyed3.core import VARIOUS_ARTISTS as VARIOUS_ARTISTS
from eyed3.id3.frames import ImageFrame as ImageFrame
from eyed3.mimetype import guessMimetype as guessMimetype
from eyed3.plugins import LoaderPlugin as LoaderPlugin
from eyed3.plugins.lastfm import getAlbumArt as getAlbumArt
from eyed3.utils import art as art, makeUniqueFileName as makeUniqueFileName
from eyed3.utils.console import Fore as Fore, cformat as cformat, printMsg as printMsg, printWarning as printWarning

DESCR_FNAME_PREFIX: str
md5_file_cache: Incomplete

class ArtFile:
    art_type: Incomplete
    file_path: Incomplete
    id3_art_type: Incomplete
    def __init__(self, file_path) -> None: ...
    @property
    def image_data(self): ...
    @property
    def mime_type(self): ...

class ArtPlugin(LoaderPlugin):
    SUMMARY: str
    DESCRIPTION: str
    NAMES: Incomplete
    def __init__(self, arg_parser) -> None: ...
    def start(self, args, config) -> None: ...
    def handleDirectory(self, d, _): ...
    def handleDone(self): ...

def pilImage(source): ...
def pilImageDetails(img): ...
def md5Data(data): ...
def md5File(file_name): ...
