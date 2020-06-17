# pedestrian_follow
Program is supposed to detect and track person on camera footage. 

This Version tracks face to allow tests indoor. To change program for body detection, toggle comments in lines 67 and 66. 

Camera will be placed on two servomotors controlled by STM32
script follow.py using opencv HaarCascade will detct human and comunicate with sevromotors via stm to keep person in the middle of image.

Hardware: STM32 NUCLEO-F746ZG, 2 servomotors, Data lines should be connected to PA6 -> X PC7-> Y 
