# -*- coding: iso-8859-1 -*-

'''
Created on April 2014

@author: El Hadji Malick FALL && Adji Ndeye Ndate SAMBE

'''


import spade
import re
from xml.dom.minidom import Document

class Client(spade.Agent.Agent):
    def _setup(self):
        print "Demarrage du client . . ."
        b = self.Send()
        self.addBehaviour(b, None)

    def tearDown(self):
        self.stop()

    class Send(spade.Behaviour.OneShotBehaviour):
    
        """
        On definit le comportement : envoyer un message au server
        """

        def _process(self):
            # on forme l iD de lagent recepteur
            receiver = spade.AID.aid(name="agent_server@127.0.0.1",
                                     addresses=["xmpp://agent_server@127.0.0.1"])
	    
            # ensuite on construit le message
            self.msg = spade.ACLMessage.ACLMessage()  # On instancie le message 
            self.msg.setPerformative("inform")        # on definit le "inform" du FIPA
            self.msg.setOntology("myOntology")        # on definit l ontology du message
            self.msg.setLanguage("French")           # on definit la langue du message
            self.msg.addReceiver(receiver)            # on ajoute le destinataire

            #-------

	    doc = Document()

            regex = re.compile('[0-9.]*')

            #on ouvre le fichier renvoye par aruco
            fichier=open("../aruco-1.2.4/build/utils/test_video.txt","r")

            #on parcourt le fichier
            tmp=fichier.readlines()
            content=str(tmp)

            #on parse le fichier
            resultat = regex.findall(content)

            
            #on definit la racine du fichier
            racine = doc.createElement("coordonnees")
            doc.appendChild(racine)

            # un marqueur est un carre constitue des points p1, p2, p3 et p4
            
            #on definit la balise p1 : (coin inferieur gauche)
            element1 = doc.createElement("p1")
            element1.setAttribute("x", resultat[5])
            element1.setAttribute("y", resultat[7])
            racine.appendChild(element1)

            #on definit la balise p2 : (coin superieur gauche)
            element2 = doc.createElement("p2")
            element2.setAttribute("x", resultat[11])
            element2.setAttribute("y", resultat[13])
            racine.appendChild(element2)
 
            #on definit la balise p3 : (coin superieur gauche)
            element3 = doc.createElement("p3")
            element3.setAttribute("x", resultat[17])
            element3.setAttribute("y", resultat[19])
            racine.appendChild(element3)

            #on definit la balise p4 : (coin inferieur droit)
            element3 = doc.createElement("p4")
            element3.setAttribute("x", resultat[23])
            element3.setAttribute("y", resultat[25])
            racine.appendChild(element3)


            #on cree un fichier XML 
            monfichier = open("monfichier.xml", "w")

            #on y stocke les donnees xml crees
            monfichier.write(doc.toprettyxml())

            #on ferme les fichiers
            monfichier.close()
            fichier.close()
            
            # envoi des donnees ............................................
            #on ouvre le fichier xml
	    file = open ('monfichier.xml','r')

            #on parcourt le fichier
            c = file.readlines()
	    for line in c:
            	
                #on definit le contenu du message
		self.msg.setContent(str(line))
 
                #envoi du message
		self.myAgent.send(self.msg)
	    
            
            # fin envoi ......................................................
           
            #myAgent est un attribut qui peut etre utilise pour tout type de comportement
            #c est une reference a l agent qui tient le comportement et donc il peut etre
            #utilise comme un raccourci pour acceder a n importe quel methode ou
            #attribut de l'agent
            
	    file.close() 

if __name__ == "__main__":
    #comme on fait les tests sur une meme machine on utilise l'adresse localhost
    a = Client("agent_client@127.0.0.1", "secret")
    a.start()
