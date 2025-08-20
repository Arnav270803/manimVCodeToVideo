from manim import *
import numpy as np  # needed for random scattering

class CubeAssembly(Scene):
    def construct(self):
        # Create a cube made of smaller cubes (like broken pieces)
        pieces = VGroup()
        offsets = [-0.5, 0.5]
        
        for x in offsets:
            for y in offsets:
                for z in offsets:
                    small_cube = Cube(side_length=1).move_to([2*x, 2*y, 2*z])
                    small_cube.set_fill(color=BLUE, opacity=0.8)
                    small_cube.set_stroke(WHITE, width=1)
                    pieces.add(small_cube)
        
        # Scatter them around randomly first
        scattered = pieces.copy()
        for cube in scattered:
            cube.shift(np.random.uniform(-3, 3, 3))
        
        # Show scattered pieces
        self.play(LaggedStart(*[FadeIn(cube) for cube in scattered], lag_ratio=0.2))
        self.wait(1)

        # Animate scattered pieces into a solid cube
        self.play(Transform(scattered, pieces), run_time=3)
        self.wait(2)
