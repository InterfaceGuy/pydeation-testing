from pydeation.imports import *


class DeepflattenTest(Scene):
    """tests nested groups, implicit visibility animations and deepflatten feature"""

    def construct(self):

        circles = Group(*[Group(*[Group(*[Circle(radius=20, x=x)
                                          for x in np.linspace(-30, 30, 2)], x=x) for x in np.linspace(-60, 60, 2)], x=x) for x in np.linspace(-120, 120, 2)])
        orbit = Circle(radius=100, p=PI / 2)

        self.play(
            Draw(circles, orbit, rel_start=1 / 4, rel_stop=1 / 2),
            UnDraw(circles, orbit, rel_start=1 / 2, rel_stop=3 / 4),
            Move(orbit, y=200, rel_stop=1 / 4),
            Move(orbit, y=-400, rel_start=1 / 4, rel_stop=3 / 4),
            Move(orbit, y=200, rel_start=3 / 4),
            Rotate(circles, h=3 * PI),
            Rotate(circles, h=3 * PI, unpack_groups=2),
            Rotate(circles, h=3 * PI, unpack_groups=1),
            Rotate(circles, h=3 * PI, unpack_groups=False),
            run_time=3)


class FourierTest(Scene):
    """tests the fourier animator"""

    def construct(self):

        n = 3
        arrows = []
        for i in range(n):
            arrow = Arrow((0, 0, 0), (0, 100, 0))
            arrows.append(arrow)

        null = Null()


class LettersTest(Scene):
    """testing text with individual letters"""

    def construct(self):

        letters = Letters("letters")


class DrawTest(Scene):
    """testing the draw animation"""

    def construct(self):

        sphere = Sphere()

        self.play(Draw(sphere), run_time=3)


class XTagTest(Scene):
    """testing xpresso tag"""

    def construct(self):

        sphere = Sphere()


# deepflatten_test = DeepflattenTest()
# fourier_test = FourierTest()
# letters_test = LettersTest()
# draw_test = DrawTest()
xtag_test = XTagTest()
