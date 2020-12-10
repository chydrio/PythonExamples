Setup:
  Write a function that returns a similarity measure, for 2 images
  images are represented by [123, 345, 346236] where eacdh number is something in the image
  123 = red
  345 = balloon
  [123, 438], 123= red. 438=child
 Continuing:
   Given a set of images, return a highly representative image (index into it).
  Input list of images, each image is a list of object tokens


  [123, 345, 346236] idx0 ->12
  [123, 345, 1] idx1 ->12
  [123, 2, 346236] ->
  [123, 345, 3]
  [123, 345, 2]
  [121, 345, 1]

  123,5
  345, 5
  2, 2
  346236,2
  3,1



  123,345,2


  def representativeImage(array):

    if len(array)==0:
      return -1


    dictionnary=dict()
    for subarray in array:
      for i in subarray:
        dictionnary[i]=  dictionnary.get(i,0)+1


        nXM


    dictionnary.sorted()
    length=len(array[0])
    idx_measure=0
    measure_max=0
    idx=0
    for subarray in array:
      measure=0 #
      for i in subarray:
        measure+=dictionnary.get(i,0)


      if measure >measure_max:
        measure_max=measure
        idx_measure=i

  return idx_measure

  from collections import Counter

  def mesure(array1, array2):
    count1=Counter(array1)
    count2=Counter(array2)

    result=0
    for token in count1.keys():
      if token in count2:
        result+=1

    return

  #bigger is similar


  O(N) with N length of my array (both arrays have the same length)



2nd interview
  median of 2 sorted arrays
