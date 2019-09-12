from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

test = 1.60934
class miletokm(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('miletokmfile.kv')
        return self.root
    def convert(self):
        value = self.get_validated_miles()
        converted = value * float(test)
        self.root.ids.mile_output.text = str(converted)
    def up(self):
        value = self.get_validated_miles()
        addnumber = value + 1
        self.root.ids.mile_input.text = str(addnumber)
    def down(self):
        value = self.get_validated_miles()
        minusnumber = value - 1
        self.root.ids.mile_input.text = str(minusnumber)
    def get_validated_miles(self):
        try:
            value = float(self.root.ids.mile_input.text)
            return value
        except ValueError:
            return 0


miletokm().run()