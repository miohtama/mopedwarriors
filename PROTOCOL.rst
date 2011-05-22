=============================
 Game server protocol
=============================

This file describes the communication between the game server and the game client.

Websockets communications are used.

Each sent and received message is a JSON object.

	{
		"messageType" : "", // compulsory attribute 
		... // Other payload
	}

When client receives a message

* It will trigger an event handler of Client object whose name is on + eventType capitalized. E.g. if event type is "welcome" the called
  event handler is onWelcome.
  
* Client itself and the users of the client bind event handlers to communicate with the server 

Message sequence
=================

client: greet

server: welcome or forbidden

client: start session or create session

server: session data

server: more session data


