import cv2
import matplotlib.pyplot as plt

class operation():
    def __init__(self, image_path, kernel,output_path = None):
        self.image_path = image_path
        self.kernel = kernel
        self.original_image = cv2.imread(self.image_path)
        self.output_path = output_path
    def filter2D(self):
        '''
        Implement the convolution operator
        '''
        self.filter_image = cv2.filter2D(self.original_image, -1, self.kernel)
        return self.filter_image
    def show(self):
        """
        Show the image
        """
        self.filter_image = cv2.cvtColor(self.filter_image, cv2.COLOR_BGR2RGB)
        plt.imshow(self.filter_image)
    def save(self):
        '''
        Save the image
        '''
        if self.output_path != None:
            plt.axis("off")
            plt.savefig(self.output_path)