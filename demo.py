import IU

import base_paths

def main():

	iou_threshold = 0.5
	path_image_directory = base_paths.base_path+'data/'
	path_s_directory = base_paths.base_path+'segmentations/'
	path_gt_directory = base_paths.base_path+'ground_truth/'
	image_ext = '.jpeg'
	s_ext = '.png'
	gt_ext = '.png'
	indexes = [0,1,2,3,4,5,6,7,8,9,11,12,15,16,17,22,23,24,27,29,32,33,35,38,39]
	iu = IU.intersection_union(path_image_directory,image_ext,path_s_directory,s_ext,path_gt_directory,gt_ext,indexes)
	print(f'mIoU is {iu[0]/iu[1]}')

if __name__ == '__main__':
	main()