/**
 * Client to a game server.
 * 
 * Connect to a game server. Start a new session or join to existing on.
 */

function Client() {
	this.id = Math.random();

	this.serverAddress = null;
    this.ws = null;
    
    // Timeout in seconds
    // For messages we expect reply 
    this.timeout = 5000;
    
    // message type -> timer handle mapping for messages which we are waiting for a reply
    this.repliesPending = {};
  
}

Client.prototype.init = function init() {

}

Client.prototype.connect = function() {
    this.opened = false;
    this.ws = new WebSocket(this.serverAddress);
    
    ws = this.ws;
    
    // Set event handlers.
    ws.onopen = $.proxy(this.onOpen, this);
    ws.onmessage = $.proxy(this.onMessage, this);
    ws.onclose = $.proxy(this.onClose, this);
    ws.onerror = $.proxy(this.onError, this);
   
}

Client.prototype.onOpen  = function() {
	console.log("Connection opened");
	this.opened = true;
	
	$(this).trigger("connectionopened", this);
		
	this.greet();
	
}


Client.prototype.onClose  = function() {
	if(!this.opened) {
		$(this).trigger("connectionfailed", this);
	}
	
	this.opened = false;
}


Client.prototype.onError  = function() {
	console.log("error");
}


/**
 * Assume messages use the protocol as defined in PROTOCOL.rst
 * 
 * @param msg WebSocket Message object
 */
Client.prototype.onMessage = function(msg) { 
	
	console.log("Message payload:" + msg.data);
	
	var data = JSON.parse(msg.data);
	var messageType = data.message.toLowerCase();
	var payload = data.payload;
	console.log("Got message:" + messageType);
	
	this.handlePendingReplies(messageType);
	
	$(this).trigger(messageType, [this, payload]);
}

/**
 * Send a message to a server.
 * 
 * @param message A Javascript object to send. This object is automatically serialized to JSON.
 */
Client.prototype.sendMessage = function(type, payload) {

	if(!payload) {
		throw "Payload missing";
	}
	
	var data = {"message" : type, "payload" : payload};
	
	
	var data = JSON.stringify(data);
	console.log("Sending message:" + data);
	this.ws.send(data);
}


/**
 * Send a message to a server and expect server to reply within a time frame.
 * 
 * @param type Message type as a string e.g. createSession
 * 
 * @param message A Javascript object to send. This object is automatically serialized to JSON.
 * 
 * @param reply Message type we expect the server to answer within the time frame
 */
Client.prototype.sendMessageExpectReply = function(type, payload, reply) {

	if(!reply) {
		throw "Reply type missing in sendMessageExpectReply";
	}
	
	reply = reply.toLowerCase();
	
	var handle = this.repliesPending[reply] || null; 
	
	if(handle) {
		delete this.repliesPending[handle];
		clearTimeout(handle);
	}
	
	
	// Do this thing in real function as local vars are subject to modify
	function setCallback(self, type, reply) {
	
		function timeoutCallback() {
			console.log("Client " + self.id + " message " + type + " never received reply " + reply);
			$(self).trigger("servertimeout", [self, type, reply]);
		}
		
		console.log("Setting timeout for " + self.timeout);
		var handle = setTimeout(timeoutCallback, self.timeout);
	
		self.repliesPending[reply] = handle;
	}
	
	setCallback(this, type, reply);
	
	this.sendMessage(type, payload);
	
}

/**
 * See if we are waiting for certain types of messages and clear timeout flag for those
 */
Client.prototype.handlePendingReplies = function(type) {
	
	console.log("Clearing timeout handle for " + type);
	
	var timerHandle = this.repliesPending[type] || null;
		
	if(timerHandle) {
		clearTimeout(timerHandle);
	} 
}


/**
 * Announce the server who am I by sending the initial handshake message.
 */
Client.prototype.greet = function() {

	var data= {
		id : this.id
	};
	
	this.sendMessage("greet", data);
}

/**
 * Connect to a server and create new gaming session.
 */
Client.prototype.createSession = function(serverAddress, name) {

	$(this).bind("welcome", function(event, client, data) {
		console.log("Got welcome. Now creating session");
		client.sendMessageExpectReply("createSession", {name:name}, "sessioncreated");
	});
	
	this.serverAddress = serverAddress;	
	this.connect();	
	
	console.log("Connected to");
}

/**
 * Connect to a server and join existing gaming session.
 */
Client.prototype.joinSession = function(serverAddress, sessionId) {
	
	this.serverAddress = serverAddress;	
	
	var self = this;
	
	$(this).bind("welcome", function() {
		self.sendMessageExpectReply("joinSession", {id:sessionId}, "joined");
	});
	
	this.connect();		
}




