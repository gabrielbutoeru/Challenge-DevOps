# Challenge-DevOps
Utilizzo di Ansible, Molecule e Travis CI per un esercizio sulla metodologia DevOps.


Questo playbook Ansible va a creare due istanze EC2 basate su CentOS 7.
Una volta fatto il deploy delle macchine le aggiorna, installa Docker e tutte le dipendenze necessarie e configura il sistema in modo che docker si sempre disponibile all'avvio e abbia a disposizione una partizione di 40 GB per l'archiviazione e l'esecuzione dei container.

File necessari
Chiave per accesso alle istanze
AWS > EC2 > Key Pairs > Create key pair
Una volta inserito un nome la chiave andrà scaricata e inserita nella cartella radice del progetto

Oltre a questo, sempre recandosi nella cartella radice del progetto, servirà dare:
chmod 400 chiave.pem 


Configurazione dell'ambiente.
Access Key and Secret Access Key 

Nella dashboardi di AWS recarsi in alto a destra. 
Nome utente > My Security Credentials > Access keys (Access key ID and secret access key > Create new access key > Download New access key

Aprire il file csv con un editor di testo per poterne leggere il contenuto ed eseguire i seguenti comandi

$ export AWS_ACCESS_KEY_ID=VALORE PRESENTE NEL CSV
$ export AWS_SECRET_ACCESS_KEY=VALORE PRESENTE NEL CSV
$ export AWS_DEFAULT_REGION=eu-central-1
