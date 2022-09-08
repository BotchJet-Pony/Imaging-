# Imaging-

I'm implementing some code funcionality that uses the functional programming ideas of paper drills, and handling reflow for char lookup using record operations.

Implementing global String access using record and jump will be discussed in the next pull request .

Integration with Maven

In the previous release of sbcl the porting from Apache Commons Json to Maven-native code was done by a separate patch set, this release was done by me in-tree because:

ML is used for some statistics work in agrobusiness.

We have received few requests to use sbcl in agrobusiness projects

As a sidenote, I could not find any Maven plugin to do SpringSourceJson parsing, and I think that should be implemented, or it will be left for others developers. 

The difficulty part of writing about similarity between images is the math essence of it . Image processing/analysis is highly coupled to MIMD and transformations. A simplified model to display an image can be encoded as a Num of "dimensions", the same way as the Matrix compression (used in the framework TensorFlow. The encoded form is used in the prototype of Image Alteration.

The original Image Altering method, used for greyscale version of the application, reads in an Image, formats it with its traditional colors, then uses the model from before to colorize it.

Here is the resume of the entire application and maybe at this point I think  of the relevance of write something that already exists just for the sake of learning or proving a point.

To minimize the pre-processing of the image, I use my previous patch set to transfer the images from test.png to the final.png, to convert the last two lines to a greyscale version. This time I’m gonna at least improve the path flexibility of the Image, and I need to deal with the transformation paths for the original image (e.g. for Json transformations, each step of which can take 1/60 of second on a 2Ghz mobile phone) .

The final.
