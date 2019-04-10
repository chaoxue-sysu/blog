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

### Linux修改最大文件句柄数
- **1 系统最大打开文件描述符数：/proc/sys/fs/file-max**
 + 1.1 查看
  ``` linux
  $ cat /proc/sys/fs/file-max
  186405
  ```
  + 1.2 设置
   + 临时性
``` linux
# echo 1000000 > /proc/sys/fs/file-max
```
   + 永久性：在/etc/sysctl.conf中设置
``` linux
fs.file-max = 1000000
```
- **2 进程最大打开文件描述符数：user limit中nofile的soft limit<br>**
+ 2.1 查看
``` linux
$ ulimit -n
1700000
```
  + 2.2 设置
   + 临时性：通过ulimit -Sn设置最大打开文件描述符数的soft limit，注意soft limit不能大于hard limit（ulimit -Hn可查看hard limit），另外ulimit -n默认查看的是soft limit，但是ulimit -n 1800000则是同时设置soft limit和hard limit。对于非root用户只能设置比原来小的hard limit。
查看hard limit：
``` linux
$ ulimit -Hn
1700000
``` 
设置soft limit，必须小于hard limit：
``` linux
$ ulimit -Sn 1600000
``` 
   + 永久性：上面的方法只是临时性的，注销重新登录就失效了，而且不能增大hard limit，只能在hard limit范围内修改soft limit。若要使修改永久有效，则需要在/etc/security/limits.conf中进行设置（需要root权限），可添加如下两行，表示用户chanon最大打开文件描述符数的soft limit为1800000，hard limit为2000000。以下设置需要注销之后重新登录才能生效：
``` linux
chanon           soft    nofile          1800000
chanon           hard   nofile          2000000
````
设置nofile的hard limit还有一点要注意的就是hard limit不能大于/proc/sys/fs/nr_open，假如hard limit大于nr_open，注销后无法正常登录。可以修改nr_open的值：
``` linux
# echo 2000000 > /proc/sys/fs/nr_open
```
- **3 查看当前系统使用的打开文件描述符数**
``` linux
# cat /proc/sys/fs/file-nr
5664        0        186405
```
其中第一个数表示当前系统已分配使用的打开文件描述符数，第二个数为分配后已释放的（目前已不再使用），第三个数等于file-max。

- **4 总结**

+ 所有进程打开的文件描述符数不能超过/proc/sys/fs/file-max
+ 单个进程打开的文件描述符数不能超过user limit中nofile的soft limit
+ nofile的soft limit不能超过其hard limit
+ nofile的hard limit不能超过/proc/sys/fs/nr_open

**Copy From**:[https://blog.csdn.net/hellozpc/article/details/47952867](https://blog.csdn.net/hellozpc/article/details/47952867)(侵权删除)
