
from mutagen.flac import FLAC

class flacCompare:
    """Diff util to compare two flac files.
    """

    def __init__(self, oldflac, newflac):
        self.oldflac=oldflac
        self.newflac=newflac

    def commonTags(self):
        return filter(lambda x: x in self.oldflac, self.newflac)

    def newTags(self):
        return filter(lambda x: x not in self.oldflac, self.newflac)

    def removedTags(self):
        return filter(lambda x: x not in self.newflac, self.oldflac)

    def changedTags(self):
        result=[]
        for x in self.commonTags():
            if self.newflac[x]!=self.oldflac[x]:
                result.append(x)
        return result
                

    def audioEqual(self):
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
        if not self.audioEqual():
            raise Exception
        for k in self.oldflac.keys():
            if k not in self.newflac:
                self.newflac[k]=self.oldflac[k]
            

    def equals(self):
        if not self.audioEqual():
            return False
        if self.newTags() != []:
            return False
        if self.removedTags() != []:
            return False
        if self.changedTags() != []:
            return False
        return True
