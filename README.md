# timelapse
Timelaspe en python

#commande
nohup python3 champignon.py &

ls > stills.txt
sudo mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o tlcam.avi -mf type=jpeg:fps=24 mf://@stills.txt
