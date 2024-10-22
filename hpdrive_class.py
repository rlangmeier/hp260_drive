# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:06:13 2024

@author: robert
"""


from pathlib import Path


# %%

class Media:
    
    def __init__(self, file_name):
        if isinstance(file_name, Path):
            self.file_name = file_name
        else:
            self.file_name = Path(file_name)
        if not self.file_name.exists():
            raise FileExistsError()
    
    def mount(self):
        pass
    
    
    def dismount(self):
        pass
    
    
    def directory(self):
        pass
    

# %%

if __name__ == "__main__":
    
    floppy_os_name = Path('./media').joinpath('250-OS-B.07.hpi')

    floppy_os = Media(floppy_os_name)
    