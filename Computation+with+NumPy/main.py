import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import  Image


#create new ndarray from scatch
my_array = np.array([1.1, 9.2, 8.1, 4.7])

#show rows and columns
my_array.shape

#accessing elements by index
print(my_array[2])

#show dimensions of an array
my_array.ndim

my_array1 = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])
print(f'array_2d has {my_array1.ndim} dimensions')
print(f'Its shape is {my_array1.shape}')
print(f'It has {my_array1.shape[0]} rows and {my_array1.shape[1]} columns')
print(my_array1)

print(my_array1[1, 2])
print(my_array1[0, :])

print('Benjamin')
#the aswers below
mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])
#How many dimensions does the array below have?
print(mystery_array.ndim)
print(f'We have {mystery_array.ndim} dimensions')

#What is its shape (i.e., how many elements are along each axis)?
print(mystery_array.shape)
print(f'The shape is {mystery_array.shape}')

#Try to access the value 18 in the last line of code.
print(mystery_array[2, 1][-1:])
#or
print(mystery_array[2, 1, 3])

#Try to retrieve a 1-dimensional vector with the values [97, 0, 27, 18]
print(mystery_array[2, 1])
#or
print(mystery_array[2, 1, :])

#Try to retrieve a (3,2) matrix with the values [[ 0, 4], [ 7, 5], [ 5, 97]]
print(mystery_array[:, :, 0])

#Use .arange()to createa a vector a with values ranging from 10 to 29
a = np.arange(10, 30)
print(a)
#Create an array containing only the last 3 values of a
print(a[-3:])
#Reverse the order of the values in a, so that the first element comes last
print(np.flip(a))

#Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]
b = np.array([6,0,9,0,0,5,0])
nz_indices = np.nonzero(b)
print(nz_indices)

#Use NumPy to generate a 3x3x3 array with random numbers
x = np.random.random((3, 3, 3))
print(x)

#Use .linspace() to create a vector x of size 9 with values spaced out evenly between 0 to 100 (both included
y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()

#Use NumPy to generate an array called noise with shape 128x128x3 that has random values.
# Then use Matplotlib's .imshow() to display the array as an image.
# The random values will be interpreted as the RGB colours for each pixel.
noise = np.random.random((128, 128, 3))
print(noise.shape)
plt.imshow(noise)

#Let's multiply a1 with b1. Looking at the Wikipedia example above,
# work out the values for c12 and c33 on paper.
# Then use the .matmul() function or the @ operator to check your work

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

a1_b1 = np.matmul(a1, b1)
print(a1_b1)

#image
img = misc.face()
plt.imshow(img)
type(img)
img.shape
img.ndim