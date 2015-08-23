import gtk
from pymouse import PyMouse
import time 

p = PyMouse()

def get_pixel_colour(i_x, i_y):
	o_gdk_pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
	o_gdk_pixbuf.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), i_x, i_y, 0, 0, 1, 1)
	return tuple(o_gdk_pixbuf.get_pixels_array().tolist()[0][0])
 

green = (75, 219, 106)

raw_input("Press enter with the mouse over a non text area of the game")

pos = p.position()

print "Click on the blue area"

for i in range(10):
    #print i
    c = False
    while c != True:
        color = get_pixel_colour(pos[0], pos[1])
        if color == green:
            p.click(pos[0], pos[1], 1)
            c = True
     #       print "clicked"
            time.sleep(0.10)
            
    p.click(pos[0], pos[1], 1)

print "done"
