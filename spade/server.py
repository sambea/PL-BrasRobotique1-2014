# -*- coding: iso-8859-1 -*-

'''
Created on April 2014

@author: El Hadji Malick FALL && Adji Ndeye Ndate SAMBE

'''

import spade

class Server(spade.Agent.Agent):
    
    def _setup(self):
        print "Demarrage du serveur..."

        # ajouter "Receive" comme comportement par defaut
        rb = self.Receive()
        self.setDefaultBehaviour(rb)

    def tearDown(self):
        self.stop()

    class Receive(spade.Behaviour.Behaviour):

        """
        On definit le comportement: attendre des messages.
        """

        def _onStart(self):
            print "En attente du client ..."

        def _process(self):
            # on initialise le message a None
            self.msg = None

            #On cloque la reception pendant 10 secondes
            self.msg = self._receive(True, 10)

            #on cree le fichier xml ou seront stockees les donnes
	    monfichier = open("../simulation/fichierSimulation.xml", "a")

            # On teste l'arrivee d'un message
            if self.msg:
                print "J'ai recu un message!"
		st = self.msg.getContent()
                print "le message est", st
		
                #on supprime le message par defaut engndré par la connexion
                if st[1:9] != "presence":
                    #on ecrit les messages dans le fichier XML
                    monfichier.write(self.msg.getContent())
		
	    
		
            else:
                print "J'ai attendu, mais je n'ai reçu aucun message"
            
                #on ferme le fichier
                monfichier.close()

	    

        def onEnd(self):
            print "Server fermé."

if __name__ == "__main__":
    #on lance le serveur sur l'adresse localhost
    a = Server("agent_server@127.0.0.1", "secret")
    a.start()
    
