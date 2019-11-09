#### Extract Body

The main idea of the algorithm is to use  the color depth image to find regions,
I iterate over these, and check if there is one that has a minimun area to be considered as
a body and check if this one has 'heat' inside, checking the red pixels in each RGB, if those conditions are
accomplished is probable that we have a body.

##### Difficulties
 - find the proper values to do the segmentation stage, if this stage fails the whole result will be affected
 - It is possible that fails if we have a big element that generates heat, since it will be accomplished the two conditions 'area and heat'

##### Complexity
Give an Image I(x,y) of dimensions N, M
 - memory: O(K*N*M) K number of copies
 - time: the method who is more expensive in time is extract.selectValidBodies, then I will just describe the complexity for this method
  O(len(contours) * K * N * M)

##### Results
<img src="assets/result/result.png"/>

##### Future work?
 - check the shape, and if this shape has some features that describe a human body.
 - It is slow, I propose think in other approach  or migrated to c++
 - there is some code that could be code in parallel, that will improve the performance

##### References
 - Documentation OpenCV


Thanks for reading my code :v
