from AsyncCelery import cele
from ConnectModule import Connect



@cele.task
def Check():
   a = Connect(Ip="34.92.205.178",Port="22",Username="root",Password="fedocx2009")
   a.SSHConnect()
   hostname = a.Command("hostname")
   return hostname
