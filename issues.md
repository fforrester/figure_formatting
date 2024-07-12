Issues often arise with how matplotlib deals with fonts:

# Delete any previously cached matplotlib entries:
These can be found here:
```
import matplotlib as mpl; print(mpl.get_cachedir())
```
# Ensure font is accessible in ttf form:
```
import matplotlib ; matplotlib.matplotlib_fname()
```
