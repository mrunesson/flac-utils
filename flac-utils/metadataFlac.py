class metadataFlacInfo:
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
    


class metadataFlac(dict):
    """Class to fake a mutagen.flac.FLAC object. This class does only
    have the metadata and does not have to be complete."""

    def readFile(file):
        """Not ready!!!"""
        f = open(file, "r")
        for line in f:
            l=line.split(u':',1)
            field=l[0]
            value=l[1]
        f.close()
        
    def writeFile(file):
        """Not ready!!!"""
        f = open(file, "w")
        f.close()

        
    def __init__(self, file=None, tags={}, info=None):
        if file is not None:
            readFile(file)
        else:
            if not isinstance(tags, dict):
                raise Exception
            self=tags
            self.info=info


