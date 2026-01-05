from manim import *

class DNSDeepDive(Scene):
    def construct(self):
        # --- 1. GLOBAL STYLE ---
        self.camera.background_color = "#000000"
        accent = "#00d4ff" 
        success = "#77ff00"
        
        # 2. THE CLEAN GRID: No center cross, very subtle color
        grid = NumberPlane(
            background_line_style={
                "stroke_color": "#1a1a1a", # Darker grey for a stealth look
                "stroke_width": 1,
                "stroke_opacity": 0.4
            },
            axis_config={"stroke_opacity": 0}, # Keeps the center clear
        )
        self.add(grid)

        # --- 3. SCENE 1: INTRO (0s - 12s) ---
        title = Text("DNS RESOLUTION PROCESS", font="Sans", weight=BOLD).scale(0.8)
        underline = Line(LEFT, RIGHT, color=accent).next_to(title, DOWN).scale(2.5)
        
        self.play(Write(title), Create(underline), run_time=3)
        self.wait(5) 
        self.play(FadeOut(title), FadeOut(underline))

        # --- 4. SCENE 2: NODES & CONNECTIONS (12s - 45s) ---
        user = VGroup(
            RoundedRectangle(height=1.2, width=2, corner_radius=0.2, color=WHITE),
            Text("Client", font_size=22)
        ).shift(LEFT * 5)

        resolver = VGroup(
            RoundedRectangle(height=1.4, width=2.4, color=accent),
            Text("DNS Resolver", font_size=22, color=accent)
        ).shift(LEFT * 1)

        self.play(Create(user), Create(resolver), run_time=2)
        
        # Animation: The Query
        query_arrow = Arrow(user.get_right(), resolver.get_left(), color=accent, buff=0.1)
        query_text = Text("Request: google.com", font_size=18).next_to(query_arrow, UP)
        
        self.play(GrowArrow(query_arrow), Write(query_text))
        self.wait(5)

        # Server Hierarchy
        servers = VGroup(
            VGroup(Rectangle(height=0.8, width=2.8), Text("Root Server", font_size=18)),
            VGroup(Rectangle(height=0.8, width=2.8), Text("TLD (.com)", font_size=18)),
            VGroup(Rectangle(height=0.8, width=2.8), Text("Authoritative", font_size=18))
        ).arrange(DOWN, buff=0.8).shift(RIGHT * 4)

        for server in servers:
            conn = CurvedArrow(resolver.get_right(), server.get_left(), angle=-TAU/12, color=GREY_B)
            self.play(FadeIn(server), Create(conn), run_time=1.5)
            self.play(Indicate(server, color=accent))
            self.wait(4) 

        # --- 5. SCENE 3: FINAL RESOLUTION (45s - 60s) ---
        res_box = RoundedRectangle(height=1, width=4, color=success, fill_opacity=0.1).shift(DOWN * 2.8)
        res_text = Text("IP: 142.250.190.46", font_size=26, color=success).move_to(res_box)
        
        # Return path
        final_arrow = Arrow(resolver.get_left(), user.get_right(), color=success, buff=0.1)
        
        self.play(Create(res_box), Write(res_text), run_time=2)
        self.play(GrowArrow(final_arrow))
        self.play(Indicate(user, color=success))
        
        self.wait(10) # Completing the 60s loop