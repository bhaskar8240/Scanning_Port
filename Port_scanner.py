
import webbrowser
import nmap
import pyfiglet
import time

banner = pyfiglet.figlet_format('PortScanner')
print(banner) 
print('################### Wait scan in progress ######################')
myscan = nmap.PortScanner()
myscan.scan('enter your ip or range ','port or port range')


for host in myscan.all_hosts():
    
    print ('Host name is:%s (%s)'% (host,myscan[host].hostname()))
    print ('Status is:%s'% myscan[host].state())

    for proto in myscan[host].all_protocols():
        print('Protocol:%s'% proto)

        all_port = myscan[host][proto].keys()

        for port in all_port:
            ('Port:%s \t State:%s Product:%s'%(port, myscan[host][proto][port]['state'],myscan[host][proto][port]['product'] ))
            if myscan[host][proto][port]['state'] == 'open':
                print('='*80 +'\n'+'Starting the scan for http/https port'+'\n'+'='*80)
                if port == 80:
                    print('='*80 +'\n'+'You can access via http'+'\n'+'='*80)
                    access = 'http://%s:%s'%(host,port)
                    print(access)
                    webbrowser.open(access)
                elif port == 443:
                    print('='*80 +'\n'+'You can access via https'+'\n'+'='*80)
                    access ='https://%s:%s'%(host,port)
                    print(access)
                    time.sleep(4) 
                    webbrowser.open_new_tab(access)
                else:
                    print('='*80 +'\n'+'Nothing for access the web-portal'+'\n'+'='*80)
            else:
                print('NO port open for http/https')

     

