### GAME ROBOARM
There are specific positions for every number on the die and the goal of the game is to rotate the arm by
60<sub>0</sub>  and close the gripper in the least number of turns. You can control the position of the robot arm with
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


