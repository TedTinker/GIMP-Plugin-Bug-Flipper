# GIMP-Plugin-Bug-Flipper
Python-fu plug-in for the GIMP, for human-assisted-image-processing at UCSB's Cheadle Center.

This plug-in takes in two folders: one full of images to be processed, another for saving the processed images.
This plug-in takes in one boolean: Do you want to delete the pictures after processing?

One at a time, JPEG files from the first folder are rotated 180 degrees and color corrected using a freeware plug-in from Diego Nassetti.
Then the image is displayed.

Then (and this was quite difficult to do, so thank you Ben Duffield for a helpful script) the plug-in brings up a dialog box
and the human user may input a string. Ideally, this string will be automatically found using a scanner-gun
on the QR-code visible in the processed image being displayed. Then the image is saved in the second folder
with the input string as its filename. 
