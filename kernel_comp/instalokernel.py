#!/usr/bin/env python
import os,sys
directorio = sys.argv[1]

version=os.popen('make -s -C '+directorio+' kernelversion').read()
os.system('make -C '+directorio+' -j12 all')
os.system('make -C '+directorio+' modules_install')
os.system('cp '+directorio+'/arch/'+version+'/boot/bzImage /boot/vmlinuz-inestable')
os.system('rm /boot/initrd.img-inestable')
os.system('mkinitramfs -v -o /boot/initrd.img-inestable '+version+' ')
sys.exit()

