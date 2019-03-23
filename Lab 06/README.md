# Lab 06: Feature Extraction

## Tasks
Implement the Following. From the Paper: [**Samuel, D., & Samuel, I. (2010). Novel feature extraction technique for off-line signature verification system. _International Journal of Engineering Science and Technology_, _2_(7), 3137-3143.**](https://pdfs.semanticscholar.org/29b0/cc3e53bf14534e4939a078045ab7c0130d41.pdf)

1. Find the size of each of the 64 cells and normalize them with the number of the black pixels in the cells,
- Calculate the height and width of each cell and use this value to obtain the cell size.
- Count the number of black pixels in each cell.
- Divide cell size by the number of black pixels.
	The feature extracted constitutes the set of the first feature (F1).

2. Calculate the angle of inclination of each sub-image centre in each cell to lower right corner of the cell.
- Locate the centre of each of the 64 sub-image cells using equations below.
- Calculate the angle that each centre point makes with the lower right corner of the cell.
	The features extracted constitutes the set of the second feature (F2).

	x' = 1/N &Sum;<sup>N</sup><sub>i=1</sub> x(i)

	y' = 1/N &Sum;<sup>N</sup><sub>j=1</sub> y(j)