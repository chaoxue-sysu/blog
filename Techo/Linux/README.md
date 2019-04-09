# Technology of Linux
### Linux如何进入单用户模式和救援模式
Linux系统用户无法登陆、系统或系统引导（[GRUB](https://en.wikipedia.org/wiki/GNU_GRUB)）无法进入时，可采用一下方法进入Linux系统或文件系统进行相应操作。
+ **单用户模式**
1. 重启系统<br>
重启系统后进入GRUB引导页面后立即按“e”，进入GRUB编辑状态。在linux16那行的ro改为rw，并在后面添加init=/sysroot/bin/bash。按Ctrl+X进入系统。<br>
2. 单用户模式操作<br>
首先执行chroot /sysroot/，如要更改语言为英文执行LANG=en，然后就可以进行需要的操作。<br>

+ **救援模式**<br>
当系统无法进入GRUB时，需要外界媒介的系统来操作计算机。救援模式实际上是利用软盘（或USB）等外界媒介中的系统来操作计算机。因此，首先要进入计算机的[BIOS](https://en.wikipedia.org/wiki/BIOS)，修改
启动项为带有救援模式系统的外界媒介。然后启动并进入系统，对计算机的文件系统进行修改修复等操作。 


**Ref**: [https://blog.csdn.net/mojianbin/article/details/78286692](https://blog.csdn.net/mojianbin/article/details/78286692)
