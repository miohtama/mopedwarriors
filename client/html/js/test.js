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

	var clients = [];
	for(i=0; i<3; i++) {
		client = new Client();		
		clients.push(client);
	}
	
	$(clients[0]).bind("sessioncreated", function(event, client) {
		console.log("Server-side session created");
	})
	
	console.log("Player 1 creating first session");
	clients[0].createSession(server, "foobar");

});