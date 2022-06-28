''' 
 based on riplpox 
'''

import logging
from copy import copy
from ecmp import HashHelperFunction

class Routing(object):
    '''Base class for data center network routing.

    Routing engines must implement the get_route() method.
    '''

    def __init__(self, topo):
        '''Create Routing object.

        @param topo Topo object from Net parent
        '''
        self.topo = topo
        

    def get_route(self, src, dst):
       
        raise NotImplementedError

class HashedRouting(Routing):
    ''' Hashed routing '''

    def __init__(self, topo):
        self.topo = topo


    def get_route(self, src, dst,util1):
        ''' Return flow path. '''
        return HashHelperFunction(self.topo,src,dst,util1)
'''
    def update_weights(self,dpid,port,utilization):
	return UpdateHelperFunction(self.topo,dpid,port,utilization)

'''       