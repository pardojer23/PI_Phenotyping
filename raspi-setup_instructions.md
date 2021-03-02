Raspberry Pi Setup instructions
1) connect microSDHC card to computer
2) navigate to the folder on the card called "boot"
3) edit the wpa_supplicant.conf file with your 2.4GHz WiFi name and password
4) copy the wpa_supplicant.conf file to the boot folder
5) create a new empty file called ssh with no extension  
Note: be sure the file has no extension if you use a text editor to create it you may have to remove the ".txt" extension
6) eject the microSDHC card and place it in the raspberry pi
7)  Connect the raspberry pi to power  
Note: if using the power supply be sure to connect it to the right most micro-USB port labled "power in"
8) find the raspberry pi's IP address
  * On Linux / MAC open a terminal window and type `hostname -I` the first set of numbers should be your computers IP address
  * Your IP address should look something like 192.168.0.1
  * Now search the subnet that your computer is on for the raspberry pi
  * assuming your computer's ip is 192.168.0.1 type `sudo nmap -sS -p 22 192.168.0/24` into a terminal window and hit enter
  * look for the entry that has (Raspberry Pi Foundation) written next to the MAC Address
  * Scroll up to find the previous line that says "Nmap  scan report for" followed by an ip address. this is your Raspberry Pi's IP address 
  *On windows:
  * open the "command prompt" program
  *  type `IPCONFIG` and look for the line in the output that says "Default Gateway" the number listed is the ip address of your router
  * in your browser enter `http://[ip address]` replacing `[ip address]` with the ip address for your router
  * login the default username is most likely "admin" and the password is likely "password" unless you have changed these settings
  * look for a page that has the wireless client list. 
  * find a line that says raspberrypi and copy the ip address  
   
**Connect to your Pi**
* On Mac and Linux type `ssh pi@[ip address]` replacing [ip address] with the ip address of your raspberry pi
* on windows download and install putty and type the ip address in the appropriate box
* when prompted enter `pi` as the username
1) On all systems enter `raspberry` as the password when prompted
2) respond yes to any security warning
3) your command prompt should now read  something like `pi@raspberrypi:~$`
4) type `sudo raspi-config` and select the option for update using your arrow keys
5) after the update select `System Options` and then `Hostname`
6) change the hostname to something unique
7) select `System Options` and then Password and change the password
8) select `Interface Options` and then `Camera`. Enable the camera
9) select `finish`
10) maker a new directory called `test_pictures` by typing `mkdir /home/pi/test_pictures`
11) take a photo from the raspberry pi camera by typing `raspistill -o /home/pi/test_pictures/test_image.jpg`





