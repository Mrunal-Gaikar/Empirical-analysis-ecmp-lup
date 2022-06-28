#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   link=TCLink, #must be added in order to change link  parameters eg. bw,delay etc. 
                   build=False
                   )

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController, 
                      ip='127.0.0.1',
                      port=6633,
                      ipBase="10.0.0.0/8")
                      

    info( '*** Add switches\n')
    
    es1=net.addSwitch( 's1', cls=OVSKernelSwitch )
    es2=net.addSwitch( 's2', cls=OVSKernelSwitch )
    
    es3=net.addSwitch( 's3', cls=OVSKernelSwitch  )
    es4=net.addSwitch( 's4', cls=OVSKernelSwitch)
    
    es5=net.addSwitch( 's5', cls=OVSKernelSwitch )
    es6=net.addSwitch( 's6', cls=OVSKernelSwitch )
    
    es7=net.addSwitch( 's7', cls=OVSKernelSwitch  )
    es8=net.addSwitch( 's8', cls=OVSKernelSwitch)
    
    
    as1=net.addSwitch( 's9', cls=OVSKernelSwitch )
    as2=net.addSwitch( 's10', cls=OVSKernelSwitch )
    
    as3=net.addSwitch( 's11', cls=OVSKernelSwitch )
    as4=net.addSwitch( 's12', cls=OVSKernelSwitch)
    
    as5=net.addSwitch( 's13', cls=OVSKernelSwitch )
    as6=net.addSwitch( 's14', cls=OVSKernelSwitch )
    
    as7=net.addSwitch( 's15', cls=OVSKernelSwitch  )
    as8=net.addSwitch( 's16', cls=OVSKernelSwitch )
    
    cs1=net.addSwitch( 's17', cls=OVSKernelSwitch )
    cs2=net.addSwitch( 's18', cls=OVSKernelSwitch )
    
    cs3=net.addSwitch( 's19', cls=OVSKernelSwitch )
    cs4=net.addSwitch( 's20', cls=OVSKernelSwitch)
    
    
    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.2',mac='00:00:00:00:00:21', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.3', mac='00:00:00:00:00:22',defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.1.2', mac='00:00:00:00:00:23',defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.1.3',mac='00:00:00:00:00:24',defaultRoute=None)
    
    h5 = net.addHost('h5', cls=Host, ip='10.1.0.2',mac='00:00:00:00:00:25', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.1.0.3',mac='00:00:00:00:00:26', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.1.1.2',mac='00:00:00:00:00:27', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.1.1.3',mac='00:00:00:00:00:28', defaultRoute=None)
  
    h9 = net.addHost('h9', cls=Host, ip='10.2.0.2', mac='00:00:00:00:00:29',defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.2.0.3',mac='00:00:00:00:00:30', defaultRoute=None)
    h11= net.addHost('h11', cls=Host, ip='10.2.1.2',mac='00:00:00:00:00:31', defaultRoute=None)
    h12= net.addHost('h12', cls=Host, ip='10.2.1.3', mac='00:00:00:00:00:32',defaultRoute=None)
    
    h13 = net.addHost('h13', cls=Host, ip='10.3.0.2',mac='00:00:00:00:00:33', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.3.0.3',mac='00:00:00:00:00:34', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.3.1.2',mac='00:00:00:00:00:35' ,defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.3.1.3',mac='00:00:00:00:00:36', defaultRoute=None)
   
    info( '*** Add links\n')
    net.addLink( es1, h1,bw=10)
    net.addLink( es1, h2 ,bw=10)
    net.addLink( es1, as1 ,bw=10)
    net.addLink( es1, as2,bw=10 )
    
    net.addLink( es2, h3,bw=10 )
    net.addLink( es2, h4 ,bw=10)
    net.addLink( es2, as1,bw=10 )
    net.addLink( es2, as2,bw=10 )
    
    net.addLink( es3, h5,bw=10 )
    net.addLink( es3, h6 ,bw=10)
    net.addLink( es3, as3,bw=10 )
    net.addLink( es3, as4 ,bw=10)
    
    net.addLink( es4, h7 ,bw=10)
    net.addLink( es4, h8 ,bw=10)
    net.addLink( es4, as3,bw=10 )
    net.addLink( es4, as4 ,bw=10)
    
    net.addLink( es5, h9 ,bw=10)
    net.addLink( es5, h10,bw=10 )
    net.addLink( es5, as5 ,bw=10)
    net.addLink( es5, as6 ,bw=10)
    
    net.addLink( es6, h11 ,bw=10)
    net.addLink( es6, h12,bw=10 )
    net.addLink( es6, as5,bw=10 )
    net.addLink( es6, as6 ,bw=10)
    
    net.addLink( es7, h13 ,bw=10)
    net.addLink( es7, h14,bw=10)
    net.addLink( es7, as7 ,bw=10)
    net.addLink( es7, as8 ,bw=10)
    
    net.addLink( es8, h15,bw=10 )
    net.addLink( es8, h16,bw=10)
    net.addLink( es8, as7,bw=10 )
    net.addLink( es8, as8,bw=10 )
    
    net.addLink( cs1, as1,bw=10 )
    net.addLink( cs1, as3 ,bw=10)
    net.addLink( cs1, as5 ,bw=10)
    net.addLink( cs1, as7,bw=10 )
    
    net.addLink( cs2, as1,bw=10 )
    net.addLink( cs2, as3 ,bw=10)
    net.addLink( cs2, as5,bw=10 )
    net.addLink( cs2, as7 ,bw=10)
    
    net.addLink( cs3, as2,bw=10 )
    net.addLink( cs3, as4 ,bw=10)
    net.addLink( cs3, as6,bw=10 )
    net.addLink( cs3, as8 ,bw=10) 
    net.addLink( cs4, as2,bw=10 )
    net.addLink( cs4, as4,bw=10)
    net.addLink( cs4, as6,bw=10 )
    net.addLink( cs4, as8,bw=10 )
   

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])
    net.get('s8').start([c0])
    
    net.get('s9').start([c0])
    net.get('s10').start([c0])
    net.get('s11').start([c0])
    net.get('s12').start([c0])
    net.get('s13').start([c0])
    net.get('s14').start([c0])
    net.get('s15').start([c0])
    net.get('s16').start([c0])
    
    net.get('s17').start([c0])
    net.get('s18').start([c0])
    net.get('s19').start([c0])
    net.get('s20').start([c0])
 
    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()


