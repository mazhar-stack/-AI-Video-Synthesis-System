import os
import sys

def run_video_system():
    # PART B - STEP 2: TOPIC -> SCRIPT
    topic = input("Enter the technical topic for the video: ")
    
    # MANUAL STYLE PROFILE
    code_content = f"""from manim import *

class GeneratedVideo(Scene):
    def construct(self):
        # Apply Manual Style (Part A Foundation)
        self.camera.background_color = "#000000"
        accent, success = "#00d4ff", "#77ff00"
        grid = NumberPlane(
            background_line_style={{"stroke_color": "#1a1a1a", "stroke_opacity": 0.4}},
            axis_config={{"stroke_opacity": 0}}
        ).set_z_index(-1)
        self.add(grid)
        
        # Scene 1: Introduction
        title = Text("{topic.upper()}: AUTOMATED ANALYSIS", font="Sans", weight=BOLD).scale(0.7)
        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(FadeOut(title))

        # Scene 2: Flowchart Animation (Blueprint Elements)
        nodes = VGroup(
            VGroup(RoundedRectangle(height=1, width=2, color=WHITE), Text("User", font_size=18)),
            VGroup(RoundedRectangle(height=1, width=2, color=accent), Text("System", font_size=18)),
            VGroup(RoundedRectangle(height=1, width=2, color=success), Text("Output", font_size=18))
        ).arrange(RIGHT, buff=1.5)

        self.play(Create(nodes[0]), run_time=1)

        for i in range(len(nodes)-1):
            arrow = CurvedArrow(nodes[i].get_right(), nodes[i+1].get_left(), angle=-TAU/8, color=accent)
            self.play(Create(nodes[i+1]), Create(arrow), run_time=1.5)
            self.play(Indicate(nodes[i+1], color=accent))
            self.wait(1) 

        # Scene 3: Final Resolution
        final_text = Text("Process Complete", color=success).scale(0.6).to_edge(DOWN)
        self.play(FadeIn(final_text))
        self.wait(3) # Reduced wait to prevent terminal hanging
"""

    with open("generated_blueprint.py", "w") as f:
        f.write(code_content)

    print(f"\n--- Blueprint Created. Starting Part B - Step 4 (Rendering) ---")

    # Blueprint -> MP4
    os.system("manim -pqh generated_blueprint.py GeneratedVideo")
    
    print("\n--- Synthesis Finished. Terminal Ready for New Topic. ---")

if __name__ == "__main__":
    run_video_system()