<?php 
	include("commun/entete.php");
	
	if(isset($_POST['nom']))
{
$la_civilite = $_POST['civilite']==1?'Madame':'Monsieur';
$le_nom = utf8_decode(addslashes($_POST['nom']));
$le_prenom = utf8_decode(addslashes($_POST['prenom']));
$la_naissance = $_POST['date_n'];
$le_mail = $_POST['mail_inscr'];
$le_mp = utf8_decode(addslashes($_POST['mp_inscr']));

$requete = "INSERT INTO inscr(inscr_civilite,inscr_nom,inscr_prenom,inscr_date,inscr_mail,inscr_mp) VALUES
('".$la_civilite."','".$le_nom."','".$le_prenom."','".$la_naissance."','".$le_mail."','".$le_mp."')";
$retours=mysqli_query($liaison,$requete) or die ("Probleme avec la requete");
}
?>
<script language="javascript" type="text/javascript">

	var b_civilite=false; var b_nom=false; var b_prenom=false;
	var b_date=false; var b_mail=false; var b_mp=false;
	
	function envoyer()
	{
		if(b_civilite==true && b_nom==true && b_prenom ==true && b_date ==true && b_mail ==true && b_mp)
		{
			document.getElementById("message").innerText = "Envoi serveur";
			document.getElementById("inscription").submit();
		}
		else
		{
			document.getElementById("message").innerText = "Le formulaire n'est pas complet";
		}
				document.getElementById("message").innerText += "-" + b_civilite + "-" + b_nom + "-" + b_prenom + "-" + b_date + "-" + b_mail + "-" + b_mp;		
	}

</script>
<script language="javascript" src="js/v_inscr.js"></script>			



<div class="topnav">
  <a class="active" href="#home">Accueil</a>
  <a href="#news">Boutique</a>
  <a href="#contact">Contact</a>
  <a href="#about">A propos</a>
    <div class="topnav-right">
        <button onclick="document.getElementById('id01').style.display='block'" style="width:auto;">Sign Up</button>
        <a href="#sinscrire">S'inscrire</a>
    </div>
</div>

<div style="padding-left:16px">
  <h2>Top Navigation Example</h2>
  <p>Some content..</p>
</div>

  <div id="id01" class="modal">
  <span onclick="document.getElementById('id01').style.display='none'" class="close" title="Close Modal">&times;</span>
  <form class="modal-content" action="/action_page.php">
    <div class="container">
      <h1>Sign Up</h1>
      <p>Please fill in this form to create an account.</p>
      <hr>
      <label for="email"><b>Email</b></label>
      <input type="text" placeholder="Enter Email" name="email" required>

      <label for="psw"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="psw" required>

      <label for="psw-repeat"><b>Repeat Password</b></label>
      <input type="password" placeholder="Repeat Password" name="psw-repeat" required>
      
      <label>
        <input type="checkbox" checked="checked" name="remember" style="margin-bottom:15px"> Remember me
      </label>

      <p>By creating an account you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>

      <div class="clearfix">
        <button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancelbtn">Cancel</button>
        <button type="submit" class="signupbtn">Sign Up</button>
      </div>
    </div> 
      
    
 

<?php 
	include("commun/pied.php");
?>