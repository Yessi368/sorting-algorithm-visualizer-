USE CASE DOCUMENT
Sorting Algorithm Visualizer

INTRODUCTION

This document describes the functional use cases of the Sorting Algorithm Visualizer system. It explains how users interact with the system and how the system responds to those interactions.

The system allows users to generate random arrays and visualize how different sorting algorithms operate step-by-step.

ACTORS

Primary Actor:
User – A student or developer interacting with the application.

System Actor:
Sorting Algorithm Visualizer System – The software that processes user input and displays sorting animations.

USE CASE 1: Generate Random Array

Actor: User

Description:
The user generates a new random array to begin the visualization process.

Preconditions:
The application must be running.

Main Flow:

The user clicks the "Generate Array" button.

The system generates a list of random numbers.

The system displays the numbers as vertical bars on the screen.

Postconditions:
A new unsorted array is displayed on the GUI.

USE CASE 2: Select Sorting Algorithm

Actor: User

Description:
The user selects a sorting algorithm to visualize.

Preconditions:
The application is running and algorithms are available.

Main Flow:

The user opens the algorithm selection dropdown.

The user selects a sorting algorithm (e.g., Bubble Sort).

The system stores the selected algorithm for execution.

Postconditions:
The selected algorithm is ready to run.

USE CASE 3: Start Sorting

Actor: User

Description:
The user starts the sorting visualization.

Preconditions:
An array has been generated.
A sorting algorithm has been selected.

Main Flow:

The user clicks the "Start Sorting" button.

The controller activates the selected sorting algorithm.

The sorting engine processes the array step-by-step.

The animation renderer updates the GUI after each comparison or swap.

The process continues until the array is fully sorted.

Postconditions:
The array is completely sorted and visually marked as sorted.

USE CASE 4: Adjust Speed

Actor: User

Description:
The user adjusts the animation speed of the sorting process.

Preconditions:
The application is running.

Main Flow:

The user moves the speed slider.

The system updates the delay time between animation steps.

The sorting animation reflects the new speed immediately.

Postconditions:
Sorting speed is updated according to user preference.

USE CASE 5: Reset Visualization

Actor: User

Description:
The user resets the system to its initial state.

Preconditions:
Sorting may be in progress or completed.

Main Flow:

The user clicks the "Reset" button.

The system stops any ongoing sorting process.

The system clears the current visualization.

The system returns to an idle state awaiting further input.

Postconditions:
The system is reset and ready for a new array generation.

ALTERNATIVE SCENARIOS

If the user attempts to start sorting without generating an array, the system will not proceed and may prompt the user to generate an array first.

If the user changes speed during sorting, the new speed will be applied immediately without restarting the algorithm.

SYSTEM STATES

Idle State – The system is waiting for user input.
Array Ready State – An array has been generated but sorting has not started.
Sorting State – The algorithm is currently executing and updating the visualization.
Completed State – The array is fully sorted and displayed.

SUMMARY

The Sorting Algorithm Visualizer system enables users to interactively understand sorting algorithms through real-time visualization. Users can generate arrays, select algorithms, start sorting, adjust animation speed, and reset the system. The system ensures clear separation between user interaction, control logic, algorithm processing, and animation rendering.