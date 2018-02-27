# HackCU2018


Jill Bill Volum IV

Team Members- Abhijit Suresh, Bhallaji Venkatesan, Sridhar Pavithrapu, Divya Sampath Kumar 

Description-

To cater to providing better disaster management strategies, we use the RPi Camera and FLIR camera connected to Raspberry Pi to stream a still image for facial recognition and a Video streaming of the premises on a Web Application that runs on a Flask server. The Web application displays essential characteristics about the image such as ethnicity, gender, age and other characteristics. It also identifies temperature profile of the location from the live video stream.


The process:

The prototype comprises of two Freewave Dev Kits, one that is directly connected to the Ethernet and the other that operates a remote node. The remote node is connected to a Raspberry Pi that has two types of cameras connected to it - The RPi Camera and the FLIR Camera from Sparkfun. To be precise, the chain is as follows:

             Raspberry Pi1              ->  Remote Freewave   ->    Freewave Node 2           ->  Remote Flask Server running  
 (With RPi Camera and FLIR)             Node 1                      connected to Ethernet                        Web Application

The Raspberry Pi1 sends 120 frames of IR image and 1 frame of RPi image that could be used for facial recognition over UDP to the Freewave Node 1. This Remote Node1 then communicates the frames over UDP to the Freewave central Node 2. The central node 2 then forwards these to a server running on a host machine over UDP to stream the frames on the Web Page that could later be used for planning out the rescue operations and to get data about the people in the disaster. The 120 frames sent over UDP are merged to generate a Live stream of the premise. 

We also connected the joystick to another Raspberry Pi to control camera movements mounted on a remote node.

       Raspberry Pi1              ->  Remote Freewave   ->    Freewave Node 2           ->  Remote Flask Server running  
(With RPi Camera and FLIR)                Node 1           connected to Internet                  Web Application


