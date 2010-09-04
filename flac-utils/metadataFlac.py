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
    


class metadataFlac:
    """Class to fake a mutagen.flac.FLAC object. This class does only
    have the metadata and does not have to be complete."""

    info=None
    comments={}
    

    def readFile(file):
        f = open(file, "r")
        for line in f:
            l=line.split(u':',1)
            field=l[0]
            value=l[1]
            
        
    def __init__(self, file=None, tags={}, info=None):
        if file is not None:
            readFile(file)
        else
            self.tags=tags
            if info is None:
                self.info=metadataFlacInfo()
            else:
                self.info=info
                
          
