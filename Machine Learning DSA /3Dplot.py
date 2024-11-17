import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the points
points = {    
    'cat': [1, 0, 0], 
    'dog': [0.5, 1, 0.5], 
    'mouse': [0, 0.5, 1]
}
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')


for word, coords in points.items():
    ax.scatter(coords[0], coords[1], coords[2], label = word)

    
ax.set_xlabel("Cat")
ax.set_ylabel("Dog")
ax.set_zlabel("Mouse")

plt.legend()
plt.title("3D Plot")
plt.show()
