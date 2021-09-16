from manim import *


class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 20, 5],
            axis_config={"include_tip": False}
        )

        labels = ax.get_axis_labels(x_label="Weight", y_label="Height")

        self.play(FadeIn(ax, labels))
        # x = [0.8,2,3,4.3,10,11,12,13,14,14.8,15.1,15.2,15.7,15.9,16.1]
        # y = [2,2,3,5,2,2.2,2.5,2.6,4,5,6,7.5,12,15,19]

        x1 = [0.8,2,3,4.3]
        y1 = [2,2,3,5]

        x2 = [10,11,12,13,14,14.8,15.1]
        y2 = [2,2.2,2.5,2.6,4,5,6]

        x3 = [15.2,15.7,15.9,16.1]
        y3 = [7.5,12,15,19]


        data_points_manim_left_vg = VGroup(*[Dot(ax.coords_to_point(i,j)).scale(1.5) for i,j in zip(x1,y1)])
        data_points_manim_mid_vg = VGroup(*[Dot(ax.coords_to_point(i,j)).scale(1.5) for i,j in zip(x2,y2)])
        data_points_manim_right_vg = VGroup(*[Dot(ax.coords_to_point(i,j)).scale(1.5) for i,j in zip(x3,y3)])


        self.play(FadeIn(data_points_manim_left_vg,data_points_manim_mid_vg,data_points_manim_right_vg))
        self.play(data_points_manim_left_vg.animate.set_color(RED),data_points_manim_mid_vg.animate.set_color(GREEN),data_points_manim_right_vg.animate.set_color(RED))
        self.wait(1)

        # margin_line
        margin_line = Line(ax.coords_to_point(3,0),ax.coords_to_point(20,13)).set_color(YELLOW)
        self.play(Create(margin_line))





