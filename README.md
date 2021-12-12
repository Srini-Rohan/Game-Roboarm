### GAME ROBOARM
This is our submission for event named Hard-Wired conducted by Robotics Club - IITBHU
There are specific positions for every number on the die and the goal of the game is to rotate the arm by
60<sup>0</sup>  and close the gripper in the least number of turns. You can control the position of the robot arm with
hand gestures.
We use 3 gestures

Thumbs Up: Moves the arm to a specific position according to number on dice

Thumbs Down: Moves the arm to initial position

Fist : Closes the gripper

##### Controls of Game:
1. Hand Gestures
2. Roll a Die
Score of the game is (1/number of times the dice rolled)
Give a hand gesture after the dice is rolled.
##### Making of Game:
● Gesture Recognition: We removed background from the hand gesture image to get a segmented
image and developed a CNN architecture which takes segmented image and classifies hand
gestures.

● Dice Number Recognition: We Used blog detection of OpenCV library to detect the number of
circles present on the top face of the die.

##### Video:
https://user-images.githubusercontent.com/76437900/145723820-b14dc8e4-c41d-437b-b504-293974a5aebb.mp4

##### Run Simulation
Run below commands in 3 seperate terminals
```bash
roslaunch control run.launch
```
```bash
roscd control
python3 dice.py
```
```bash
roscd control
python3 gesture.py
```
##### Contributors:
<table>
 <td align="center">
     <a href="https://github.com/Srini-Rohan">
    <img src="https://avatars.githubusercontent.com/u/76437900?v=4" width="100px;" alt=""/><br /><sub><b>Gujulla Leel Srini Rohan</b></sub></a><br />
    </td>
  <td align="center">
     <a href="https://github.com/SaiHarshaKarna">
    <img src="https://avatars.githubusercontent.com/u/90554422?v=4" width="100px;" alt=""/><br /><sub><b>Sai Harsha</b></sub></a><br />
	</td>
  <td align="center">
     <a href="https://github.com/AYUSH-ISHAN">
    <img src="https://avatars.githubusercontent.com/u/77822265?v=4" width="100px;" alt=""/><br /><sub><b>Ayush Ishan</b></sub></a><br />
	</td>


</table>
