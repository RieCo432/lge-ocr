from PIL import Image
from pytesser import *
import urllib
import os
import unicodedata
import time
from datetime import datetime

while True:
    initTimestamp = datetime.now()

    i = 1
    nr_slides = 30
    all_text = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    while i <= nr_slides:

        urllib.urlretrieve("http://www.lge.lu/lgeapp/intranet/2006/1996/Slide"+str(i)+".JPG", "images/slide"+str(i)+".jpg")
        os.system("convert images/slide"+str(i)+".jpg -resize 1800 images/slide"+str(i)+".tif")
        text = image_to_string(Image.open("images/slide"+str(i)+".tif"))

        linenr = 1
        text_final = ""

        for line in text.split("\n"):
            if(not(line == "" or line == " " or line == "  " or line == "   " or line == "    ")):
                if(linenr == 1):
                    text_final = text_final+"<h4>"+line+"</h4>\n<p>"
                else:
                    text_final = text_final+"<br>"+line
            linenr = linenr + 1
            all_text[i] = text_final + "</p>\n"

        i = i + 1

    j = 1
    final_all_text = "<h4>Timestamp: "+time.strftime("%H:%M", time.localtime())+"</h4><br><br>\n"
    while j <= nr_slides:
        final_all_text = final_all_text + all_text[j]
        j = j + 1

    text_file = open("/home/server/www/lge/intranet_trans.html", "w")
    text_file.write(final_all_text)
    text_file.close()

    elapsedtime = datetime.now() - initTimestamp
    while elapsedtime.total_seconds() <= 900:
        time.sleep(15)
        elapsedtime = datetime.now() - initTimestamp
