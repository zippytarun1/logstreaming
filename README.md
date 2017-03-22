# logstreaming

Pre-Setup :

1/ Install Gunicorn and run gunicorn -w 5 stream:app 127.0.0.1:8088 

5 here means how many workers/threads we want to run  .We can change depending on how many request we want to handle at one point of time

2/ Now open 127.0.0.1:8080/page

3/ Now start entering data in output.txt file and save everytime data comes

4/ You will now see realtime data in browser


FYI : This will only read new data that we are entering currently .Old data available in file will not be printed 
