# password_generator
v1.0

At the icon there is a fisherman. Because in Turkish there is a phrase which used for who goes to fishing: "Rastgele". In English nearest words that i found 'randomly' and 'by chance'. 

This application created for password generation. When you push the generate button password generated and save randPwd.txt file. 
For run code you do not have to do steps down below. You can use this code also on ide with run button.

It is tested on Ubuntu 24.04 LTS distrbition. It works well. 

For transforming this code to an desktop application:
  on Linux: 
      Go to terminal (Ctrl + Alt + T)
      1. cd ~/Desktop
      2. nano randPwd.desktop // It will create a file and it will consists version informations.
      3. [Desktop Entry]
          Version=1.0
          Type=Application
          Name=randPwd // You can customize this part
          Exec=/fullpath/your_code
          Icon=/fullpath/fisherman.ico  // You can customize this part too.
          Terminal=false
          Categories=Utility;
      4. chmod +x randPwd.desktop
      5. At the end there is an icon on desktop. If icon is gray scale and has an 'x' on its right bottom side you should right click on icon and chose 'Allow Launching'.
