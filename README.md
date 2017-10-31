# GIMP-Plugin-Bug-Flipper
A Python-fu plug-in for the GIMP, for human-assisted-image-processing at UCSB's Cheadle Center.

This plug-in takes in two folders: one full of images to be processed, another for saving the processed images.
(There's no reason they can't be the same folder. Also, to find a folder, click the relevant box and select "other".)

This plug-in takes in a series of booleans: Should the files be renamed? Should they be rotated? Perform color correction? Should the old files be deleted? And so on.

This plug-in takes in one value via slider bar: What quality level should be used to save the images? (Default 30%)

One at a time, JPEG files beginning with "DSC_" from the first folder have the requested operations performed
(using color-correction from a freeware plug-in from Diego Nassetti). Then, if the image is to be renamed or edited, the image is displayed.

Then (and this was quite difficult to do, so thank you Ben Duffield for a helpful script) the plug-in brings up a dialog box
and the human user may input a string. Ideally, this string will be automatically found using a scanner-gun
on the QR-code visible in the processed image being displayed. The user may also flag the image as requiring a reshoot.

Then the JPEG is saved in the second folder with the input string as its filename. 

I'd like to thank Diego Nassetti and Ben Duffield for the Python-fu they provided online. The documentation for GIMP-fu isn't
as robust as it should be, and examining freeware is the only way to understand some of the limitations and work-arounds.
