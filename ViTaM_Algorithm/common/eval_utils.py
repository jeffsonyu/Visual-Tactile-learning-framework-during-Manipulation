import torch
import numpy as np
import math
from scipy.spatial import distance


def compute_iou(occ1, occ2, threshold=0.5):
    ''' Computes the Intersection over Union (IoU) value for two sets of
    occupancy values.

    Args:
        occ1 (tensor): first set of occupancy values
        occ2 (tensor): second set of occupancy values
    '''
    occ1 = np.asarray(occ1)
    occ2 = np.asarray(occ2)

    # Put all data in second dimension
    # Also works for 1-dimensional data
    if occ1.ndim >= 2:
        occ1 = occ1.reshape(occ1.shape[0], -1)
    if occ2.ndim >= 2:
        occ2 = occ2.reshape(occ2.shape[0], -1)

    # Convert to boolean values
    # occ1 = (occ1 >= threshold)
    # occ2 = (occ2 >= threshold)
    
    threshold = np.mean(occ2)
    occ1 = (occ1 >= threshold)
    occ2 = (occ2 >= threshold)

    # Compute IOU
    area_union = (occ1 | occ2).astype(np.float32).sum(axis=-1)
    area_intersect = (occ1 & occ2).astype(np.float32).sum(axis=-1)

    iou = (area_intersect / area_union)

    return iou