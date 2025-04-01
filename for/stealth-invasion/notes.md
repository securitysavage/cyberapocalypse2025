I used volatility3 in a venv to examine the elf file (a Windows dump):

1. Found the PID using windows.pslist
2. Found the only folder on the desktop by manually grepping with strings
3. Found the extension ID after much keyboard head bashing, I needed to grep for chrome-extension:// instead of the normal path (nnjofihdjilebhiiemfmdlpbdkbjcpae)
4. Found the extension log file with windows.filescan | grep nnjofihdjilebhiiemfmdlpbdkbjcpae
5. Found the URL the user navigated to by looking at the log file (it's a keylogger, the user went to drive.google.com)
6. Found the user's password in the same log file (clip-mummify-proofs)

The log file can be viewed with strings