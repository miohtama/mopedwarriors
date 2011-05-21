===========================
 Moped Warriors
===========================

A multiplayer experiement in HTML5 and Python

Client

* HTML5

* cocos2d-javascript

* websockets-js (Flash implementation for websockets)

Server

* Tornado 

* pygame

Installation
===============

Installation::

	git clone blablaba
	virtualenv virtualenv # use -p for force python 2.6
	source  virtualenv/bin/activate
	easy_install Tornado
	easy_install pygame
	
	
	https://github.com/gimite/web-socket-js/tree/hybi-07
	
Running the server
====================

	source virtualenv/bin/activate
	cd warriors
	python run.py
		
Communications
================

* Web server is started

	* Tornado listens port 80
	
* Browser opens index.html

* Browser downloads available game sessions from Tornado

	* User may choose an existing session to join
	
	* User may create a new sessions
	 		