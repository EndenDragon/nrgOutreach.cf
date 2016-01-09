# nrgOutreach.cf

## By Jeremy Zhang

[http://nrgOutreach.cf](http://nrgOutreach.cf/)

Newport Robotics Group (NRG948) Outreach Site

Make any changes that needed and submit a pull-request!

**Significant files and their purpose**

* index.html - Static HTML file asking members to input their name
* nrgOutreach.py - Python CGI file. Takes the name, process the `nrgOutreach.csv` file, and display the output. The webpage style mirrors everything on index.html.
* nrgOutreach.csv - User data to be processed.
* /assets - Javascript, CSS, imgs, & more!
* /upload - Uploads the csv files onto the site! ~Written in PHP due to the author’s lack of knowledge of using upload with Python.

Url format example for nrgOutreach.py to process: `http://nrgoutreach.cf/nrgOutreach.py?fn=Jeremy&ln=Zhang`

* First Name (fn): Jeremy
* Last Name (ln): Zhang