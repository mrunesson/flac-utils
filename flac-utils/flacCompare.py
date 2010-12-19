
from mutagen.flac import FLAC

class flacCompare:
    """Can compare and merge two flac files. Is instantied with one old and
    one new flac object representing different flac files. The flac object
    should be mutagen FLAC instances or similar.
    """

    def __init__(self, oldflac, newflac):
        self.oldflac=oldflac
        self.newflac=newflac

    def commonTags(self):
        """Return the common tags for the flac files."""
        return filter(lambda x: x in self.oldflac, self.newflac)

    def newTags(self):
        """Return tags exist in newflac but not oldflac."""
        return filter(lambda x: x not in self.oldflac, self.newflac)

    def removedTags(self):
        """Return tags exist in oldflac but not newflac."""
        return filter(lambda x: x not in self.newflac, self.oldflac)

    def changedTags(self):
        """Return tags changed between the two flacs."""
        result=[]
        for x in self.commonTags():
            if self.newflac[x]!=self.oldflac[x]:
                result.append(x)
        return result
                

    def audioEqual(self):
        """Compare if the audio part of the two flacs are equal. This is
        done comparing MD5 signature, total samples and length.
        Returns true if one of the flacs does not have a info block with
        the stream info."""
        if self.oldflac.info is None or self.newflac.info is None:
            # If either of the datasets not has an info-block
            # then assume that they are equal.
            return True
        if self.oldflac.info.md5_signature!=self.newflac.info.md5_signature:
            return False
        if self.oldflac.info.total_samples!=self.newflac.info.total_samples:
            return False
        if self.oldflac.info.length!=self.newflac.info.length:
            return False
        return True
    

    def merge(self):
        """Merge missing tags in oldflac into newflac."""
        if not self.audioEqual():
            raise Exception
        for k in self.oldflac.keys():
            if k not in self.newflac:
                self.newflac[k]=self.oldflac[k]

    def equals(self):
        """Compare the two flacs."""
        if not self.audioEqual():
            return False
        if self.newTags() != []:
            return False
        if self.removedTags() != []:
            return False
        if self.changedTags() != []:
            return False
        return True
