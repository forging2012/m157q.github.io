Title: [Misc] Boot LiveUSB in VirtualBox 4.3.18
Date: 2014-12-04 04:21
Author: m157q
Category: Misc
Tags: boot, virtualbox, Liveusb, Unix-Like
Slug: misc-boot-liveusb-in-virtualbox-4318

<!--more-->  
  
# Steps  
  
+ `sudo chown m157q /dev/disk1`  
+ `VBoxManage internalcommands createrawvmdk -filename ~/VirtualBox\ VMs/win7_test.vmdk -rawdisk /dev/disk1`  
+ Create New Machine in VirtualBox and select the generated .vmdk file as the hard drive   
	+ Use an existing virtual hard drive file while addding the Hard drive  
+ Boot  
  
# References  
  
+ [VirtualBox 4.3.4使用USB隨身碟開機](http://blog.xuite.net/yh96301/blog/64131045-VirtualBox+4.3.4%E4%BD%BF%E7%94%A8USB%E9%9A%A8%E8%BA%AB%E7%A2%9F%E9%96%8B%E6%A9%9F)  
+ [VirtualBox設定由USB隨身碟開機](http://gordon168.tw/?p=324)  
+ [Using a raw hard disk on Mac OS X](https://forums.virtualbox.org/viewtopic.php?t=9223)  
+ [VERR_ACCESS_DENIED](https://forums.virtualbox.org/viewtopic.php?f=8&p=99406)  
  
  