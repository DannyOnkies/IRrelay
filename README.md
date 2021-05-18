# IRrelay
Turn on a lamp with a relay and a remote control

# Upgrade
* 19/05/2021 - Memory was filled abnormally. I have inserted a **`gs.collect()`** instruction, to free up the memory at each cycle. Also, the **`decode_it()`** function has been rewritten. Now 6 readings are carried out at each cycle in order to read 3 bits. 

# Project
With this project I want to switch a relay on and off using a remote control that I don't use.
![Image](https://github.com/DannyOnkies/IRrelay/blob/main/pic/photoaf%20(1).jpg "icon")

 With this project https://github.com/DannyOnkies/ObtainIRcodes I was able to find out which decimal 
 codes the remote emitted and this was useful for me in this project.
 
# Video
 In this video you can see how the program works. 
 
https://user-images.githubusercontent.com/80686975/118376035-d57f3300-b5c5-11eb-83e4-db54a66339e9.mp4

# Wiring diagram
Below you can see the wiring diagram of the circuit.
![IR_Command_schem](https://user-images.githubusercontent.com/80686975/118376139-75d55780-b5c6-11eb-897e-08295ec12883.jpg)

An image of the components.
![IR_Command_bb](https://user-images.githubusercontent.com/80686975/118376210-db294880-b5c6-11eb-8649-83f696e79b42.jpg)



