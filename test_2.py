from manim import *

class LinkedListScene(Scene):
    def construct(self):
        # Create nodes (rectangles with text inside)
        node1 = Rectangle(width=2, height=1, color=BLUE).shift(LEFT*4)
        text1 = Text("Aryan").move_to(node1.get_center())

        node2 = Rectangle(width=2, height=1, color=GREEN).shift(ORIGIN)
        text2 = Text("Jay").move_to(node2.get_center())

        node3 = Rectangle(width=2, height=1, color=RED).shift(RIGHT*4)
        text3 = Text("Arnav").move_to(node3.get_center())

        # Group nodes with labels
        n1 = VGroup(node1, text1)
        n2 = VGroup(node2, text2)
        n3 = VGroup(node3, text3)

        # Create arrows (links)
        arrow1 = Arrow(node1.get_right(), node2.get_left(), buff=0.1, color=YELLOW)
        arrow2 = Arrow(node2.get_right(), node3.get_left(), buff=0.1, color=YELLOW)

        # Animate creation
        self.play(Create(node1), Write(text1))
        self.play(Create(node2), Write(text2))
        self.play(Create(node3), Write(text3))
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))

        # Add some cool animations
        self.play(n1.animate.shift(UP*0.5).scale(1.1), run_time=1)
        self.play(n2.animate.shift(DOWN*0.5).scale(1.1), run_time=1)
        self.play(n3.animate.shift(UP*0.5).scale(1.1), run_time=1)

        # Glow effect around nodes
        glow1 = Circle(color=BLUE, radius=1.2).move_to(n1).set_stroke(width=4)
        glow2 = Circle(color=GREEN, radius=1.2).move_to(n2).set_stroke(width=4)
        glow3 = Circle(color=RED, radius=1.2).move_to(n3).set_stroke(width=4)

        self.play(Create(glow1), Create(glow2), Create(glow3), run_time=1.5)
        self.wait(2)
