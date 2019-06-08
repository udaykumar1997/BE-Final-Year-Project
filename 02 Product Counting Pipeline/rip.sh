for file in *.png ; do
	python3.5 ./.segmentation_2.py --input $file
#	python3.5 ./.segmentation_1.py --input $file
done
