class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folderSet = set(folder)
        res = []

        for f in folder:
            isSubFolder = False
            prefix = f

            while not prefix == "":
                pos = prefix.rfind("/")
                if pos == -1:
                    break
                
                prefix = prefix[0:pos]

                if prefix in folderSet:
                    isSubFolder = True
                    break
                
            if not isSubFolder:
                res.append(f)
            
        return res
# 1233. Remove Sub-Folders from the Filesystem 
