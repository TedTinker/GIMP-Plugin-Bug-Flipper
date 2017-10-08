# A freeware plugin by Ted Tinker for the zoologists of Cheadle Center, UCSB.
# This freeware plugin by Ted Tinker was made for the zoologists of UCSB's Cheadle Center
# to aid human-assisted-image-processing of entomological specimens. 

# To use this plugin, put it in the plugins folder of GIMP 2.6.11.
# You must also have Python 2.6, pycairo, pygtk, and pygobject installed, as per
# this installation guide: https://www.cartographersguild.com/showthread.php?t=3060
# This also requires the WhiteBalanceStretch freeware plugin from Diego Nassetti.
# Once everything is installed, BugFlipper will appear in the GIMP menus under Filters.
# Click it, and a dialog prompt will appear in which you may choose two folders and a boolean.
# The program will open every JPEG starting with DSC_ in the first folder. It will flip the JPEG 180 degrees,
# color correct it, and open another dialog prompt requesting a name. Use the scanner gun to read the QR code in the image.
# Then the image is saved with that filename in the second folder. 
# If the boolean is "YES", the original images are deleted to save computer memory.


#####


#!/usr/bin/env python

from gimpfu import * 	# For interacting with the GIMP
import os		# For pulling files from folders
import gtk		# The gtk code is based on code from Ben Duffield's Ardonis Wordpress. Thanks, Ben!
			# It's used for generating dialog boxes to prompt users for new filenames. 

##### 

def responseToDialog(entry, dialog, response):
    dialog.response(response)
def getText():
    #base this on a message dialog
    dialog = gtk.MessageDialog(
        None,
        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
        gtk.MESSAGE_QUESTION,
        gtk.BUTTONS_OK,
        None)
    dialog.set_markup('Enter New File Name. Use the scanner gun if possible.')
    #create the text input field
    entry = gtk.Entry()
    #allow the user to press enter to do ok
    entry.connect("activate", responseToDialog, dialog, gtk.RESPONSE_OK)
    #create a horizontal box to pack the entry and a label
    hbox = gtk.HBox()
    hbox.pack_start(gtk.Label("Name:"), False, 5, 5)
    hbox.pack_end(entry)
    #some secondary text
    dialog.format_secondary_markup('This should begin with UCSB-')
    #add it and show it
    dialog.vbox.pack_end(hbox, True, True, 0)
    dialog.show_all()
    #go go go
    dialog.run()
    text = entry.get_text()
    dialog.destroy()
    return text

	# Problem: This dialog box is often opened behind other windows.
	# Future versions of this program will try to correct that. --Ted


#####

def BugFlipper(OldDir,NewDir,deleteOld):
	for file in os.listdir(OldDir):						# Checks every file in first folder
		if (file.endswith(".jpg") and file.startswith("DSC_")): 	# Selects JPEGS beginning DSC_
			PrepareImage(OldDir+"/"+file,NewDir)			# Method for image processing
		if (deleteOld):
			os.remove(OldDir+"/"+file)				# Delete old photos, if selected
	return()

#####	

def PrepareImage(file,NewDir):									# Processes photos
	image = pdb.gimp_file_load(file,file)
	drawable = pdb.gimp_image_get_active_layer(image)			
	pdb.gimp_drawable_transform_rotate_simple(drawable,ROTATE_180, 1,0,0,1)			# Rotate 180 degrees
	drawable = pdb.python_fu_WhiteBalanceStretch(image,drawable)				# White/Color balance by Diego Nassetti
	display = pdb.gimp_display_new(image)							# Display the photo
	newFileName = getText()									# Asks user for new filename
	pdb.gimp_file_save(image, drawable,NewDir+"/"+newFileName+".jpg",NewDir+"/"+newFileName)# Save in second folder with new name
	pdb.gimp_display_delete(display)							# Remove display

#####

register(
   	"BugFlipper",						# Name
   	"Made by Ted Tinker for Cheadle Center's zoologists",	# Blurb
   	"Made by Ted Tinker for Cheadle Center's zoologists for human-assisted-image-processing of standardized insect photos.",	# Help
	"Ted Tinker",						# Author
	"Ted Tinker, freeware",					# Copywrite
    	"2017",							# Date
    	"BugFlipper",						# Display Name
    	"",      						# No picture required
    [
	(PF_DIRNAME, "OldDir", "Folder to Flip","C:\\"),	# Method Parameters
	(PF_DIRNAME, "NewDir", "Folder to save", "C:\\"),
	(PF_BOOL, "deleteOld", "Delete old photos after processing?", 0)
    ],
    [],								# Method Return
    BugFlipper, menu="<Toolbox>/Filters")

main()