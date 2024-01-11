import numpy as np
from matplotlib import pyplot as plt

def barnsley_fern_generator(repet_count):
    # Initialize the matrices and vectors to be applied to the point
    w_1 = np.array([[0.0, 0.0], [0.0, 0.16]], dtype='float')
    b_1 = np.array([0.0, 0.0], dtype='float')
    w_2 = np.array([[0.85, 0.04], [-0.04, 0.85]], dtype='float')
    b_2 = np.array([0.00, 1.60], dtype='float')  
    w_3 = np.array([[0.20, -0.26], [0.23, 0.22]], dtype='float')
    b_3 = np.array([0.00, 1.60], dtype='float') 
    w_4 = np.array([[0.15, 0.28], [-0.26, 0.24]], dtype='float')
    b_4 = np.array([0.00, 0.44], dtype='float') 

    # Stores all points in a list
    points = []

    # [x, y]
    current_point = np.random.random((2,)) 
    for _ in range(repet_count):
        p = np.random.random()

        # Implement the algorithm to get [x_new, y_new]
        if p <= 0.01:
            new_point = np.dot(w_1, current_point) + b_1
        elif p <= 0.86:
            new_point = np.dot(w_2, current_point) + b_2
        elif p <= 0.93:
            new_point = np.dot(w_3, current_point) + b_3
        else:
            new_point = np.dot(w_4, current_point) + b_4

        # Add [x_new, y_new] to the list
        points.append(new_point.flatten()) 

        # Set the current_point as [x_new, y_new]
        current_point = new_point

    # Save the points to a file
    np_points = np.array(points)
    np.savetxt(f'fern_data_{repet_count}.txt', np_points, fmt='%.18e', delimiter=' ')
    
def main():
    repet_count = 50000
    barnsley_fern_generator(repet_count)
    
    # Load the points from the file    
    fern_points = np.genfromtxt(f"fern_data_{repet_count}.txt")
    
    # Plot the points
    x = fern_points[:, 0]
    y = fern_points[:, 1]
    plt.scatter(x, y, s=0.5, c='green', edgecolor='none')
    plt.axis('off')  
    
    # Show the plot
    plt.show()
    
    # Save the plot as an image 
    plt.savefig('barnsley_fern_50000.png', transparent=True)


main()

