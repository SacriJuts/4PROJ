<?php 
	// Initialisation de la connexion
	
	$liaison = mysqli_connect("127.0.0.1","root","") or die ("Acc�s � la base de donn�e impossible !!!");
	mysqli_select_db($liaison, "formulaire_mail") or die ("Acc�s � la base de donn�e impossible !!!");
	
?>