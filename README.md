# TextPasswordGenerator
Generates a password with two different files.
project.py will generate the password with possible repeatable segments, while non_repeat_project.py will not have repeatable segments.

These programs will generate a password with two files, they can be of any type, then generate a password from it.

dw_about_it.dll is the initial seed of the file.
seed.txt is meant to allow randomizing the password segments.

In the sample, dw_about_it.dll is the entire Bee Movie script, while seed.txt is the lyrics to All Star by Smash Mouth.

The code will append the lyrics to All Star to the Bee Movie script to change the value of the password generated to prevent repeated password.

Alternatively, you can run this after taking a picture, and generate a password with a picture.

The password is output onto password.txt.
