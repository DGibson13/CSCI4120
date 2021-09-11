David Gibson
gibsond18@students.ecu.edu

There are two other team members but I could not get in contact with them. I tried email, canvas, and MS Teams with no success.
As a result, all the work for HW1 in this repository is done by me, David Gibson.

The file is for jupyter notebook. It imports from sklearn, matplotlib, pandas and warnings.
Warnings is imported and used because I was using a soon-to-be-deprecated bahavior in my loop.
In Jupyter Notebook, this caused the warning box to print for each iteration. This made it very difficult to see the results of the code, and so I decided
to use warnings.filterwarnings('ignore') to hide them.

I did not finish implementing the entire loop. It loops k from 1 through 20, but I did not do the five repititions for average accuracy.
As a result, I can only make an educated guess for which K has the best accuracy based on what I saw during testing.
It appeared to me that the k values around 5 seemed to have consistently high accuracy.
