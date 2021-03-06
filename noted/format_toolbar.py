import gi
gi.require_version('Gtk', '3.0')
#gi.require_version('Granite', '1.0')
from gi.repository import Gtk


class FormatBar(Gtk.Box):

    def __init__(self):

        Gtk.Box.__init__(self)
        Gtk.StyleContext.add_class(self.get_style_context(), "linked")

        # bold
        self.bold = Gtk.ToggleButton()
        image = Gtk.Image.new_from_icon_name(
            "format-text-bold-symbolic", Gtk.IconSize.MENU)
        image.show()
        self.bold.add(image)
        self.bold.set_tooltip_text("Bold (Ctrl+B)")

        # Italic
        self.italic = Gtk.ToggleButton()
        image = Gtk.Image.new_from_icon_name(
            "format-text-italic-symbolic", Gtk.IconSize.MENU)
        image.show()
        self.italic.add(image)
        self.italic.set_tooltip_text("Italic (Ctrl+I)")

        # Underline
        self.underline = Gtk.ToggleButton()
        image = Gtk.Image.new_from_icon_name(
            "format-text-underline-symbolic", Gtk.IconSize.MENU)
        image.show()
        self.underline.add(image)
        self.underline.set_tooltip_text("Underline (Ctrl+U)")

        # font size
        # self.size = Gtk.Entry()
        # self.size.set_text(str(12))
        # self.size.set_max_width_chars(4)
        # self.size.set_width_chars(4)
        # self.size.set_max_length(2)

        # justification
        self.just_left = Gtk.Button()
        image = Gtk.Image.new_from_icon_name(
            "format-justify-left-symbolic", Gtk.IconSize.MENU)
        image.show()
        self.just_left.add(image)
        self.just_left.set_tooltip_text(
            "Left Justification (Select the entire line) (Ctrl+L)")

        self.just_center = Gtk.Button()
        image = Gtk.Image.new_from_icon_name(
            "format-justify-center-symbolic", Gtk.IconSize.MENU)
        image.show()
        self.just_center.add(image)
        self.just_center.set_tooltip_text(
            "Center Justification (Select the entire line) (Ctrl+E)")

        self.just_right = Gtk.Button()
        image = Gtk.Image.new_from_icon_name(
            "format-justify-right-symbolic", Gtk.IconSize.MENU)
        image.show()
        self.just_right.add(image)
        self.just_left.set_tooltip_text(
            "Left Justification (Select the entire line) (Ctrl+R)")

        self.just_fill = Gtk.Button()
        image = Gtk.Image.new_from_icon_name(
            "format-justify-fill-symbolic", Gtk.IconSize.MENU)
        image.show()
        self.just_fill.add(image)
        self.just_fill.set_tooltip_text(
            "Fill Justification (Select the entire line) (Ctrl+J)")

        #self.image = Gtk.Button()
        #image = Gtk.Image.new_from_icon_name(
        #    "multimedia-photo-manager", Gtk.IconSize.MENU)
        #image.show()
        #self.image.add(image)
        #self.image.set_tooltip_text("Add an image")

        self.send_feedback = Gtk.Button.new_with_label('Feedback')
        self.send_feedback.set_tooltip_text("Send Feedback")
        self.send_feedback.props.relief = Gtk.ReliefStyle(2)

        self.title = Gtk.Button.new_with_label("T")
        self.title.set_tooltip_text("Title (Ctrl+T)")

        self.header = Gtk.Button.new_with_label("H")
        self.header.set_tooltip_text("Header (Ctrl+H)")

        self.undo = Gtk.Button()
        image = Gtk.Image.new_from_icon_name("edit-undo-symbolic",Gtk.IconSize.MENU)
        image.show()
        self.undo.add(image)
        self.undo.set_tooltip_text("Undo")

        self.redo = Gtk.Button()
        image = Gtk.Image.new_from_icon_name("edit-redo-symbolic",Gtk.IconSize.MENU)
        image.show()
        self.redo.add(image)
        self.redo.set_tooltip_text("Redo")

        self.list = Gtk.ToggleButton()
        image = Gtk.Image.new_from_icon_name("view-list-compact-symbolic", Gtk.IconSize.MENU)
        image.show()
        self.list.add(image)
        self.list.set_tooltip_text("List (Ctrl+G)")

        self.buttons = {}
        self.buttons['bold'] = self.bold
        self.buttons['italic'] = self.italic
        self.buttons['underline'] = self.underline

        self.pack_end(self.send_feedback, False, False, 0)


        self.pack_start(self.bold, False, False, 0)
        self.pack_start(self.italic, False, False, 0)
        self.pack_start(self.underline, False, False, 0)
        self.pack_start(self.title, False, False, 0)
        self.pack_start(self.header, False, False, 0)
        #self.pack_start(self.image, False, False, 0)
        self.pack_start(self.just_left, False, False, 0)
        self.pack_start(self.just_center, False, False, 0)
        self.pack_start(self.just_right, False, False, 0)
        self.pack_start(self.just_fill, False, False, 0)
        self.pack_start(self.list,False,False,0)
        self.pack_start(self.undo,False,False,0)
        self.pack_start(self.redo,False,False,0)
        
        
