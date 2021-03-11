# -*- coding: utf-8 -*-




import paramiko
import sys
import time
from functools import partial
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QCheckBox, QLineEdit, QLabel)



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())





class sshForNoobConnect(QWidget):

	

    def __init__(self):
        super(sshForNoobConnect, self).__init__()


        self.setWindowTitle('Ssh for noobs')
        self.setupUi()
        self.setupConnection()


        self.show()

    def setupUi(self):

        self.gridLayout = QGridLayout(self)
        self.resize(300,20)


        self.ip = QLineEdit()
        self.id = QLineEdit()
        self.mdp = QLineEdit()
        self.port = QLineEdit()
        self.mdpRoot = QLineEdit()		

        self.mdp.setEchoMode(QLineEdit.Password)
        self.mdpRoot.setEchoMode(QLineEdit.Password)

        self.ip.setPlaceholderText("Ip du serveur")
        self.id.setPlaceholderText("Nom de compte SSH")
        self.mdp.setPlaceholderText("Mot de passe SSH")
        self.port.setPlaceholderText("Port")
        self.mdpRoot.setPlaceholderText("Si compte non admin, mettre mdp compte root ici")

        self.rootCheck = QCheckBox("cocher si le compte est admin")


        self.ip.clearFocus()
        self.id.clearFocus()
        self.mdp.clearFocus()
        self.port.clearFocus()
        self.mdpRoot.clearFocus()

        self.port.setText("22")

        self.boutonOk = QPushButton("ok")
        self.boutonOk.setDefault(True)
        self.boutonOk.setFocus()


        self.gridLayout.addWidget(self.ip,0 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.id,1 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.mdp,2 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.port,3 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.rootCheck,4 ,0 ,1 ,6)
        self.gridLayout.addWidget(self.mdpRoot,5 ,0 ,1 ,6)

        self.gridLayout.addWidget(self.boutonOk,6 ,3 ,1 ,1)

    def setupConnection(self):

        self.boutonOk.clicked.connect(self.boutonOkDef)

    def boutonOkDef(self):

        username = str(self.id.text())
        host = str(self.ip.text())
        password = str(self.mdp.text())
        port = str(self.port.text())
        ssh.connect(host, port, username, password,timeout=100 )
        passwordRoot = str(self.mdpRoot.text())


        def send_string_and_wait(command, wait_time, should_print):
            shell.send(command)
            time.sleep(wait_time)
		    


        if self.rootCheck.isChecked():
            shell = ssh.invoke_shell()			
            send_string_and_wait("sudo -i\n", 1, True)
            send_string_and_wait(passwordRoot + "\n", 1, True)
            send_string_and_wait("apt-get update" + "\n", 1, True)
            send_string_and_wait("clear" + "\n", 1, True)


        else :
            shell = ssh.invoke_shell()			
            send_string_and_wait("su\n", 1, True)
            send_string_and_wait(passwordRoot + "\n", 1, True)
            send_string_and_wait("apt-get update" + "\n", 1, True)
            send_string_and_wait("clear\n", 1, True)
            
        class sshForNoob(QWidget):
            def __init__(self):
                super(sshForNoob, self).__init__()

                self.gridLayout2 = QGridLayout(self)
                self.setupUi2()

                self.setupConnections2()
                self.setWindowTitle('Ssh for noobs')
                self.resize(500,300)
                
                
            def actionBase(self, commandeBase):
                tempList = []
                shell.send("clear\n")
                shell.send(commandeBase)
                time.sleep(1)
                for line in shell.recv(10240).splitlines():
                    tempList.append(line.decode(errors='ignore'))
                del tempList[:3]
                varRetour = ' \n '.join(str(v) for v in tempList)

                self.retour.setText(varRetour)

            def actionBaseCour(self, commandeBase):
                tempList = []
                shell.send("clear\n")
                shell.send(commandeBase)
                time.sleep(1)
                for line in shell.recv(10240).splitlines():
                    tempList.append(line.decode(errors='ignore'))
                    
                del tempList[:3]
                del tempList[0:len(tempList)- 30]
                varRetour = ' \n '.join(str(v) for v in tempList)
                
                self.retour.setText(varRetour)




            def setupUi2(self):
                self.retour = QLabel("retour terminal")

                self.boutonMaj = QPushButton("maj")
                self.dist= QCheckBox("maj paquet \nnon essenciel")
                self.boutonInfoReseau = QPushButton("info reseau")
                self.boutonInfoProsso = QPushButton("info proco")
                self.boutonInfoRam = QPushButton("info ram")
                self.boutonInfoHdd = QPushButton("info HDD/SSD")

                self.paquet = QLineEdit()
                self.paquet.setPlaceholderText("nom du paquet ou service")


                self.affichagePaquet = QLabel("Gestion Paquets")

                self.boutonInstall = QPushButton("install")
                self.boutonStatus = QPushButton("status")
                self.boutonRemove = QPushButton("remove")
                self.boutonVersion = QPushButton("version")


                self.affichaqueService = QLabel("Gestion Services")

                self.boutonStart = QPushButton("start")
                self.boutonStop = QPushButton("stop")
                self.boutonRestart = QPushButton("restart")
                self.boutonStatusService = QPushButton("status")


                self.gridLayout2.addWidget(self.retour,0 ,0 ,3 ,4)

                self.gridLayout2.addWidget(self.boutonMaj,3 ,0 ,1 ,1)
                self.gridLayout2.addWidget(self.dist,3 ,1 ,1 ,2)
                self.gridLayout2.addWidget(self.boutonInfoReseau,4 ,0 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonInfoProsso,5 ,0 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonInfoRam,6 ,0 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonInfoHdd,7 ,0 ,1 ,1)


                self.gridLayout2.addWidget(self.paquet,3 ,3 ,1 ,2)

                self.gridLayout2.addWidget(self.affichagePaquet,4 ,3 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonInstall,5 ,3 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonStatus,5 ,4 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonRemove,6 ,3 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonVersion,6 ,4 ,1 ,1)

                self.gridLayout2.addWidget(self.affichaqueService,7 ,3 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonStart,8 ,3 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonStop,8 ,4 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonRestart,9 ,3 ,1 ,1)
                self.gridLayout2.addWidget(self.boutonStatusService,9 ,4 ,1 ,1)






            def setupConnections2(self):

                self.boutonMaj.clicked.connect(self.boutonMajDef)
                self.boutonInfoReseau.clicked.connect(self.boutonInfoReseauDef)
                self.boutonInfoProsso.clicked.connect(self.boutonInfoProssoDef)
                self.boutonInfoRam.clicked.connect(self.boutonInfoRamDef)
                self.boutonInfoHdd.clicked.connect(self.boutonInfoHddDef)

                self.boutonInstall.clicked.connect(self.boutonInstallDef)
                self.boutonStatus.clicked.connect(self.boutonStatusDef)
                self.boutonRemove.clicked.connect(self.boutonRemoveDef)
                self.boutonVersion.clicked.connect(self.boutonVersionDef)

                self.boutonStart.clicked.connect(self.boutonStartDef)
                self.boutonStop.clicked.connect(self.boutonStopDef)
                self.boutonRestart.clicked.connect(self.boutonRestartDef)
                self.boutonStatusService.clicked.connect(self.boutonStatusServiceDef)

            def boutonMajDef(self):

                if self.dist.isChecked():
                    self.actionBaseCour("apt-get upgrade -y\n")

                    self.actionBaseCour("apt-get dist-upgrade -y\n")
					
                else:
                    self.actionBaseCour("apt-get upgrade -y\n")


            def boutonInfoReseauDef(self):
                self.actionBase("ip a\n")

            def boutonInfoProssoDef(self):
                self.actionBase("lscpu\n")

            def boutonInfoRamDef(self):
                self.actionBase(str("free\n"))

            def boutonInfoHddDef(self):
                self.actionBase("fdisk -l\n")


            def boutonInstallDef(self):
                nomPaquet = str(self.paquet.text())
                nomPaquet = "apt-get install " + nomPaquet + " -y\n"
                self.actionBase(nomPaquet)

            def boutonStatusDef(self):
                nomPaquet = str(self.paquet.text())
                nomPaquet = "dpkg --status " + nomPaquet + "\n"
                self.actionBase(nomPaquet)

            def boutonRemoveDef(self):
                nomPaquet = str(self.paquet.text())
                nomPaquet = "apt-get remove " + nomPaquet + " -y\n"
                self.actionBase(nomPaquet)

            def boutonVersionDef(self):
                nomPaquet = str(self.paquet.text())
                nomPaquet = "apt-cache policy " + nomPaquet + "\n"
                self.actionBase(nomPaquet)			

            def boutonStartDef(self):
                nomPaquet = str(self.paquet.text())
                nomPaquet = "service " + nomPaquet + " start\n"
                self.actionBase(nomPaquet)

            def boutonStopDef(self):
                nomPaquet = str(self.paquet.text())
                nomPaquet = "service " + nomPaquet + " stop\n"
                self.actionBase(nomPaquet)

            def boutonRestartDef(self):
                nomPaquet = str(self.paquet.text())
                nomPaquet = "service " + nomPaquet + " restart\n"
                self.actionBase(nomPaquet)

            def boutonStatusServiceDef(self):
                nomPaquet = str(self.paquet.text())
                nomPaquet = "service " + nomPaquet + " status\n"
                self.actionBase(nomPaquet)

        self.fenetre2 = sshForNoob()
        self.fenetre2.show()
        self.close()

            
            
            
app = QApplication([])
fenetre = sshForNoobConnect()
fenetre.show()
app.exec_()