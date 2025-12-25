# CocoaGUI trial  

Template project to test out CocoaGUI's, well, gui system.
Labeled by the kind of app it is, eg. Calculator.py
Requires installing CocoaGUI such as with `dependencies.sh`  

## Files  

1. `size_monitor.py`  
    * Essentially a RAM usage monitoring script. Called before and after window starts, updates every 5 seconds.  
    * Uses pympler's `asizeof` utility to check each object in the passed `objects: list[object]`  
2. `calculator.py`  
    * A simple calculator  
3. `logs/*.usage.log`  
    * Logs from RAM usage tests, files are named by `{script_name - '.py'}.usage.log`  
