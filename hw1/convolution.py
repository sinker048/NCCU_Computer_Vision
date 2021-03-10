from src.processing import operation
import argparse
import numpy as np
import os
from glob import glob

def get_opt():
    '''
    Getting the argument
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel_name")
    opt = parser.parse_args()
    return opt

def get_kernel(kernel_name):
    '''
    Arg:
        kernel_name: the kernel filter name
    Return:
        kernel: the kernel filter
    '''
    kernel_dict = {'sharp':([0,-1,0],[-1,5,-1],[0,-1,0]),
    'emboss':([-2,-1,0],[-1,1,1],[0,1,2]),
    'laplacian':([0,1,0],[1,-4,1],[0,1,0]),
    'outline':([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),
    'blur':([0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625])}

    kernel = np.array(kernel_dict[kernel_name],dtype='float32')

    return kernel

def main():
    '''
    The image processing
    '''
    opt = get_opt()
    image_path = glob('image/*jpg')
    for img_path in image_path:
        kernel = get_kernel(opt.kernel_name)
        output_path = 'output/' + img_path.split('\\')[-1]
        img = operation(img_path, kernel, output_path)
        img.filter2D()
        img.show()
        img.save()
if __name__ == '__main__':
    main()