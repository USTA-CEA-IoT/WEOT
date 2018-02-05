
<!DOCTYPE html>
<html>
<head>
<!-- <meta http-equiv="refresh" content="5" /> -->
<title>WEoT | Datos Ambientales</title>
<meta charset="utf-8">
<link href="../layout/styles/layout.css" rel="stylesheet" type="text/css" media="all">
</head>
<body id="top">
<!-- ################################################################################################ --> 
<!-- ################################################################################################ --> 
<!-- ################################################################################################ -->
<div class="wrapper row0">
  <div id="topbar" class="clear"> 
    <!-- ################################################################################################ -->
    <div class="fl_left">
      <ul class="nospace">
        <li><span class="icon-phone"></span> +00 (123) 456 7890</li>
        <li><span class="icon-envelope-alt"></span> info@domain.com</li>
      </ul>
    </div>
    <!-- ################################################################################################ --> 
  </div>
</div>
<!-- ################################################################################################ --> 
<!-- ################################################################################################ --> 
<!-- ################################################################################################ -->
<div class="wrapper row1">
  <header id="header" class="clear"> 
    <!-- ################################################################################################ -->
    <div id="logo" class="fl_left">
      <h1><a href="index.html">WEoT</a></h1>
    </div>
    <nav id="mainav" class="fl_right">
      <ul class="clear">
        <li><a href="index.html">Inicio</a></li>
        <li><a href="variables-ambientales.html">Gases Efecto Invernadero</a></li>
	<li class=active><a href="testdatos.php">Datos Ambientales</a></li>
      </ul>
    </nav>
    <!-- ################################################################################################ --> 
  </header>
</div>
<!-- ################################################################################################ --> 
<!-- ################################################################################################ --> 
<!-- ################################################################################################ -->
<div class="wrapper row2">
  <div id="breadcrumb"> 
    <!-- ########################################################################################## -->
    <ul>
      <li><a href="index.html">Inicio</a></li>
      <li><a href="testdatos.php">Datos Ambientales</a></li>
      
    </ul>
    <!-- ########################################################################################## --> 
  </div>
</div>
<!-- ################################################################################################ --> 
<!-- ################################################################################################ --> 
<!-- ################################################################################################ -->
<div class="wrapper row3">
  <main id="container" class="clear"> 
    <!-- container body --> 
    <!-- ########################################################################################## -->
    
    <h1 style="text-align:center;">Temperatura&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Humedad relativa</h1>

<?php
    $output = array();
   exec("python /var/www/html/default_data.py",$output);
    
    ?>

<table border="0" width="100%" cellpadding="8" cellspacing="8"> 
  <tr> 
<td width="50%"> 
    <table border="1"> 
    <tr> 
      <td style="vertical-align:middle;">
      <font size="16"><?php echo $output[0]; ?> Grados</font>
      </td> 
      
      <td valign="middle" align"center">
      <img src="images/gradosc.png" alt="" style="width:128px;height:128px;">
      </td> 
    </tr> 
   
    </table> 
</td> 

<td width="50%"> 
    <table border="1"> 
    <tr> 
      <td style="vertical-align:middle;">
      <font size="16"><?php echo $output[1]; ?>%</font>
      </td>      
      <td valign="middle" align"center">
      <img src="images/humedad.png" alt="" style="width:108px;height:128px;">
      </td> 
    </tr> 
    
    </table> 

</td> 
</tr> 
</table>

    <h1 style="text-align:center;">Concentración de Dióxido de Carbono &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Concentración de Metano</h1>


<table border="0" width="100%" cellpadding="8" cellspacing="8"> 
  <tr> 
<td width="50%"> 
    <table border="1"> 
    <tr> 
      <td style="vertical-align:middle;">
      <font size="16"><?php echo $output[3]; ?>PPM</font>
      </td>
      <td valign="middle" align"center">
      <img src="images/dioxido.png" alt="" style="width:128px;height:128px;">
      </td>
    </tr> 
   
    </table> 


</td> 
<td width="50%"> 
    <table border="1"> 
    <tr> 
      <td style="vertical-align:middle;">
      <font size="16"><?php echo $output[2]; ?>PPM</font>
      </td>
      <td valign="middle" align"center">
      <img src="images/metano.png" alt="" style="width:178px;height:128px;">
      </td> 
    </tr> 
    
    </table> 

</td> 
</tr> 
</table>



    <!-- ########################################################################################## --> 
    <!-- / container body -->
    <div class="clear"></div>
  <h4 style="text-align:center;">Última actualización: <?php echo $output[4]; ?></h4>
  </main>

<h1 style="text-align:center;">Mapa de ubicacion de los nodos de monitoreo ambiental</h1>
<div style="text-align:center;">
<iframe src="https://www.google.com/maps/embed?pb=!1m10!1m8!1m3!1d1320.9638424609013!2d-74.06395619873597!3d4.638127816263637!3m2!1i1024!2i768!4f13.1!5e0!3m2!1ses!2sco!4v1517349988996" width="800" height="600" frameborder="0" style="border:0" allowfullscreen></iframe>
</div>
<br>
</br>
</div>
<!-- ################################################################################################ --> 
<!-- ################################################################################################ --> 
<!-- ################################################################################################ -->

<div class="wrapper row4">
  <footer id="footer" class="clear"> 
    <!-- ################################################################################################ -->
    <div class="one_third first">
      <h6 class="title">Acerca de Nosotros</h6>
      <address class="push30">
      Centro de Excelencia y Apropiación en Internet de las Cosas CEA-IoT Nodo Universidad Santo Tomás<br>
      Calle 52 #9-62 Piso 3<br>
      Chapinero-Bogotá<br>
      </address>
    </div>

    <div class="one_third">
      <h6 class="title">Contactanos</h6>
      <ul class="nospace clear">
        <ul class="nospace">
        <li class="push10"><span class="icon-time"></span> Lunes - Viernes. 9:00am - 5:00pm</li>
        <li class="push10"><span class="icon-phone"></span> +57 (317) 539 2753</li>
        <li><span class="icon-envelope-alt"></span> info@weot.com.co</li>
      </ul>
        
      </ul>
    </div>
    <div class="one_third">
      
        <img src="images/logousta.png" alt="" style="width:700px;height:100px;">
        
        <img src="images/logoCEA.png" alt="" style="width:280px;height:80px;">
        
      </ul>
    </div>
    <!-- ################################################################################################ --> 
  </footer>
</div>
<!-- ################################################################################################ --> 
<!-- ################################################################################################ --> 
<!-- ################################################################################################ -->
<div class="wrapper row5">
  <div id="copyright" class="clear"> 
    <!-- ################################################################################################ -->
    <p class="fl_left">Copyright &copy; 2017 - Todos los derechos reservados - <a href="#">weot.usantotomas.edu.co</a></p>
    
    <!-- ################################################################################################ --> 
  </div>
</div
</body>
</html>
