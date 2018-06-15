import struct
from socket import(
		inet_aton,
		inet_ntoa
)
from ctypes import *


class Ethernet(Structure):

	_fields_ = [

		("dest", c_char * 6),
		("src",	 c_char * 6),
		("type", c_ushort),
	]

	def __new__(self, socket_buffer=None):
		return self.from_buffer_copy(socket_buffer)

	def __init__(self, socket_buffer):

		self.dest_mac = self.nmac_to_host(self.dest)
		self.source_mac = self.nmac_to_host(self.src)

	def __str__(self):
		return "Dest: {} Source: {}".format(self.dest_mac, self.source_mac)

	def nmac_to_host(self, _nmac):
		return ':'.join(['%02x' % b for b in _nmac])

class IP(Structure):

	_fields_ = [

		("ihl", 	c_ubyte, 4),
		("version", c_ubyte, 4),
		("tos", 	c_ubyte),
		("len",	 	c_ushort),
		("id", 		c_ushort),
		("offset",	c_ushort),
		("ttl",		c_ubyte),
		("protocol_t",c_ubyte),
		("sum",		c_ushort),
		("src",		c_ulong),
		("dst",		c_ulong),

	]

	def __new__(self ,socket_buffer=None):

		return self.from_buffer_copy(socket_buffer)

	def __init__(self, socket_buffer):


		"""self.protocols = {1: ,
						  6: ,
						  7:, }
						  """


class TCP(Structure):

	_fields_ = [


	]

	def __new__(self):

		pass

	def __init__(self):

		pass

class UDP(Structure):

	_fields_ = [


	]

	def __new__(self):

		pass

	def __init__(self):
		pass

class ARP(Structure):

	_fields_ = [

	]

	def __new__(self):

		pass

	def __init__(self):

		pass

class ICMP(Structure):

	_fields_ = [


	]


	def __new__(self):
		pass

	def __init__(self):
		pass
