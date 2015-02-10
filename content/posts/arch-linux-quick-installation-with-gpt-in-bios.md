Title: [Arch Linux] Quick Installation with GPT in BIOS
Date: 2013-12-30 16:36
Author: m157q
Category: Arch
Tags: Linux, Arch, Installation
Slug: arch-linux-quick-installation-with-gpt-in-bios

## Arch Linux Quick Installation with GPT in BIOS  
### updated time: 2013/12/31  
  
A quick installation based on [Arch wiki - Beginners' Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide).  
  
> WITHOUT NETWORK CONFIGURATION   
> (INSTALL IN VIRTUAL MACHINE USING DHCP).  
> YOU NEED TO SETUP THE NETWORK OF THE MACHINE FIRST.  
  
<!--more-->  
  
### Network  
  
> to be written...  
  
---  
#### Partition  
  
* `# lsblk` - Check you are partitioning on the right disk. (assume /dev/sda here)  
* `# cgdisk /dev/sda`  
    * Partition Table  
        * GPT - ef02 (BIOS boot partition)  
            * 1M  
            * MUST be the first partition of the disk.  
            * `IMPORTANT!! Set to BIOS Boot partition for grub2`.  
        * / - 8300 (Linux filesystem)  
        * swap - 8200 (Linux swap)  
        * home - 8302 (Linux /home)  
    * Write -> yes  
    * QUIT  
* `# lsblk` - Check if the partition scheme of the disk is right.  
  
#### Create Filesystem  
  
* `# mkfs.ext4 /dev/sda1` - ext4 for /  
* `# mkfs.ext4 /dev/sda3` - ext4 for home/  
* `# mkswap /dev/sda2 && swapon /dev/sda2` - swap for swap/  
  
#### Mount partitionis  
  
* `# mount /dev/sda1 /mnt`  
* `# mkdir /mnt/home && mount /dev/sda3 /mnt/home`  
  
#### Select a mirror  
  
* `# vi /etc/pacman.d/mirrorlist`  
    * Choose a mirror site that is the nearest from your machine  
    * Copy it to the top of this mirrorlist.  
  
#### Install the base system  
  
* `# pacstrap /mnt base base-devel`  
  
#### Generate fstab  
  
* `# genfstab -p /mnt > /mnt/etc/fstab`  
* `# vi /mnt/etc/fstab` - Check if the fstab is right.  
  
---  
  
#### Chroot and configure the base system  
  
* `# arch-chroot /mnt /bin/bash` -  After change root, use bash.  
  
###### Locale & Keymap  
  
* `# vi /etc/locale.gen` - Select needed encoding and uncomment them.  
    * en_US.UTF-8 UTF-8  
    * en_US ISO-8859-1  
    * zh_TW.UTF-8 UTF-8  
* `# locale-gen`  
* `# echo "LANG=en_US.UTF-8" > /etc/locale.conf`  
* `# echo "KEYMAP=us" > /etc/vconsole.conf`  
  
##### Timezone & Hardclock & Hostname(not necessary)  
  
* `# ln -s /usr/share/zoneinfo/Asia/Taipei /etc/localtime`  
* `# hwclock --systohc --utc`  
* `# echo "$myhostname" > /etc/hostname`  
  
##### Configure the network  
  
* `# systemctl enable dhcpcd.service` - For Virtual Machine all it needed.  
  
> to be written...  
  
##### Create an initial ramdisk environment  
  
* If you won't modify `/etc/mkinitcpio.conf`, you can just skip this step.  
* `# mkinitcpio -p linux` after modified `/etc/mkinitcpio.conf`  
  
##### Set User  
  
* `# passwd` - set root password.  
* `# useradd -m m157q` - add a user with home directory.  
* `# passwd m157q` - set the password for the user.  
  
---  
  
#### Install and configure a bootloader  
  
* `# pacman -S grub`  
* `# vi /etc/default/grub` - [For a bug of grub I've met](https://bugs.archlinux.org/task/38041?project=1&cat%5B0%5D=31&string=grub).  
    * Add `GRUB_DISABLE_SUBMENU=y` at the end of `/etc/default/grub`  
* `# grub-mkconfig -o /boot/grub/grub.cfg` - Generate the configuration file of grub  
> If you didn't add the `GRUB_DISABLE_SUBMENU=y` mentioned above  
> you would get error message and fail here.  
  
* `# grub-install --target=i386-pc --recheck /dev/sda`  
> If you didn't mark the GPT partition (1007KiB)  
> as a `BIOS Boot Partition`  
> you would get error message and fail here. [see](https://wiki.archlinux.org/index.php/GRUB#Intel_BIOS_not_booting_GPT)  
  
---  
  
* `# exit`  
* `# umount -R /mnt` - unmount the partitions  
* `# reboot`  
  
---  
  
### References  
  
* [Arch wiki - Beginner's Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide)  
* [Arch wiki - GRUB - Intel BIOS not booting GPT](https://wiki.archlinux.org/index.php/GRUB#Intel_BIOS_not_booting_GPT)  
* [[solved] Grub Update gives Syntax error](https://bbs.archlinux.org/viewtopic.php?id=173921)  
* [FS#38041 - grub 1:2.00.1282.g5ae5c54-1 will not generate grub.cfg file syntax errors](https://bugs.archlinux.org/task/38041?project=1&cat%5B0%5D=31&string=grub)  
* [Archlinux installation - xatierlike](http://xatierlike.blogspot.tw/2012/10/archlinux-installation.html)  