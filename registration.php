<html>
    <head> <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <script src="https://kit.fontawesome.com/aaf7f5e39f.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="css/form.css" />
        <title>Nguyen's Project</title>
    </head>
    <body>
    <header>
        <div class="child logo">
        <img src="images/logo.png" alt="Creator Logo">
        </div>
    <nav>
    <ul class="child">
        <li class="nav-effect"><a href="index.html">Main Page</a></li>
        <li class="nav-effect"><a href="page2.html">Page 2</a></li>       
        <li class="nav-effect"><a href="registration.php">Registration</a></li>
        
        </ul>    
    </nav>
        <div class="child" id="contactPhone">
        <a href="#"><i class="fas fa-phone-square"></i></a>
        </div>
        <div class="hero">
              <div class="center-content">
                <h1>Khanh Trinh Nguyen's Project</h1><h3>Creating a sample website for a Temple</h3>
            </div></div> 
        </header>
 <form action="action_page.php">
  <div class="container">
    <h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" id="email" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" id="psw" required>

    <label for="psw-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Repeat Password" name="psw-repeat" id="psw-repeat" required>
    <hr>

    <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>
    <button type="submit" class="registerbtn">Register</button>
  </div>

  <div class="container signin">
    <p>Already have an account? <a href="#">Sign in</a>.</p>
  </div>
</form> 
         </body>
</html>