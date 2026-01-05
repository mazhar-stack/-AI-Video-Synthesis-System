from manim import *

class JWTDeepDive(Scene):
    def construct(self):
        # 1. APPLY MASTER TEMPLATE
        self.camera.background_color = "#000000"
        accent, success = "#00d4ff", "#77ff00"
        grid = NumberPlane(
            background_line_style={"stroke_color": "#1a1a1a", "stroke_opacity": 0.4},
            axis_config={"stroke_opacity": 0}
        )
        self.add(grid)

        # 2. SCENE 1: THE LOGIN (0s-20s)
        title = Text("JWT AUTHENTICATION", font="Sans", weight=BOLD).to_edge(UP)
        user = VGroup(RoundedRectangle(height=1, width=1.5), Text("User", font_size=18)).shift(LEFT*5)
        auth_server = VGroup(RoundedRectangle(height=1.2, width=2, color=accent), Text("Auth Server", font_size=18)).shift(RIGHT*1)
        
        self.play(Write(title), Create(user), Create(auth_server))
        
        login_path = Arrow(user.get_right(), auth_server.get_left(), color=WHITE)
        self.play(GrowArrow(login_path), Write(Text("Credentials", font_size=14).next_to(login_path, UP)))
        self.wait(5)

        # 3. SCENE 2: TOKEN ISSUANCE (20s-45s)
        token = VGroup(Star(n=5, color=success).scale(0.2), Text("JWT", color=success, font_size=16)).next_to(auth_server, UP)
        self.play(Create(token), Indicate(auth_server, color=success))
        
        return_path = CurvedArrow(auth_server.get_left(), user.get_right(), angle=TAU/4, color=success)
        self.play(MoveAlongPath(token, return_path), run_time=2)
        self.wait(10)

        # 4. SCENE 3: ACCESS GRANTED (45s-60s)
        status = Text("Secure Session Active", color=success).scale(0.8).shift(DOWN*2)
        self.play(Write(status))
        self.wait(10)