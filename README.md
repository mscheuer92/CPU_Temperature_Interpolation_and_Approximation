## Calculating the Piecewise Linear Interpolation of CPU Temperatures
#### Michelle Scheuer
#### 11/15/2021

The data supplied to this program can be found in the text files located in `files/input_files`. It is the form of temperatures.
Each column in the files represents a temperature reading from 4 processor cores.

The output files are written in the following form:
    
*x<sub>k</sub> &nbsp; < = x &nbsp;<&nbsp; x<sub>k+1</sub>&nbsp;; &nbsp;y<sub>i</sub>&nbsp;=&nbsp;c<sub>0</sub>&nbsp;+&nbsp;c<sub>1</sub>x ; type*

* *x<sub>k</sub>* and *x<sub>k+1</sub>* are the domain that *y<sub>k</sub>* is applicable.
* *y<sub>k</sub>* is the *k<sup>th<sup>* function.
* The type is interpolation.


To run this program:

* `python3 main.py input_files/<filename>`

Each core will be saved as:
* {filename}- core # -.{txt}