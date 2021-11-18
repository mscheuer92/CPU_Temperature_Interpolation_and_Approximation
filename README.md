## Calculating the Piecewise Linear Interpolation and Linear Approximation of CPU Temperatures
#### Michelle Scheuer
#### 11/15/2021


To run this program:

* `python3 main.py <filename>`

For convenience, I've included some files within the project:
*  For files with labels:
    * `python3 main.py files/sensors-2018.12.26.txt`

      
* For files without labels:
    * `python3 main.py files/sensors-2018.12.26-no-labels.txt`

    
Each core will be saved as:
* {filename}- core # -.{txt}


In `files/output_files` you will find 8 files. Four of which contain data from cores from a file without labels. The remaining 4 files contain
data from a file with labels.

The data supplied to this program can be found in the text files located in `files/input_files`. It is the form of temperatures.
Each column in the files represents a temperature reading from 4 processor cores.

The output files are written in the following form:
    
*x<sub>k</sub> &nbsp; < = x &nbsp;<&nbsp; x<sub>k+1</sub>&nbsp;; &nbsp;y<sub>i</sub>&nbsp;=&nbsp;c<sub>0</sub>&nbsp;+&nbsp;c<sub>1</sub>x ; type*

* *x<sub>k</sub>* and *x<sub>k+1</sub>* are the domain that *y<sub>k</sub>* is applicable.
* *y<sub>k</sub>* is the *k<sup>th<sup>* function.
* The type is interpolation and approximation.
