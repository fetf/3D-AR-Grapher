# 3D-AR-Grapher
Hackathon Project: Graph your 3D equations in AR!

Written by Richard Sbaschnig, Victor Liu, Julian Chavez  
Submitted to [ThetaHacks 2021](https://thetahacks.tech/) ([Devpost](https://thetahacks.devpost.com/))  
See full project [here](https://devpost.com/software/3d-ar-grapher)  
[Video Demo](https://youtu.be/tCQJtKbdkGI)  
## Inspiration
We wanted to make a useful program for students by using both Wolfram and EchoAR APIs, so we thought of 3D graphing in AR.

## What it does
On the website, you input a 3D equation and the graph window size, and the website will display the 3D model of the graph in AR.

## How I built it
We used HTML, Javascript, and Flask for the website. We used the Wolfram Client Library for Python, EchoAR API, and Flask for receiving website data, creating a 3D model from it, and displaying the result as an AR 3D object.

## Challenges I ran into
We had trouble converting website data into a format the Wolfram Client Library could understand, and with uploading and directing the user to the AR 3D model. However, we did find solutions to all these challenges.

## Accomplishments that I'm proud of
We made the integration between the Wolfram Client Library and EchoAR run smoothly, and we made the website available to any device on the local network through Flask.

## What We learned
We learned the ins and outs of the Wolfram and EchoAR APIs, along with how to create web servers with Flask.

## What's next for 3D AR Grapher
We would improve the UI to look more appealing, and we would offer users more customization for their graphs.
