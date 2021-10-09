import tensorflow as tf
import keras
tf.compat.v1.reset_default_graph()

with tf.compat.v1.Session() as sess:
	x = tf.constant(1.8)
	y = tf.constant(3.6)
	a = tf.round(x, name='Round')
	b = tf.floor(y, name='Floor')
	c = tf.add(a, b, name='Add')
	d = tf.multiply(a, c, name='Multiply')
	e = tf.abs(c, name='Abs')
	f = tf.add(d, e, name='Addition')
	writer = tf.summary.create_file_writer('./graphs')
	print(sess.run(f))
