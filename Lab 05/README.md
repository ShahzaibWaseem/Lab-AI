# Lab 05: Offline Signature Verification (Feature Extration)

## Tasks
In this lab, you will modify your own implementations of last lab to perform the following tasks. Additions to the previous lab are highlighted.

1. Develop a bounding box around the signature content.
2. Find out the centroid of the signature.
3. Segment signature from centroid vertically and horizontally (the signature will be divided into four pieces)
4. **Repeat steps 2-3 until you have segmented the image into 64 cells.**
5. Calculate black to white transitions for each of the 64 cells.
6. **Calculate aspect ratio of each cell.**