# bird-game

## Introduction
A bird game made using the Pygame Library in Python.

The game features a bird that the player can control to navigate through a series of pillars. The objective is to avoid collisions with the pillars and achieve the highest score possible (Score feature not yet in place).


## How to play?
The bird automatically falls down, you need to use the **spacebar ␣** to jump.
The pillars are generated at a regular interval which can be changed at line 85 of the [main.py file](./main.py).

## Requirements
Make sure you have **Python** installed on your system. Additionally, install the Pygame library using the following command:

```
pip install pygame
```
The **os** and the **random** modules are required, but are built-in modules in Python.

## Parameter tweaks
There are a couple of parameters you can change.

- The variable ```FPS``` in *line 9* controls the Frames per Second at which the game runs. Increasing this parameter will increase the speed of the gameplay.

- The variable ```VEL``` in *line 20* controls the velocity at which the bird moves up and down. Increasing this parameter will increase the rate at which the bird moves up and down.

- The variable ```PILLAR_VELOCITY``` IN *line 23* controls the velocity at which the x coordinate of the pillars changes. Increasing this parameter will increase the rate at which the pillars move from right to left and result in a similar result to 						increasing the FPS variable.

Other possible parameters such as ```BIRD_WIDTH```, ```BIRD_HEIGHT```, ```random_y```, are not recommended to be changed.
