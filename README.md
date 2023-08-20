# TestFuncitons
 Multiple Helper Functions for Rigging Use



**TODO**
    Split code into Modules


**First shelf Install **

```python
import RiggingHelperTillsToolkit
import importlib
importlib.reload(RiggingHelperTillsToolkit)
from RiggingHelperTillsToolkit import shelf_base
importlib.reload(shelf_base)
test = shelf_base.customShelf()
```


**userSetup.py - entry**

```python
import maya.cmds as mc
import maya.utils

import RiggingHelperTillsToolkit.shelf_base as shelf
mc.evalDeferred("shelf.customShelf()")
```
