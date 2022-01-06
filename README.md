# The Planet Saturn


### Intro
For this mini-project, I have made use of ursina, designed for developing games, as well as python language to create a visualization of the planet Saturn. The original idea of making such animation came from an honors research I have conducted during a semester in my undergraduate studies. The outcome has rather an entertaining purpose for the users.  


### Some Design Details
At the design level, I have used some techniques to overcome a few barriers which I thought would be interesting to share.

The first issue I encountered was the texture of the globe itself. I realized no matter what texture I use, the lines will always be vertical, whereas one can notice by a quick look that the lines are horizontal as if there are an ample number of round plates piled on top of each other. For the first attempt, I have tried to rotate the sphere by 90 degrees but after running the program the direction completely went off and the lings became vertical again. My second approach was to create a smaller globe as kind of a parent class for Saturn, rotating in the z-direction (horizontally clockwise) and called it fixed_entity in the code. Then I would fix the x rotational direction of Saturn as 80 degrees and put it as an outer shell for fixed_entity (Imagine a small marble, fixed_entity, trapped inside a bigger marble, Saturn, both with the same center point). Similar terminology applied to the rings. 

The second issue was after a few seconds through running the program, the planet started to move away from the camera point of view and disappeared into space. This bug was caused due to the fact that EditorCamera() function had no prior distance from the planet, therefore it stayed still while Saturn was slowly moving away. So, I defined a cam_lens distance from Saturn as the position of the camera. In this case, wherever the planet was moving, the camera was also capturing the movement at a constant distance from it.

The final issue worth mentioning was the ring itself. After a few tests and trials, I have come to realize that an oval-shaped texture can do the trick for having more realistic-looking rings than a triangular plane.  




### How Does It Work
The program has a simple function. The Planet Saturn starts rotating at an angle of 20 degrees from the horizontal line. The user can control the size of the planet by using the up and down arrows on the keyboard as well as navigating through the space by hovering the mouse around. Keyboard "Q" is used for quitting the program. 

### Challenges & Improvements
There is obviously a lot of room for improvement for this project that was made within a few days. As a computer graphics research enthusiast, I very much like to see what are the possibilities for adding shades and lighting to the scene. Ursina seems relatively new (if I'm not wrong) and there hasn't been much information around lighting features as far as I have looked into it. If you have any ideas/suggestions around that subject please feel free to educate me! :) Another bug that needs to be fixed is the resolution issue, especially with the rings. This precision issue would be more evident to see if we zoom into the shape. 



