# Assignment 05 - Functions, Modules, and Methods

As usual, please fork this assignment to your own repository and
clone the code locally to your computer. 

Like last assignment, we are going to be working with point patterns.   
The readings this week focused primarily on functions, modules, and to 
a lesser extent methods.  This assignment focuses on the first two.

Tasks:

1. Organize the functions that were in `point_pattern.py` into the appropriate
modules.
2. Update the tests to reflect the new structure.
3. Write a function to generate $n$ random points, where the user defines $n$.  Clarification: Please have the random points in the domain [0,1] for the functional tests to pass.
4. Write a function that takes $p$ an integer number of permutations.  For each 
permutation, create $n$ random points and compute the mean nearest neighbor
distance.  Let this function default to p=99 and n=100.  Make sure that the user 
can alter these values if they like.
5. Write a function to compute the critical points in the results returned by the
function you wrote in 4.  If p = 99, then the function in 4 should return a list
of 99 distances.  This function will take that list and find the smallest
and largest distances.  These are the critical points of the Monte Carlo test.
6. Write a function that takes the critical points of the Monte Carlo simulation
and the observed value and returns True if the observed distance is significant,
i.e., less than or greater than the observed.  Otherwise, return False.
7. Write tests for items 3, 4, 5, and 6.
8. Look at the file, functional_test.py.  In that file I have written a single
functional test that ties together all of your previous work.  For this test,
you should replace the module and function names with your own values.  For example,
I assume that all the necessary methods are in the point_pattern module.  Since you
refactored the structure of the code in completing #1, the point_pattern module
does not exist.  Instead, analytics and utils do.  Additionally,for #3 - 5, you 
wrote functions.  I guessed at what you might name these, but leave it
to you to update the functional test with the names you selected.

If you have any questions, please post in the forums.

Once you are happy with your assignment, go ahead and submit a pull request.
If TravisCI shows an error (red X in the pull request) feel free to update
your repository (`git add -A .`, `git commit`, `git push origin master`).  Please
*do not* open more than one pull request.


