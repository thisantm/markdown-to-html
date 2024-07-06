import os, shutil

def copyFolder(src, dst):
    for item in os.listdir(src):
        itemSrcPath = os.path.join(src, item)
        itemDstPath = os.path.join(dst, item)
        if os.path.isfile(itemSrcPath):
            shutil.copy(itemSrcPath, itemDstPath)
        else:
            os.mkdir(itemDstPath)
            copyFolder(itemSrcPath, itemDstPath)