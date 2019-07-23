# Labelling

## From Unsupervised to Supervised Learning

Clustering is a knowledge acquisition technique. In short, rather than asking everyone about everything, first cluster the data
then only check a sample of rows from each cluster.

For example, clustering is one way to help _active learning_.
Often we have more rows than labels (a.k.a. classes) for that data (that is, most of our data is suitable only for unsupervised learning). This is a common situation.
For example:

- Suppose it takes 15 seconds to read a four line Github issue before you can say if that issue is 
  "about a bug" or "otherwise".
- Suppose further you have 10,000 such issues to read. Assume you can stand doing that for 20 hours in a standard 35 hour work week (which is actually a  bit of a stretch), and suppose that
  you label issues ina  group of two (so that when labels disagree, you go ask the other person). That labelling task will take two people, four weeks to complete[^mt]-- and you many just
  not have time for that.

[^mt]: Some might comment that this four weeks could be done in an hour, via
[crowdsourcing](https://www.youtube.com/watch?v=Pjm1uYbuyk4),  That's true BUT consider- when comissioning a crowdsourcing rig, you have to first certify the efficacy of that rig. That means
you need some "ground truth" to check the conclusions. So now you are back to labelling some significant percentage of the data. 

For another example:

- Suppose you are doing effort estimation for software projects. It is relatively much harder to access financial details about a project (e.g. the salaries of the workers) than
  the product details about that software.
- This means that your data has many independent rows (the product details) but little or no dependent information.


Given some oracle that can label data (e.g. a human being), and assuming that oracle takes time $$t$$ or costs $$x$$  everytime you ask it a question,
then _active learning_ is the process of learning an adequate model after asking the oracle using minimum time and/or cost.

(Aside: Another way to handle label-shortage is  _semi-supervised_ learning that finds things similar to the labelled examples,
then propagates the labels to the unlabelled space. For example, if you cluster data, then (a) each cluster will have a few labels and (b) the unlabelled
examples in each cluster can be given that cluster's majority label.  Of course, you still have to check if the resulting new labels are correct.
If you want to do that check effeciently (i.e. not check everything) then you'll need some smart way to check a sub-sample of the new labels.
At which point you are back to active learning-- but perhaps with fewer overall queries to the oracle).

An _aquisition function_ is one way to guide an active learner:

- Given a model built from the $$L$$ labels seen to date, go forth and make guesses; i.e. use the tiny model built so far to guess labels for the remaining data.
- Apply the aqusition function to select the most interesting guess
     - e.g. select the guess with the highest/lowest score (if you are truing to maximimze/ minimize something).
     - e.g. select the guess with the highest uncertainty
     - e.g. or select the guess with higest score plus uncertainty
- Give that most interesting guess  to an oracle. Ask them to label it
- Build a new model from  the $$L+1$$ labels.

Here are some important details about the above process:

- When building a new model using the new label, it is useful if the new model can be incrementally 
    - If the number of labelled examples is very small, then anything will do. 
    - But as the labelled space grows, consider using learners that incrementally update very quickly (e.g. fast nearest-neighbors; Naive Bayes).
- The uncertainty of a guess can be determines in different ways, depending on the learner:
    - Within [NaiveBayes](img/boundary.png), the most uncertain guess is the one that with nearly equal probabilities of being in multiple classes. 
    - Within [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression#/media/File:Exam_pass_logistic_curve.jpeg), the most uncertain guess is the one closest to 0.5.
    - Within [Support Vector Machines](https://quantdare.com/wp-content/uploads/2016/09/svm2.png), the most uncertain row is the one that falls mid-way between the support vectors
    - In an [ensemble learning](https://miro.medium.com/max/590/1*DUaQoSKHX09hLG0QcGApTg.png), an uncertain guess is the one made by the smallest majoirity. For example consider an ensemble of
      built from (say) ten 90% samples of the current data. That ensemble offers a label when 6,7,8,9 or 10 ensemble members vote the same way.
      In that case, the most uncertain guess would be from a majoroty of only 6.
    - [Gaussian process models](https://miro.medium.com/max/700/1*PF8XTtgVm1UYTuRc3U2ePQ.jpeg) offer a mean and standard deviation for each prediction.


