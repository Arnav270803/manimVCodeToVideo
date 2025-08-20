from manim import *
import numpy as np

class ComplexFromSimple(Scene):
    def construct(self):
        # Create many circles in a spiral pattern
        shapes = VGroup()
        for i in range(60):  # just a loop, simple code
            angle = i * 0.2
            radius = 0.15 * i
            circle = Circle(radius=0.2, color=interpolate_color(BLUE, PURPLE, i/60))
            circle.shift(np.array([radius*np.cos(angle), radius*np.sin(angle), 0]))
            shapes.add(circle)

        # Animate the spiral design
        self.play(LaggedStartMap(FadeIn, shapes, shift=UP, lag_ratio=0.05))
        self.wait(1)

        # Rotate everything for cool effect
        self.play(Rotate(shapes, angle=2*PI, run_time=6))
        self.wait(1)

        # Morph into a square grid
        grid = VGroup()
        for x in range(-5, 6):
            for y in range(-3, 4):
                dot = Dot(point=[x, y, 0], color=YELLOW)
                grid.add(dot)

        self.play(Transform(shapes, grid, run_time=4))
        self.wait(2)
