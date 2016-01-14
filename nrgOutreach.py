#!/usr/bin/python
print "Content-Type: text/html"
print ""
import cgi
form = cgi.FieldStorage()
import csv
try:
    firstName = str(form["fn"].value).replace(" ", "")
except:
    firstName = "null"
else:
    pass

try:
    lastName = str(form["ln"].value).replace(" ", "")
except:
    lastName = "null"
else:
    pass

firstName = firstName.lower()
lastName = lastName.lower()

with open("nrgOutreach.csv") as csvfile:
    cr = csv.DictReader(csvfile)
    for row in cr:
    #print row
    #print (row['First Name'] + " " + row['Last Name'])
        if row['First Name'].replace(" ", "").lower() == firstName and row['Last Name'].replace(" ", "").lower() == lastName:
            dictionary = row
            del dictionary['First Name']
            del dictionary['Last Name']
        
print """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Newport Robotics Group Outreach Hours Lookup.">
    <meta name="author" content="Jeremy Zhang">

    <title>NRG Outreach Hours Lookup</title>

    <!-- Bootstrap Core CSS -->
    <link media="not print" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link media="not print" href="assets/css/logo-nav.css" rel="stylesheet">
    <link media="not print" href="assets/css/custom.css" rel="stylesheet">
    <link href="assets/css/print.css" rel="stylesheet">
    
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    
    <!-- Github Fork -->
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.1.1/gh-fork-ribbon.min.css" />
    <!--[if lt IE 9]>
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.1.1/gh-fork-ribbon.ie.min.css" />
    <![endif]-->
    
    <!-- Favicons -->
    <link rel="apple-touch-icon" sizes="57x57" href="assets/icn/apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="assets/icn/apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="assets/icn/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="assets/icn/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="assets/icn/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="assets/icn/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="assets/icn/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="assets/icn/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="assets/icn/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192"  href="assets/icn/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="assets/icn/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="assets/icn/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/icn/favicon-16x16.png">
    <link rel="manifest" href="assets/icn/manifest.json">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="msapplication-TileImage" content="assets/icn/ms-icon-144x144.png">
    <meta name="theme-color" content="#ffffff">
</head>

<body>
<div class="non-printable">
    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <!-- Fork Github -->
        <div class="github-fork-ribbon-wrapper right">
            <div class="github-fork-ribbon">
                <a href=" https://github.com/EndenDragon/nrgOutreach.cf">View me on GitHub</a>
            </div>
        </div>
        
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <a class="navbar-brand">
                    <img src="assets/img/logo.png" alt="">
                </a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        <a>Newport Robotics Group 948 Outreach</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Content -->
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <h1>NRG Outreach Hours Lookup</h1>
                <p>By Jeremy Zhang</p>
                
                <div class="col-md-8">
                <form action="nrgOutreach.py" method="get" id="nameForm">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title">Lookup</h3>
                        </div>
                        <div class="panel-body">
                            <div class="input-group input-group-lg">
                                <span class="input-group-addon" id="sizing-addon1"><span class="glyphicon glyphicon-user" aria-hidden="true"></span></span>
                                <input type="text" class="form-control" placeholder="First Name" aria-describedby="sizing-addon1" name="fn" required>
                                <input type="text" class="form-control" placeholder="Last Name" aria-describedby="sizing-addon1" name="ln" required>
                                <span class="input-group-addon">
                                    <button class="btn btn-default btn-large" type="button submit" value="Submit">Submit <span class="glyphicon glyphicon-ok" aria-hidden="true"></span></button>
                                </span>
                            </div>
                        </div> <div class="well well-sm"><div class="pull-right"><a href="" id="printJS" onclick="return false;">Print</a> <span class="glyphicon glyphicon-minus" aria-hidden="true" style="color: black;"></span> <a href="../">Clear</a></div>"""
totalHrs = 0

if firstName == "null" or lastName == "null":
    print """<div class="alert alert-danger" role="alert"><strong>Error:</strong>"""
    if firstName == "null":
        print " You didn't enter a first name!"
    if lastName == "null":
        print " You didn't enter a last name!"
    print "</div>"

print '<p style="color: #333;">'

try:
    print "<b>" + str(form["fn"].value).replace(" ", "") + " " + str(form["ln"].value).replace(" ", "") + "-</b>"
except:
    pass
else:
    pass

print "<br />"
print "Your outreach events (hours): <br>"
try:
    for x in dictionary:
        if dictionary[x] == "":
            dictionary[x] = 0
        print x + ":"
        print dictionary[x]
        totalHrs = totalHrs + float(dictionary[x])
        print "<br />"
    print "<br /><b>Total hours participated in outreach: " + str(totalHrs) + "</b>"
except:
    print """<div class="panel panel-danger">"""
    print """<div class="panel-heading"><h3 class="panel-title"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span> User not found! Double check if you typed it right or notify Jeremy.</h3></div>"""
    print '<div class=panel-body><p style="color:red">Either your name was incorrectly typed/not present in outreach master file, or you typed something wrong in the name fields above. Sorry about that!</p></div>'
    print "</div>"
print "</p>"

print """</div>
</div>
                </form>
                </div>
                <div class="col-md-4">
                    <div class="panel panel-default" style="color: #333;">
                        <div class="panel-heading">
                            <h3 class="panel-title">Friendly Outreach Reminder</h3>
                        </div>
                        <div class="panel-body">
                            <p>In order to be excused from school to attend local competitions, you need five hours of outreach.</p>
                            <p>In order to letter (and attend world competitions)- by way of the "outreach" path, you need a total of 25.</p>
                            <p>Outreach events come and go quickly, but we always announce them at meetings and over email.  You can also find them on the club's website - <a href="http://www.nrg948.com/">www.nrg948.com</a>.</p>
                            <br />
                            <strong>Please note: the hours may not be up to date. If you have any questions with the hours posted, please contact Delphine Lepeintre. Otherwise, for problems with the website, please contact Jeremy Zhang.</strong>
                        </div>
                    </div>
                </div>
                    <p class="pull-right" style="color: yellow;">&copy; 2015<script>new Date().getFullYear()>2010&&document.write("-"+new Date().getFullYear());</script>, by Jeremy Zhang.</p>
            </div>
        </div>
    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    
    <!-- Bootstrap Core JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</div>"""


print """
<script type='text/javascript'>//<![CDATA[
$(window).load(function(){
var print = `<html><head></head><body style="color: black;"><h1>Your NRG Outreach Hours</h1><p>Print friendly page from http://nrgOutreach.cf/</p><br>"""


totalHrs = 0

print '<p>'

try:
    print "<b>" + str(form["fn"].value).replace(" ", "") + " " + str(form["ln"].value).replace(" ", "") + "-</b>"
except:
    pass
else:
    pass

print "<br />"
print "Your outreach events (hours): <br>"
try:
    for x in dictionary:
        if dictionary[x] == "":
            dictionary[x] = 0
        print x + ":"
        print dictionary[x]
        totalHrs = totalHrs + float(dictionary[x])
        print "<br />"
    print "<br /><b>Total hours participated in outreach: " + str(totalHrs) + "</b>"
except:
    print """<p><strong>Error! User typed not found!</strong></p>"""


print """</p>

<p><b>Friendly outreach reminder: </b></p>
<p>In order to be excused from school to attend local competitions, you need five hours of outreach.</p>
<p>In order to letter (and attend world competitions)- by way of the "outreach" path, you need a total of 25.</p>
<p>Outreach events come and go quickly, but we always announce them at meetings and over email.  You can also find them on the club's website - <a href="http://www.nrg948.com">www.nrg948.com</a>.</p>
<br />
<p>Please note: the hours may not be up to date. If you have any questions with the hours posted, please contact Delphine Lepeintre. Otherwise, for problems with the website, please contact Jeremy Zhang.</p>


</body></html>`

$('#printJS').click(function(){
    $('.printable').html(print);
    window.print();
});
});//]]> 
</script>"""

print """
<div class="printable">
<p>Yo! Try pressing the "print" link on the page. If no print dialog shows up <strong>AFTER</strong> pressing the print link, proceed to print via your browser so the printable page can be loaded into the site.</p>
</div>

</body>

</html>"""
