# Lab 09: k-NN Classifier

## Task

Choose one signature image form "TestSet/Questioned/" directory:

1. Run the algorithm developed previously to extract the seven features (see Features Extracted) from the questioned signature.
2. You will get 7 vectors of 64 elements each. Write these to text file(s).
3. Read the 64-element vector of one feature for one of the reference signatures. (It should already have been written to files in previous lab).
4. In a loop, perform one-to-one comparison between feature value of questioned signature and reference signature by calculating Euclidean distance. Store distances in a vector, _D_.
5. Repeat 3 - 4 for all seven features.
6. Store final output in a text file.

### Features Extracted

For each of the 64 cells in a signature image, these 7 features:

1. Coordinates of centroid, C = (cx, cy)
2. Black to white transitions, T
3. Aspect ratio, R = cell-width / cell-height of cell
4. Number of black pixels
5. Normalized size
6. Angle of inclination of centroid
7. Normalized sum of angles of inclinations of black pixels

For each of the 25 images in "TestSet/Reference/" directory, you should have extracted vectors of 64 elements for each of the features.

- That is, 7 vectors, each of size 64, per reference signature
- These vectors should be dumped in text files
