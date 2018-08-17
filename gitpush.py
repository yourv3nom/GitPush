try:
	import os
	import sys
	import time
	from sys import argv
	from colorama import *
	import subprocess
except KeyboardInterrupt:
	print "\nExiting"
	sys.exit()
except:
	pip = raw_input("Do you have colorama installed? [y/N] --> ")
	if "Yes" in pip or "yes" in pip or "y" in pip or "Y" in pip:
	  print "ok"
	if "No" in pip or "no" in pip or "n" in pip or "N" in pip:
	  os1 = raw_input("What OS? Centos or Debian? --> ")
	  if "debian" in os1 or "Debian" in os1:
	    shell("sudo apt install python-pip")
	    shell("sudo pip install colorama")
	  if "centos" in os1 or "Centos" in os1 or "CentOS" in os1 or "centOS" in os1:
 	   shell("yum install python-pip -y")
 	   shell("pip install colorama")

G1 = Style.BRIGHT + Fore.RED + "Exiting.." + Style.RESET_ALL
F1 = Style.BRIGHT + Fore.RED + "[!] MAKE SURE YOU ENTER ALL DIRECTORIES CORRECTLY [!]" + Style.RESET_ALL
F2 = Style.BRIGHT + Fore.CYAN + "[!] MAKE SURE YOU ENTER ALL DIRECTORIES CORRECTLY [!]" + Style.RESET_ALL
F3 = Style.BRIGHT + Fore.YELLOW + "[!] MAKE SURE YOU ENTER ALL DIRECTORIES CORRECTLY [!]" + Style.RESET_ALL
F4 = Style.BRIGHT + Fore.GREEN + "[!] MAKE SURE YOU ENTER ALL DIRECTORIES CORRECTLY [!]" + Style.RESET_ALL
x1 = Style.BRIGHT + Fore.MAGENTA + "		   _____ _ _   _____           _      " + Style.RESET_ALL
x2 = Style.BRIGHT + Fore.MAGENTA + "		  / ____(_) | |  __ \         | |     " + Style.RESET_ALL
x3 = Style.BRIGHT + Fore.MAGENTA + "		 | |  __ _| |_| |__) |   _ ___| |__   " + Style.RESET_ALL
x4 = Style.BRIGHT + Fore.MAGENTA + "		 | | |_ | | __|  ___/ | | / __| '_ \  " + Style.RESET_ALL
x5 = Style.BRIGHT + Fore.MAGENTA + "		 | |__| | | |_| |   | |_| \__ \ | | | " + Style.RESET_ALL
x6 = Style.BRIGHT + Fore.MAGENTA + "		  \_____|_|\__|_|    \__,_|___/_| |_| " + Style.RESET_ALL
x7 = Style.BRIGHT + Fore.YELLOW + " 		 	@yourv3nom - instagram            " + Style.RESET_ALL                 
G3 = Style.BRIGHT + Fore.RED + "Okay so here is how this is going to work: " + Style.RESET_ALL
G6 = Style.BRIGHT + Fore.CYAN + "1.) Go to github, login, and click the top right \"+\" sign and click new repository " + Style.RESET_ALL
G7 = Style.BRIGHT + Fore.CYAN + "2.) Name the repository the same thing as your folder containing your script(s) and leave a description " + Style.RESET_ALL
G8 = Style.BRIGHT + Fore.CYAN + "3.) Once you do that, there will be a link under the " + Style.RESET_ALL
G9 = Style.BRIGHT + Fore.CYAN + "4.) That link is what you will type when my script prompts you for the " + Style.RESET_ALL
G10 = Style.BRIGHT + Fore.RED + "Press ENTER when you're ready to continue with the script " + Style.RESET_ALL
G11 = Style.BRIGHT + Fore.RED + "\"Quick Setup - If you've done this thing before etc..\"" + Style.RESET_ALL
G12 = Style.BRIGHT + Fore.RED + "\"Whats the github repository name\"" + Style.RESET_ALL
G13 = Style.BRIGHT + Fore.RED + "Please realize this is a git command and i have no keyloggers in this script. VIEW source code if you dont trust it." + Style.RESET_ALL
G4 = Style.BRIGHT + Fore.CYAN + "Paste the link to the folder directory\nExample: [/home/venom/Desktop/Scripts/NameOfFolderWithTheScript] --> " + Style.RESET_ALL
G5 = Style.BRIGHT + Fore.CYAN + "Whats the github repository name?\nExample: [https://github.com/username/NameOfRepositoryOnGitHub.git] --> " + Style.RESET_ALL
G14 = Style.BRIGHT + Fore.CYAN + "\nTell me about the script in a sentence or two. Dont press ENTER key until done.\n--> " + Style.RESET_ALL 
G15 = Style.BRIGHT + Fore.CYAN + "Well, your script should be uploaded. Refresh the GitHub page and check if it worked.\nIf it didnt work, message me on instagram @yourv3nom and we'll see what went wrong. <3 " + Style.RESET_ALL
def shell(cmd):
	subprocess.call(cmd, shell=True)
                              
def venom():
	os.system("clear")
	print x1
	print x2
	print x3
	print x4
	print x5
	print x6
	print x7 + "\n"
	print G3 + "\n"
	print G6 
	print G7
	print G8 + G11
	print G9 + G12 + "\n"
	dedewd = raw_input(G10) 
	print "\n"
	print F1
	print F2
	print F3
	print F4 + "\n"
try:
	venom()
except KeyboardInterrupt:
	print "\n"+ G1
	sys.exit()
	
try:
	t5 = raw_input(G4) 
	print "\n"
	t6 = raw_input(G5)
	os.chdir(t5)
	os.system("touch README.md")
	t7 = raw_input(G14)
	g = open('README.md', 'a')
	g.write(t7)
	g.close()
	os.system("git init")
	os.system("git add *")
	os.system("""git commit -m "First Commit" """) 
	shell("git remote add origin " + t6)
	print G13
	os.system("git push -u origin master")
	print G15 
	sys.exit()
except KeyboardInterrupt:
	print "\n" + G1
