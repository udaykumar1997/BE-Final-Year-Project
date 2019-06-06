for file in *.png ; do
	python3 ./.segmentation_2.py --input $file
#	python3 ./.segmentation_1.py --input $file
done
