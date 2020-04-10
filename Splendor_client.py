import socket  # Import socket moduleA
from Splendor_card_display import *
from Splendor_cards import *


'''
Client needs to display:
Table:  (note: eventually each of the cards will have an image as well)
L1, L2 and L3 decks:  card back color and a number of remaining cards in the stack
L1, L2, and L3 piles:  cards current face up on the table for each level (display type, victory points, cost for each card)
Nobles in play:  display "cost" and victory points
Bank:  number available for each gem type / gold coins

Player states to display (one for each player, you and the up-to-3 others)
Resources: number available for each gem type / gold coins
Purchased cards:  number of cards of each gem type, individual victory points per card
Reserved cards: cards that player has reserved (by taking a gold coin) and is NOT active
Total victory points
Total gems generated per turn
'''
s = socket.socket()  # Create a socket object

port = 61111  # Reserve a port for your service.
server_local_name = 'FW-CodingLaptop'
server_remote_IP_addr = '73.71.247.208'
try:
    server_name = server_local_name
    s = socket.create_connection((server_local_name, port))
except:
    server_name = server_remote_IP_addr
    s = socket.create_connection((server_remote_IP_addr, port))

print("Server is '%s', I received message '%s'" % (server_name, s.recv(1024).decode('ascii')))
s.close()
