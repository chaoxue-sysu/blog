# PBS使用教程
## PBS安装

## PBS常见异常和解决方法汇总
+ #### 无法提交任务到指定节点
利用pbsnodes查看个节点状态，发现```bash message=ERROR: torque spool filesystem full```，表明torque中间文件系统已满，因此进入/var/spool/torque/spool清除文件，并重启pbs_mom: ```killall pbs_mom && pbs_mom``` 。
<br>(**Ref:** http://silas.net.br/tech/hpc/torque.html)

