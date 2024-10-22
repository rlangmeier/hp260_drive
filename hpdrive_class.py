# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:06:13 2024

@author: robert
"""


from pathlib import Path
import struct


# %% 

class Media:
    
    def __init__(self, file_name):
        self.file_name = Path(file_name)
        if not self.file_name.exists():
            raise FileExistsError()
        self._blocks = []
        
    def _read_blocks(self, block_size=256):
        with self.file_name.open(mode='rb') as f:
            while buf := f.read(block_size):
                self._blocks.append(buf)
        
    def _system_block(self):
        system_block = self._blocks[0]
            
        
    def mount(self):
        self._read_blocks()
    
    def dismount(self):
        pass
    
    
    def directory(self):
        pass
    

# %%

if __name__ == "__main__":
    
    floppy_os_name = Path('./media').joinpath('250-OS-B.07.hpi')

    floppy_os = Media(floppy_os_name)
    floppy_os.mount()
    struct.unpack()