'''
Lines Extended Demo
===================

This demonstrates how to use the extended line drawing routines such
as circles, ellipses, and rectangles. You should see a static image of
labelled shapes on the screen.
'''

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''


<LineRectangle>:
    canvas:
        Color:
            rgba: .1, .1, 1, .9
        Line:
            width: 2.
            rectangle: (self.x, self.y, self.width, self.height)
    Label:
        center: root.center
        text: 'Rectangle'

<LineBezier>:
    canvas:
        Color:
            rgba: .1, .1, 1, .9
        Line:
            width: 2.
            bezier:
                (self.x, self.y, self.center_x - 40, self.y + 100,
                self.center_x + 40, self.y - 100, self.right, self.y)
    Label:
        center: root.center
        text: 'Bezier'
''')




class LineRectangle(Widget):
    pass


class LineBezier(Widget):
    pass


class LineExtendedApp(App):
    def build(self):
        root = GridLayout(cols=2, padding=50, spacing=50)
        root.add_widget(LineRectangle())
        root.add_widget(LineBezier())
        return root


if __name__ == '__main__':
    LineExtendedApp().run()