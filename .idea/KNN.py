#KNN using TensorFlow library
from __future__ import print_function

import numpy as np
import tensorflow as tf

#Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
print ("loading data")
mnist=input_data.read_data_sets("/tmp/data/",one_hot=True)

print("finish!")

#In this example,we limit mnist data
Xtr,Ytr=mnist.train.next_batch(5000)
Xte,Yte=mnist.test.next_batch(200)

#tf Gragh Input
xtr=tf.placeholder("float",[None,784])
xte=tf.placeholder("float",[784])

#Nearest Neighbor calculation using L1 Distance
#Calculate L1 Distance
distance=tf.reduce_sum(tf.abs(tf.add(xtr,tf.neg(xte))),reduction_indices=1)

#Prediction:Get min distance index(Nearest neighbor)
pred = tf.arg_min(distance,0)

accuracy=0.

#Initializing the variables
init=tf.initialize_all_variables()

#Lauch the graph
with tf.Session() as sess:
    sess.run(init)

    #loop over test neighbor
    for i in range(len(Xte)):
        nn_index=sess.run(pred,feed_dict={xtr:Xtr,xte:Xte[i,:]})
        # Get nearest neighbor class label and compare it to its true label
        print("Test", i,"Prediction:",np.argmax(Ytr[nn_index]),"True Class:",np.argmax(Yte[i]))
        #Calculate accuracy
        if np.argmax(Ytr[nn_index])==np.argmax(Yte[i]):
            accuracy+=1./len(Xte)
    print("Done!")
    print("Accurcy:",accuracy)