'''

based on riplpox 

'''



import sys

sys.path.append(".")



from mininet.topo import Topo

from mininet.node import Controller, RemoteController, OVSKernelSwitch, CPULimitedHost

from mininet.net import Mininet

from mininet.link import TCLink

from mininet.cli import CLI

from mininet.util import custom

from mininet.log import setLogLevel, info, warn, error, debug



from Topo import FatTreeTopo

from Routing import Routing



from subprocess import Popen, PIPE

from argparse import ArgumentParser

import multiprocessing

from time import sleep

import os





# Number of pods in Fat-Tree 

K = 4



# Queue Size

QUEUE_SIZE = 100



# Link capacity (Mbps)

BW = 10 



parser = ArgumentParser(description="minient_fattree")





parser.add_argument('-p', '--cpu', dest='cpu', type=float, default=-1,

        help='cpu fraction to allocate to each host')





args = parser.parse_args()







def FatTreeNet(args, k=4, bw=10, cpu=-1, queue=100, controller='DCController'):

    ''' Create a Fat-Tree network '''



    

    info('*** Creating the topology')

    topo = FatTreeTopo(k)



    host = custom(CPULimitedHost, cpu=cpu)

    link = custom(TCLink, bw=bw, max_queue_size=queue)

    

    net = Mininet(topo, host=host, link=link, switch=OVSKernelSwitch,

            controller=RemoteController, autoStaticArp=True)



    return net





def file_len(fname):

    with open(fname) as f:

        for i, l in enumerate(f):

            pass

    return i 

  



def iperfTrafficGen(args, hosts, net): 

  



	CLI(net)

	



def FatTreeTest(args,controller):

    net = FatTreeNet(args, k=K, cpu=args.cpu, bw=BW, queue=QUEUE_SIZE,

            controller=controller)

    net.start()





    # wait for the switches to connect to the controller

    info('** Waiting for switches to connect to the controller\n')

    sleep(4)



    hosts = net.hosts

    

    iperfTrafficGen(args, hosts, net)



    net.stop()



def clean():

    ''' Clean any the running instances of POX '''



    p = Popen("ps aux | grep 'pox' | awk '{print $2}'",

            stdout=PIPE, shell=True)

    p.wait()

    procs = (p.communicate()[0]).split('\n')

    for pid in procs:

        try:

            pid = int(pid)

            Popen('kill %d' % pid, shell=True).wait()

        except:

            pass



if __name__ == '__main__':



    setLogLevel( 'info' )

    



    #clean()



  

    FatTreeTest(args,controller='Controller')



    

    #clean()



    Popen("killall -9 top bwm-ng", shell=True).wait()

    #os.system('sudo mn -c')