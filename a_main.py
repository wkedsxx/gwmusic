import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf




class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="gwmusic")
		self.set_default_size(320, 240)
		self.builder = Gtk.Builder()
		self.builder.add_from_file("mainWin.glade")
		self.mainWin = self.builder.get_object("mainWin")
		self.mainWin.show_all()

win = MainWindow()
Gtk.main()