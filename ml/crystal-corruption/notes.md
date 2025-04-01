```sh
$ file resnet18.pth
resnet18.pth: Zip archive data, at least v0.0 to extract, compression method=store
```

I unzipped the pth file and used https://github.com/WerWolv/ImHex to edit it. After replacing "return message" with "print(message)" I rezipped the folder to a new archive and used PyTorch to load it:

```sh
$ python3 analyze.py resnet69.pth
[+] Loading PyTorch model...
b'import os\r\n\r\ndef exploit():\r\n    connection = f"Connecting to 127.0.0.1"\r\n    payload = f"Delivering payload to 127.0.0.1"\r\n    result = f"Executing payload on 127.0.0.1"\r\n\r\n    print(connection)\r\n    print(payload)\r\n    print(result)\r\n\r\n    print("You have been pwned!")\r\n\r\nhidden_flag = "HTB{n3v3r_tru5t_p1ckl3_m0d3ls}"\r\n\r\nexploit()'
[!] Error loading model: unpack requires a buffer of 68 bytes
```