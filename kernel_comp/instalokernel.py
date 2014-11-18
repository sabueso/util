#!/usr/bin/env python
import os,sys
directorio = sys.argv[1]
arch_ref={'i686':'i386','x86_64':'amd64'}

#Show linux version
version=os.popen('make -s -C '+directorio+' kernelversion').read()

#Show arch type for future use
arch_os=os.popen('arch').read()
arch_os=arch_os.strip()
for i in arch_ref:
	if arch_os in i:
		directory_arch=str(arch_ref[i])

print('==Compiling '+directory_arch+' kernel version==')
#Compile ALL
os.system('make -C '+directorio+' -j12 all')
os.system('make -C '+directorio+' modules_install')
os.system('cp '+directorio+'/arch/'+directory_arch+'/boot/bzImage /boot/vmlinuz-inestable')
os.system('rm /boot/initrd.img-inestable')
os.system('mkinitramfs -v -o /boot/initrd.img-inestable '+version+' ')
sys.exit()

