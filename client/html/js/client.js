/* */

function Client() {
	this.id = Math.random();

	this.serverAddress = "ws://localhost:10081/";
    this.ws = null;
    

}

Client.prototype.init = function init() {

}

Client.prototype.connect = function() {
	// Connect to Web Socket.
    // Change host/port here to your own Web Socket server.
    this.ws = new WebSocket(this.serverAddress);
    
    ws = this.ws;
    
    
    // Set event handlers.
    ws.onopen = function() {
    	console.log("Socket opened");
    };
    
    ws.onmessage = function(e) {
      // e.data contains received string.
      output("onmessage: " + e.data);
     
      
    };
    ws.onclose = function() {
      output("onclose");
    };
    ws.onerror = function() {
      output("onerror");
    };
   
}

Client.prototype.createSession = function(serverAddress) {
	
	this.serverAddress = serverAddress;	
	this.connect();	
	
	console.log("Connected to");
}

Client.prototype.joinSession = function(serverAddress, sessionId) {
	
}




