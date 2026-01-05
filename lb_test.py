from manim import *

class LoadBalancerDeepDive(Scene):
    def construct(self):
        # 1. TEMPLATE STYLE (The ByteMonk standard)
        self.camera.background_color = "#000000"
        accent = "#00d4ff" 
        success = "#77ff00"
        
        grid = NumberPlane(
            background_line_style={"stroke_color": "#1a1a1a", "stroke_width": 1, "stroke_opacity": 0.4},
            axis_config={"stroke_opacity": 0},
        )
        self.add(grid)

        # 2. SCENE 1: THE PROBLEM (0s-15s)
        title = Text("LOAD BALANCER: THE TRAFFIC COP", font="Sans", weight=BOLD).scale(0.7)
        self.play(Write(title), run_time=3)
        self.wait(2)
        self.play(title.animate.to_edge(UP).scale(0.6))

        # 3. SCENE 2: SCALING (15s-45s)
        lb = VGroup(RoundedRectangle(height=1.5, width=1, color=accent), Text("LB", font_size=20)).shift(LEFT*2)
        servers = VGroup(*[
            VGroup(Rectangle(height=0.6, width=1.5), Text(f"Server {i}", font_size=14)) 
            for i in range(1, 4)
        ]).arrange(DOWN, buff=0.5).shift(RIGHT*3)

        self.play(Create(lb), FadeIn(servers), run_time=2)
        
        # Traffic Simulation (Automatic Step: Data Flow)
        for i in range(3):
            dot = Dot(color=WHITE).move_to(LEFT*5)
            path = Line(LEFT*5, lb.get_left(), color=WHITE)
            # Route to different servers
            target_server = servers[i]
            route = CurvedArrow(lb.get_right(), target_server.get_left(), angle=-TAU/12)
            
            self.play(MoveAlongPath(dot, path), run_time=1)
            self.play(MoveAlongPath(dot, route), run_time=1)
            self.play(Indicate(target_server, color=success))
            self.remove(dot)

        # 4. SCENE 3: WRAP UP (45s-60s)
        summary = Text("High Availability Achieved", color=success, font_size=24).shift(DOWN*3)
        self.play(Write(summary))
        self.wait(10)