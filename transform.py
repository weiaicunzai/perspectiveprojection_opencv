#import os
#import pickle
#import numpy as np
from torchvision.transforms import transforms




def simclr_transforms(img_size):
    # In this work, we sequentially apply three simple augmentations:
    # random cropping followed by resize back to the original size
    # random color distortions
    # random Gaussian blur


    # the augmentation policy used to train our models only includes 
    # random crop (with flip and resize), 
    # color distortion, 
    # and Gaussian blur. 
    

    s = 2
    size = img_size
    color_jitter = transforms.ColorJitter(0.8 * s, 0.8 * s, 0.8 * s, 0.2 * s)
    data_transforms = transforms.Compose([transforms.RandomResizedCrop(size=size),
                                              transforms.RandomHorizontalFlip(),
                                              transforms.RandomApply([color_jitter], p=0.8),
                                              transforms.GaussianBlur(kernel_size=int(0.1 * size)),
                                              transforms.ToTensor()])
    return data_transforms
    # print('ff')



#def cifar100_train(data_dir):
#
#    with open(os.path.join(data_dir, 'train'), 'rb') as cifar100_train:
#        data = pickle.load(cifar100_train, encoding='bytes')
#    
#    images = data['data'.encode()]
#    labels = data['fine_labels'.encode()]
#    images = np.reshape(images, (-1, 3, 32, 32))
#    images = np.transpose(images, (0, 2, 3, 1))
#    
#    return images, labels
#
#def cifar100_test(data_dir):
#    with open(os.path.join(data_dir, 'test'), 'rb') as cifar100_test:
#        data = pickle.load(cifar100_test, encoding='bytes')
#
#    images = data['data'.encode()]
#    labels = data['fine_labels'.encode()] 
#    images = np.reshape(images, (-1, 3, 32, 32))
#    images = np.transpose(images, (0, 2, 3, 1))
#
#    return images, labels

