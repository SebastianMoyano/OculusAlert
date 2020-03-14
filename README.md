# OculusAlert

 Python script to check on oculus quest
 
 # WARNING I DID THE CODE IN HALF AN HOUR TO 1 HOUR, SO IT MOST THAN CERTAIN HAS MANY FLAWS, USE IT AT YOUR OWN RISK.
 # ALSO IT WONT STEAL YOUR PASSWORD OR ANYTHING, EVERYTHING IS STORED LOCALLY.
  IVE TESTED AND IT WORKS OK FOR ME ATLEAST.
 
 This is a script that i made very fast, so you can check for any update on oculus quest.
 i made a .exe file so its easier to make it work if  you dont want to use the script.

 
 ## The Simple Way:
 
 1.- OculusAlert.exe and credential.txt must be in same dir 
 
 2.- Fill the credential.txt with email and password
 
 3.- Allow unsafe apps for gmail https://myaccount.google.com/lesssecureapps
 
 4.- Right click on OculusAlert.exe and open it. After it may look like nothing happend but it should be working in the background. If you want you can verify in task manager and look for OculusAlert (I recommend this)
 
 with this it should be ready,it will check each minute the oculus page and notify any changes.
 
 ## Using python script:
  
 1.- you need to have the last version of python, in my case python 3.8
 
 2.- you need to intall via pip bs4,schedule and requests 
 
 3.- put the script in the same dir as .txt, fill txt with corresponding info
 
 4.- allow unsafe apps for gmail https://myaccount.google.com/lesssecureapps
 
 5.- execute python script, this will promp a console window and print each time it searchs for info in the page.
 
## Script functionality:
 
The script first gets the raw info of https://www.oculus.com/quest/ page with requests.get() function, then with BeautifulSoup we scrap the page to get the div with the specific class in which we can find the text that shows if oculus is available or not, this is check latter with a if statement, if any version of the quest is available then we create a .ino file preventing excesive mailing to ourself, it should only send 1 mail. when nothing is available it deletes the file.
 
 

 
 Note: Each time your computer turns off you have to execute again.
 I've test it in windows 10 pro
 
### sorry for the sloppy description, i will complete it in the next few days
 
