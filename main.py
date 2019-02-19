import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="gwmusic")
        self.set_default_size(320, 240)
        self.fullscreen()

        self.button = Gtk.Button(label="X")
        self.button.connect("clicked", self.on_X_clicked)
        self.add(self.button)

    def on_X_clicked(self, widget):
        Gtk.main_quit()
    


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()