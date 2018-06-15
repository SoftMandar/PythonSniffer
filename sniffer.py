import sys
import socket
import struct

from packets import Ethernet

class Sniffer:


	def __init__(self, proto=None, all_proto=False):

		protocols = {
			"ICMP": socket.IPPROTO_ICMP,
			"TCP" : socket.IPPROTO_TCP,
			"UDP" : socket.IPPROTO_UDP,

		}

		try:
			self.sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
						socket.ntohs(0x0003))
		except socket.error as msg:
			print(msg)
			sys.exit(0)

	def start_sniffing(self):


		try:
			while True:

				data = self.sniffer_socket.recvfrom(65565)

				packet = data[0]
				self.process_packet(packet)

		except KeyboardInterrupt:
			self.sniffer_socket.close()
			sys.exit(0)

	def process_packet(self, packet):

		eth_pack = Ethernet(packet[0:14])
		print(eth_pack)



if __name__ == "__main__":


	snif = Sniffer(proto="TCP")
	snif.start_sniffing()
