import numpy as np
from sklearn.metrics import confusion_matrix
import os
from skimage import io
import pandas as pd

def parts(labels,gt):

	"""
	Returns tn, fp, fn, tp

	Parameters:
		labels : foreground-background output of technique
		gt : foreground-background ground truth

		Returns: (tn, fp, fn, tp)
		
	"""

	a = confusion_matrix(labels.ravel(), gt.ravel()).ravel()
	if a.shape == (1,):
		return (a[0],0,0,0)
	else:
		return (a[0],a[1],a[2],a[3])

def intersection_union(path_image_directory,image_ext,path_s_directory,s_ext,path_gt_directory,gt_ext,indexes):
	"""
	Finds mean intersection over union for images whose index is in indexes

	Parameters:
	path_image_directory : Path containing all the images
	path_s_directory :  Path containing segmentation label images
	path_gt_directory : Path containing ground truth segmenatation label images
	image_ext : valid image extension
	s_ext : valid segmentation extension
	gt_ext : valid ground truth extension
	indexes : list
		indexes denotes images to be used.
	"""
	inter = 0
	union = 0

	image_files = os.listdir(path_image_directory)
	image_files = sorted(image_files)
	for index in indexes:

		print(f'Processing image indexed at {index}')

		entry = image_files[index]
		entry_name,entry_extension = os.path.splitext(entry)

		if entry_extension != image_ext:
			continue

		path_s = path_s_directory+'Label_'+entry_name+s_ext
		path_gt = path_gt_directory+'Label_'+entry_name+gt_ext

		labels = io.imread(path_s)
		gt = io.imread(path_gt)

		if labels.shape != gt.shape:
			print("Incompatible size of labels and gt image")
			break

		p = parts(labels,gt)

		inter = inter+p[3]
		union = union+(p[1]+p[2]+p[3])

	return (inter,union)





