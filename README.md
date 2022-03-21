README.md
------------------
McKenna L. Branting
-------------------
Included:
-------------------
this README, 
riemannSumSin.py file, 
riemannSumGraph.py file,
riemannSumStreaming.py file,
riemannSumCalc.py file,
output from executing python files [riemannSumSin.py, riemannSumGraph.py, riemannSumStreaming.py] (each output 3 graphs modeling left Riemann sum, right Riemann sum, and midpoint Riemann sum),
output from executing [riemannSumCalc.py] file (Riemann value)

-------------------
Packages 
------------------
Install packages for 
- numpy 
Using pip (sudo apt install python-pip) 
Install numpy (pip install numpy or pip3 install numpy (depending on version of Python))
Verify numpy installation (pip show numpy / pip3 show numpy)
(program code includes importing the package -- import numpy as np)
- scipy
Using pip install scipy (pip install scipy)
- matplotlib
Using pip (pip install matplotlib)
(program code includes importing the package -- import matplotlib.pyplot as plt)
- odeint
(program code imports the package using scipy from scipy.integrate import odeint)
Import module math to be able to run calculations
- import math 

------------------
Design Decisions & Project Issues
------------------
From the description in the documentation, the code was modeled based on this layout,
and the methodology shown in the handwritten work.
The equations and steps for understanding the algorithm used can be seen further explained in
the documentation.
Initial values were also provided and can be seen implemented throughout the code.

-------------------
Results 
-------------------
Running the code will result in:
- graphs modeling the various Riemann sums for 1a from running RiemannSumSin.py
- graph modeling the various Riemann sums for 1c.1 from running RiemannSumGraph.py
- graph modeling the various Riemann sums for 2 from running RiemannSumStreaming.py
- Riemann value for equation from running riemannSumCalc.py
