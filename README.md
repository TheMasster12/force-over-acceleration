force-over-acceleration
=======================
When finished, this project will be a 3D python app that runs simulations on a large number of point-particles. Features will be added as they are conceived.

Any help is appreciated, check the list below to see what needs to be worked on.

List of Features to Add
-----------------------
 * Implement Barnes-Hut approximation algorithm
 * Add visual cartesion coordinates display
 * Implement parallelization library to speed up computation
 * Make the physics more realistic by changing constants
 * Improve camera rotation system and possibly add support for mouse drag rotation

Testing
-------
You can write your own test files by writing bodies in the following format:
`x y z m vx vy vz`
where `x`, `y`, `z` are coordinates, `m` is mass, and `vx`, `vy`, `vz` are components of velocity.

Separate bodies with newlines and save in a file with the `.test` extension.

Then run your test file with `python force-over-acceleration.py test < file.test`

Documentation
-------------
All documentation is in HTML in the `doc/` folder. 

If you make changes, please document your code and run `docgen.sh` to update the documentation for all files. 

Installation
------------
You will need to install the following packages:
 * NumPy - `sudo pip install numpy`
 * PyOpenGL - `sudo pip install pyopengl`
 * FreeGLUT - `sudo apt-get install freeglut3-dev`