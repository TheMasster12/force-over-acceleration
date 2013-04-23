force-over-acceleration
=======================

When finished, this project will be a 3D python app that runs simulations on a large number of point-particles. Features and functionality will be added as it is dreamed up.

Any help is appreciated, especially with the 3D graphics part of the project.

Testing
-------
You can write your own test files by writing bodies in the following format:
`x y z mass vx vy vz`
where `x,y,z` are coordinates, `mass` is mass, and `vx,vy,vz` are components of velocity.
Separate bodies with newlines and save in a file.

Then, to test, simply use the command
`python simulator.py test < file.test`
