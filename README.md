# Colonnade

Colonnade is a Sublime Text 3 package that allows you to set a fixed number of columns in your view, *and make those columns divide your screen into 1/n **exactly***. It also makes it so that even if you temporarily move the boundaries, it will restore itself to the exact division boundaries.

For example, if you use colonnade to have 3 columns, the columns will be *always* 1/3 of your available window. Even if you move the boundaries by dragging, when you switch to another column, they will snap back to their allocated 1/3 size.

This is different from Sublime's own ```Layout > Columns: 2 / 3 / 4``` because if you use those, not only the boundaries won't retain their exact divisions, it's also the fact that if you move the boundaries, they will stay where you move them to.

## Shortcuts

Colonnade comes with three shortcuts.

(```Super``` is a shorthand for ```Cmd``` on Mac OS, ```Alt``` on Windows, and ```Super``` on Linux.)

```Ctrl + Super + 2```: 2-column exact division layout, force retained
```Ctrl + Super + 3```: 3-column
```Ctrl + Super + 4```: 4-column

## Options

There are no options.

## Install

1) Open Sublime Text. Go to ```Preferences > Browse Packages```
2) Download this repository, and put the ```Colonnade``` folder into your Sublime Packages directory.

## Uninstall

1) Open Sublime Text. Go to ```Preferences > Browse Packages```
2) Delete ```Colonnade``` directory
3) Go to ```Preferences > Settings```. Look for the ```on_activated_async_project``` key in the JSON file. Delete the key and the array it contains. If you don't know how to edit JSON, ask a friend to do it for you, you might accidentally corrupt your settings file if you do it wrong.

## Author

Copyright © 2019-Current Burak Nehbit. All rights reserved.

## License

MIT