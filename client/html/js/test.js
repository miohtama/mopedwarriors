/**
 * Some testing code stressting the client-server communications.
 *
 */


$(window).ready(function() {
	
	console.log("Starting tests");
	
	var server = "ws://localhost:9999/websocket";

	// Let the library know where WebSocketMain.swf is:
	WEB_SOCKET_DEBUG = true; 
	WEB_SOCKET_SWF_LOCATION = server + "/../swf/WebSocketMain.swf";

	var clientCount = 3;
	var sessionId = null;
	
	var clients = [];
	for(i=0; i<clientCount ; i++) {
		var client = new Client();			
		clients.push(client);
		
		$(client).bind("servertimeout", function(event, client, type, reply) {
			alert("Server timed out for call " + type + ". Did not get reply:" + reply);
		});
	}
			
	// Connect other clients to session created by client 1
	$(clients[0]).bind("sessioncreated", function(event, client, data) {
		
		sessionId = data.id;
		console.log("Server-side session created:" + sessionId);
		
		// Connect other clients to this session
		for(i=1; i<clientCount; i++) {
			var client = clients[i];
			console.log("Connecting client " + i);
			client.joinSession(server, sessionId);		
		}		
	});
			
	
	$(clients[0]).bind("connectionfailed", function(event, client) {
		alert("Could not connect to server:" + client.serverAddress);
	});
	
	console.log("Player 1 creating first session");
	clients[0].createSession(server, "foobar");

});