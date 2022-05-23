from pydeation.imports import *


class DeepflattenTest(Scene):
    """tests nested groups, implicit visibility animations and deepflatten feature"""

    def construct(self):

        circles = Group(*[Group(*[Group(*[Circle(radius=20, x=x)
                                          for x in np.linspace(-30, 30, 2)], x=x) for x in np.linspace(-60, 60, 2)], x=x) for x in np.linspace(-120, 120, 2)])
        orbit = Circle(radius=100, p=PI / 2)

        self.play(
            # Draw(circles, orbit, rel_start=1 / 4, rel_stop=1 / 2),
            # UnDraw(circles, orbit, rel_start=1 / 2, rel_stop=3 / 4),
            Show(circles, orbit),
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

        letters = Letters("letters", visible=True)


class DrawTest(Scene):
    """testing the draw animation"""

    def construct(self):

        sphere = Sphere()

        self.play(Draw(sphere), run_time=3)


class XPressionTest(Scene):
    """testing the xpression class"""

    def construct(self):
        
        sphere = Sphere()

        # gather desc_ids
        sketch_completion_desc_id = c4d.DescID(c4d.DescLevel(
            c4d.OUTLINEMAT_ANIMATE_STROKE_SPEED_COMPLETE, c4d.DTYPE_REAL, 0))

        # creat nodes
        object_node_out = XObject(sphere, link_target=sphere.sketch_material)

        # create ports
        parameter_port_out = object_node_out.obj.AddPort(c4d.GV_PORT_OUTPUT, sketch_completion_desc_id)

        # combine to xpression
        parameter = UParameter(sphere, sketch_completion_desc_id, link_target=sphere.sketch_material, name="SketchCompletion")
        animator1 = XAnimator(sphere, name="Draw", interpolate=True)
        animator2 = XAnimator(sphere, name="SinDraw", formula="sin(Pi*t)*sin(Pi*t)")
        composition1 = XAnimation(animator1, animator2, target=sphere, parameter=parameter)
        composition2 = XComposition((animator2,(0,1/2)), (animator1,(1/2,1)), target=sphere, name="FillThenDraw")


class PulseTest(Scene):
    """testing the pulse animator"""

    def construct(self):

        sphere = Sphere()

        self.play(
            Pulse(sphere, rel_stop=1/2),
            Pulse(sphere, n=3, filling_upper=0.1, rel_start=1/2),
            Move(sphere, x=-200, rel_stop=1/2),
            Move(sphere, x=200, relative=False, rel_start=1/2),
            run_time=3)

class OverrideControllerTest(Scene):
    """testing the updated override controller"""

    def construct(self):

        sphere = Sphere()
        
        self.play(Fill(sphere), run_time=1/2)
        #self.play(ChangeFillColorG(sphere, color_g=0), run_time=1/2)
        self.play(ChangeFillColorGB(sphere, color=RED), run_time=2+1/2)
        #self.play(ChangeFillColorGB(sphere, color=WHITE), run_time=1)
        #self.play(ChangeFillColorG(sphere, color_g=0), run_time=1)



# deepflatten_test = DeepflattenTest()
# fourier_test = FourierTest()
# letters_test = LettersTest()
# draw_test = DrawTest()
# xpression_test = XPressionTest()
# pulse_test = PulseTest()
override_controller_test = OverrideControllerTest()
