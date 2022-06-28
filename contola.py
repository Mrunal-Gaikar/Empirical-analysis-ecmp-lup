'''

Roll no : 2021H1030101P

'''



from pox.core import core

import pox.openflow.libopenflow_01 as of



log = core.getLogger()



class Learning_switch (object):

 

  def __init__ (self, connection):

    

    self.connection = connection  # Keep track of the connection to the switch so that we can send it messages 

    connection.addListeners(self) # This binds our PacketIn event listener   

    self.mac_to_port = {}           #This dictionary keeps track of which ethernet address is on which switch port (keys are MACs, values are ports)





  def send_pckt (self, packet_in, out_port):
 

    msg = of.ofp_packet_out()

    msg.data = packet_in   

    action = of.ofp_action_output(port = out_port)

    msg.actions.append(action)   

    self.connection.send(msg)   # Sends message to switch



  def Switch (self, packet, packet_in):   

    if packet.src not in self.mac_to_port:               #Adding the Input port information in the mac_to_port dictionary for a particular source if not already present

      self.mac_to_port[packet.src] = packet_in.in_port
            #print(mac_to_port)



    if packet.dst in self.mac_to_port:        

      self.send_pckt(packet_in, self.mac_to_port[packet.dst])

      print("In port = " ,packet_in.in_port)

      print("Source MAC =",packet.src)

      print("Destination MAC =",packet.dst)

      print("Out port=",self.mac_to_port[packet.dst])

      print("\n Mac table=")

      print(self.mac_to_port)          

      msg = of.ofp_flow_mod()      

      msg.match.dl_dst = packet.dst

      msg.actions.append(of.ofp_action_output(port=self.mac_to_port[packet.dst]))      

      self.connection.send(msg)



    else:

     

      self.send_pckt(packet_in, of.OFPP_ALL)  # Floods the packet 



  def _handle_PacketIn (self, event): 

    packet = event.parsed # This is the parsed packet data.

    if not packet.parsed:      

      return



    packet_in = event.ofp 

    self.Switch(packet, packet_in)





def launch ():
 

  def start_learning_switch(event):
	
    print(event.connection.dpid)   

    Learning_switch(event.connection)

  core.openflow.addListenerByName("ConnectionUp", start_learning_switch)
