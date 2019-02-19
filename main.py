import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

class ListBoxRowAlbumCover(Gtk.ListBoxRow):
    def __init__(self, coverImage):
        super(Gtk.ListBoxRow, self).__init__()
        self.coverImage = coverImage


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="gwmusic")
        self.set_default_size(320, 240)
        self.fullscreen()

        self.box1 = Gtk.Box()
        self.add(self.box1)


        self.button1 = Gtk.Button(label="X")
        
        self.button1.connect("clicked", self.on_X_clicked)
        self.box1.set_size_request(10, 0)
        self.box1.pack_start(self.button1, False, False, 0)
        
        
    def on_X_clicked(self, widget):
        Gtk.main_quit()
    


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()