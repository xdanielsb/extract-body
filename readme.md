#### Extract Body

The main idea of the algorithm is using the color depth image to find regions,
throw these regions I find a region that has a minimun area to be considered as
a body and find if this area has a region of 'heat', if those conditions are
acommplish is probable that we have a body.


##### Difficulties
 - find the proper values to do the segmentation stage, if this stage fails the whole result will be affected

##### Complexity
Give an Image I(x,y) of dimensions N, M
 - memory: O(K*N*M) K number of copies
 - time: the method who is more expensive in time is extract.selectValidBodies, then I will just show the complexity for this method
  O(len(contours) * K * N * M) amortized

##### References
 - Documentation OpenCV


Thanks for reading my code :v 
