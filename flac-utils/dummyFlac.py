from mutagen.flac import FLAC

class metadataFlacStreamInfo:
    bits_per_sample=None
    channels=None
    code=None
    length=None
    max_blocksize=None
    max_framesize=None
    md5_signature=None
    min_blocksize=None
    min_framesize=None
    sample_rate=None
    total_samples=None

class dummyFlac(FLAC):

    def load(self, filename):
        """Load file information from a filename."""

        self.metadata_blocks = [metadataFlacStreamInfo()]
        self.tags = None
        self.cuesheet = None
        self.seektable = None
        self.filename = filename
