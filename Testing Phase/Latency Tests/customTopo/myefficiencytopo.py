
from mininet.topo import Topo
from mininet.link import Intf
class myefficiencytopo(Topo):
	def __init__(self):
		Topo.__init__(self)
		#add Switches
		s1 = self.addSwitch('s1')
		s3 = self.addSwitch('s3')
		s7 = self.addSwitch('s7')
		#add Hosts
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
		h7 = self.addHost('h7')
		h8 = self.addHost('h8')
		# add Links
		self.addLink(h1, s1)
		self.addLink(h2, s1)
		self.addLink(h3, s1)
		self.addLink(h4, s1)
		self.addLink(h5, s1)
		self.addLink(h6, s1)
		self.addLink(s1, s3)
		self.addLink(s3, s7)
		self.addLink(h7, s7)
		self.addLink(h8, s7)



topos = { 'myefficiencytopo': ( lambda: myefficiencytopo() ) }
