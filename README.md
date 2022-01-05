# The Planet Saturn


### Intro
For this mini-project I have made use of ursina, designed for developing games, as well as python language to create a visualization of the planet Saturn. The original idea of making such animation came from an honors research I have conducted during a semester in my undergraduate studies. The outcome has rather an entertaining purpose for the users.  


### Some Design Details
At the design level I have used some techniques to overcome a few barriers which I thought would be interesting to share.

The first issue I encountered with was texture of the globe itself. I realized no matter what texture I use, the lines will always be vertical, whereas one can notice by a quick look that the lines are horizontal as if there are an ample number of round plates piled on top of each other. For the first attempt, I have tried to rotate the sphere by 90 degrees but after running the programm the direction completely went off and the lings became vertical again. My second approach was to create a smaller globe as kind of a parent class for Saturn, rotating in the z direction (horizontally clockwise) and call it fixed_entity in the code. Then I would fix the x rotational direction of Saturn as 80 degrees and put it as an outer shell for fixed_entity (Imagine a small marble, fixed_entity, trapped inside a bigger marble, Saturn, both with the same center point). Simila terminology was applied to the rings. 

The second issue was when I ran the program, after a few seconds the planet started to move away from the camera point of view and dispapeared into the space. This bug was cause due to the fact that EditorCamera() function had to prior distance from the planet, therefore it stayed still while Saturn was slowly moving away. So, I defined a cam_lens distance from Saturn as the position of camera. In this acse, wherever the planet was moving, the camera was also acpturing the movement at a constant distance from it.

The final issue worth mentioning was the ring itself. After a few tests and trials I have come to realize that an oval shaped texture can do the trick for having a more realistic looking rings than a plane triangular shape.  




### How Does It Work
The program has a simple function. The Planet Saturn sphere starts rotating at an angle of 20 degrees from the horizontal line. The user can control the size of the object by using the up and down arrows on the keyboard as well as navigating through the space by hovering the mouse around. Keyboard "Q" is used for quitting the program. 

### Challenges and Rooms for Improvement
There are obviously a lot of rooms for improvement for this project that was made within a few days. 

adding shades and lights fixing rings precisouns 


