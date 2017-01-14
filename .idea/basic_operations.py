import tensorflow as tf

#Basic constant operations
#the value returned by the constructor represents the output
#of the Constant op.
a=tf.constant(2)
b=tf.constant(3)

#Launch the default gragh
with tf.Session() as sess:
    print "a=2.b=3"
    print "Addition with constants :%i" % sess.run(a+b)
    print "Multiplication with constants:%i" % sess.run(a*b)

#Basic Operations with variable as gragh input
#The value returned by constructor represents the output
#of the Variable op.(define as input when running session)
#tf Gragh input
a=tf.placeholder(tf.int16)
b=tf.placeholder(tf.int16)

#Define some operations
add=tf.add(a,b)
mul=tf.mul(a,b)

#Launch the default gragh.
with tf.Session() as sess:
    print "Addition with variables: %i" % sess.run(add,feed_dict={a:2,b:3})
    print "Multiplication with variables: %i" % sess.run(mul,feed_dict={a:2,b:3})

#----------------------More in details--------------------
#Matrix Multiplication from TensorFlow official tutorial
#creat a Constant op that produces a 1*2 matrix. The op is
#added as a node to default gragh.
#The value returned by the constructor represents the output
#of the Constant op.
matrix1=tf.constant([[3.,3.]])
matrix2=tf.constant([[2.],[2.]])
#create a Matmul op that takes 1 and 2 ad inputs
#the returned value,'Product',represents the result of the matrix
#multiplication
product=tf.matmul(matrix1,matrix2)

with tf.Session() as sess:
    result=sess.run(product)
    print result


