#!/usr/bin/env python
import os,sys
directorio = sys.argv[1]
arch_def="X86_64"


#Obtenemos la version del kernel que vamos a compilar
version=os.popen('make -s -C '+directorio+' kernelversion').read()
#Cremos solo 12 hilos paralelos para evitar una race condition
#de la compilacion
os.system('make -C '+directorio+' -j12 all')
##os.system('make -C '+directorio+' all')
#Instalamos los modulos
os.system('make -C '+directorio+' modules_install')
#Copiamos el kernel
os.system('cp '+directorio+'/arch/'+arch_def+'/boot/bzImage /boot/vmlinuz-inestable')
##Borramos el antiguo initrd
os.system('rm /boot/initrd.img-inestable')
#Creamos el nuevo initrd
os.system('mkinitramfs -v -o /boot/initrd.img-inestable '+version+' ')
#Listo!
sys.exit()

