# A freeware plugin made by Ted Tinker for the zoologists of UCSB's Cheadle Center
# to aid human-assisted-image-processing of entomological specimens. 

# To use this plugin, put it in the plugins folder of GIMP.
# You must also have Python, and the PyGTK plugins for it.
# This also utylizes a WhiteBalanceStretch freeware plugin from Diego Nassetti.
# Once everything is installed, BugFlipper will appear in the GIMP menus under Filters.
# Click it, and a dialog prompt will appear in which you may choose two folders and some options.
# The program will open every JPEG starting with DSC_ in the first folder. It can flip the JPEG 180 degrees,
# color correct it, and open another dialog prompt requesting a name. Use the scanner gun to read the QR code in the image.
# If the photo is so blurry it's difficult to read the labels, mark the checkbox to flag it. Then scan the qr as normal, if possible.
# Then the image is saved with that filename in the second folder. 


#####


#!/usr/bin/env python

from gimpfu import * 	# For interacting with the GIMP
import os		# For pulling files from folders
import gtk		# The gtk code is adapted from Ben Duffield's Ardonis Wordpress. Thanks, Ben!
			# It's used for generating dialog boxes to prompt users for new filenames.
			# It comes with a checkbox marked "Flag bad image?" If checked, "bad_pic_" appended to filename start 

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
    dialog.set_markup('Enter New File Name. Use the scanner-gun on the QR if possible.')

    checkBlurry = gtk.CheckButton() 	# Add checkmark box
    entry = gtk.Entry()			# Add text-entry box				
    entry.connect("activate", responseToDialog, dialog, gtk.RESPONSE_OK)
    vbox = gtk.VBox(TRUE)						# Vertical box
    hbox1 = gtk.HBox(TRUE)						# First horizontal box has text-entry
    hbox1.pack_start(gtk.Label("New Filename:"), True, True, 0)
    hbox1.pack_end(entry)
    vbox.pack_start(hbox1) 						# Second horizontal box has checkbox
    hbox2 = gtk.HBox(TRUE)
    hbox2.pack_start(gtk.Label("Flag bad image"), True, True, 0)
    hbox2.pack_end(checkBlurry, True, True, 0)
    vbox.pack_end(hbox2)						# Done packing
    dialog.vbox.pack_end(vbox, True, True, 0)
    dialog.show_all()

    dialog.run()
    text = entry.get_text()

    if(checkBlurry.get_active()):	# If flagged, start filename with "bad_pic_"
	dialog.destroy()
	return "bad_pic_" + text

    dialog.destroy() 			# Otherwise, return filename
    return text

#####

def BugFlipper(OldDir,NewDir,renameMe,rotateMe,correctMe,deleteOld,imageQuality):
	for file in os.listdir(OldDir):						# Checks every file in first folder
		if (file.endswith(".jpg") and file.startswith("DSC_")): 	# Selects JPEGS beginning DSC_
			PrepareImage(file,OldDir,NewDir,renameMe,rotateMe,correctMe,imageQuality)	
										# Method for image processing
		if (deleteOld):
			os.remove(OldDir+"/"+file)				# Delete old photos, if selected
	return()

#####	

def PrepareImage(file,OldDir,NewDir,renameMe,rotateMe,correctMe,imageQuality):				# Processes photos
	image = pdb.gimp_file_load(OldDir+"/"+file,OldDir+"/"+file)
	drawable = pdb.gimp_image_get_active_layer(image)			
	if(rotateMe):
		pdb.gimp_drawable_transform_rotate_simple(drawable,ROTATE_180, 1,0,0,1)		# Rotate 180 degrees, if selected
	if(correctMe):
		drawable = pdb.python_fu_WhiteBalanceStretch(image,drawable)			# White/Color balance by Diego Nassetti, if selected
	if(renameMe):
		display = pdb.gimp_display_new(image)						# Displays the photo
		newFileName = getText()								# Asks user for new filename
		pdb.file_jpeg_save(image, drawable,NewDir+"/"+newFileName+".jpg",NewDir+"/"+newFileName+".jpg",
			imageQuality, 0,0,0,"newFileName",0,1,0,0)				# Save in second folder with new name and quality
		pdb.gimp_display_delete(display)						# Remove display
	else:
		pdb.file_jpeg_save(image, drawable,NewDir+"/"+file,NewDir+"/"+file,		# If not renaming, save with old name in new folder
			imageQuality, 0,0,0,"newFileName",0,1,0,0)	

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
	(PF_DIRNAME, "OldDir", "Folder with photos","C:\\"),	# Method Parameters
	(PF_DIRNAME, "NewDir", "Folder to save photos", "C:\\"),
	(PF_BOOL, "renameMe", "Rename photos?", 1),
	(PF_BOOL, "rotateMe", "Rotate photos 180 degrees?", 1),
	(PF_BOOL, "correctMe", "White-balance/color-correction?", 1),
	(PF_BOOL, "deleteOld", "Delete old photos after processing?", 0),
	(PF_SLIDER, "imageQuality", "Saved Image Quality", 1, [.01,1,.01])
    ],
    [],								# Method Return
    BugFlipper, menu="<Toolbox>/Filters")

main()
