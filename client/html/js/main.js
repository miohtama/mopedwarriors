

/**
 * Javascript main handler
 * @return
 */
function Main() {
	
}

Main.prototype.init = function() {
	this.client = new Client();	
}


/**
 * Start a WebSockets session with a gaming server.
 * 
 * Game server is identified by URL. One server can run several games so we need the session id also.
 */
Main.joinGame = function(server, gameId) {
	
}