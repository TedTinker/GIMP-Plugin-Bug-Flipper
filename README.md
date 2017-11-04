# GIMP-Plugin-Bug-Flipper
A Python-fu plug-in for the GIMP, for human-assisted-image-processing at UCSB's Cheadle Center.
GenericBugFlipper is similar, but with new options and different defaults for more general usage. 

Both versions of the plug-in prompt the user for two folders: one full of images to be processed, another for saving the processed images.
(There's no reason they can't be the same folder. You may modify the default pathnames in the registry function to save time.)

They prompt the user for a series of options: Should the files be renamed? Should they be rotated? Perform color correction? Should the old files be deleted? And so on.

There is one value input via slider bar: What quality level should be used to save the images? 
(Default 30%, which is almost indistinguishable from full-quality. Using 1% may compress the images beyond legibility.)

One at a time, selected image from the first folder folder have the requested operations performed
(using color-correction from a freeware plug-in from Diego Nassetti). If the image is to be hand-named or edited, the image is displayed.

Then (and this was quite difficult to do, so thank you Ben Duffield for a helpful example script) the plug-in brings up a dialog box
and the human user may input a string for the new filename. Ideally, this string will be automatically found using a scanner-gun
on a QR-code visible in the processed image being displayed. The user may also mark a checkbox to flag the image as requiring a reshoot;
if they do, the string "bad_pic_" is prepended to the filename given. If the filename box is left blank, it reuses the old filename. 

Then the image is saved in the second folder with its new filename, at the desired compression level. 

I'd like to thank Diego Nassetti and Ben Duffield for the Python-fu they provided online. The documentation for GIMP-fu isn't
as robust as it should be, and examining freeware is the only way to understand some of the limitations and work-arounds.
