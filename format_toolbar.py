import gi
gi.require_version('Gtk', '3.0')
#gi.require_version('Granite', '1.0')
from gi.repository import Gtk

class FormatBar(Gtk.Box):

	def __init__(self):
		Gtk.Box.__init__(self)
		Gtk.StyleContext.add_class(self.get_style_context(), "linked")

		#bold
		self.bold = Gtk.ToggleButton()
		image =  Gtk.Image.new_from_icon_name("format-text-bold-symbolic", Gtk.IconSize.MENU)
		image.show()
		self.bold.add(image)
		self.bold.set_tooltip_text("Bold (Ctrl+B)")

		#Italic
		self.italic = Gtk.ToggleButton()
		image =  Gtk.Image.new_from_icon_name("format-text-italic-symbolic", Gtk.IconSize.MENU)
		image.show()
		self.italic.add(image)
		self.italic.set_tooltip_text("Italic (Ctrl+I)")

		#Underline
		self.underline = Gtk.ToggleButton()
		image =  Gtk.Image.new_from_icon_name("format-text-underline-symbolic", Gtk.IconSize.MENU)
		image.show()
		self.underline.add(image)
		self.underline.set_tooltip_text("Underline (Ctrl+U)")



		self.font_size = Gtk.ToggleButton.new_with_label("Font Size")


		self.pack_end(self.font_size,False,True,0)
		self.pack_end(self.underline,False,True,0)
		self.pack_end(self.italic,False,True,0)
		self.pack_end(self.bold,False,True,0)