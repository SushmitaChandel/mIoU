# mIoU
mean intersection over union for one class

Steps to use the package:

1. Add ground truth files in the folder "ground_truth/". 
2. Add segmentation files in the folder "segmentations/".
3. Update base_path in base_paths.py file and point to the current directory.
4. RUN demo.py file.

Notes: "indexes" in demo are according to lexicographical naming of the the images. 

For example, image 1 has name "1.jpg", image 2 has name "2.jpg",..., image 10 has name "10.jpg", then (image_name,index) pairs are as follows:
(1.jpg,0)
(10.jpg,1)
(2.jpg,2)
(3.jpg,3)
(4.jpg,4)
(5.jpg,5)
(6.jpg,6)
(7.jpg,7)
(8.jpg,8)
(9.jpg,9)

To use all 40 images indexes = [0,1,2,....,39]
