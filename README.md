Visual Learning Pattern Analysis + AI Video Synthesis System
📌 Project Overview
This project implements a hybrid system designed to automate the creation of technical educational videos. The system operates in two distinct phases:



Manual Step: An engineering analysis of a reference video (ByteMonk's "How WebSockets Work") to identify its unique "Visual DNA".



Automatic Step: An AI-driven engine that generates a new instructional MP4 video in that exact style for any user-provided topic.


🛠️ Tools & Technologies
The prototype uses the following open-source animation and synthesis frameworks:



Manim (Community Edition): For programmatically generating 2D diagrams, flowcharts, and transitions.



FFMPEG: For video encoding and media synthesis.


Python: The core logic engine for script generation and blueprinting.


VS Code: Primary development environment.

🚀 Features

Style Replication: Automatically applies identified visual patterns such as black backgrounds, #1a1a1a grids, and neon color palettes (#00d4ff, #77ff00).



Automated Scripting: Converts raw topics into structured narration and scene-by-scene concepts.



Dynamic Blueprinting: Generates an "Animation Blueprint" including element lists, timing, and transition instructions.



Rapid Rendering: Synthesizes high-definition MP4 videos with kinetic typography and flowchart animations.




📂 System Architecture
The system follows a 4-step pipeline:


Topic Input: User enters a technical topic (e.g., "Evolution" or "How DNS Works").


AI Logic Engine: Generates a narration script and divides the content into logical scenes.


Blueprint Synthesis: Translates the script into Manim-executable code based on the manual style profile.



MP4 Synthesis: Triggers the rendering engine to produce the final video file.

💻 Setup & Usage
Install Dependencies:

Bash

pip install manim
Run the Engine: Execute the controller script to start the automatic synthesis:

Bash
python synthesis_engine.py
Output: The generated video will be saved in the media/videos/ directory as GeneratedVideo.mp4

python synthesis_engine.py
Output: The generated video will be saved in the media/videos/ directory as GeneratedVideo.mp4.
