# Calculating the average spin for a microstate

In this final set of exercises we are going to calculate yet another ensemble average.  The object that we are calculating the ensemble average of is rather complicated, however, so we are going to introduce the complexity slowly.  Hopefully, by doing things slowly you will, at the end of the process, be able to clearly see how we are using the ideas in the previous exercise on calculating an ensemble average when we compute the correlation function.

In this first exercise what I would like you to write a program that takes a list of spin variables as input.  In other words, the input to your program will the coordinates for a particular microstate.  Your program should then return the average value of the spin in the microstate, which will be given by:

![](https://render.githubusercontent.com/render/math?math=\langle\s\rangle=\frac{1}{N}\sum_{i=1}^Ns_i)

In this expression, the sum runs over the number, ![](https://render.githubusercontent.com/render/math?math=N), of spins in the system so the ![](https://render.githubusercontent.com/render/math?math=s_i) values are the spin variables.
