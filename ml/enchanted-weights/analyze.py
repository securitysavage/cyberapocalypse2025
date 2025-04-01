#!/usr/bin/env python3

import torch
import argparse

def analyze_pth(file_path):
    print(f"Analyzing {file_path}...")
    
    try:
        # Load the PyTorch .pth file
        data = torch.load(file_path, map_location="cpu")
        
        if isinstance(data, dict) and "hidden.weight" in data:
            print("\n[+] Extracting Hidden Weight Values...")
            
            # Convert tensor to a NumPy array and flatten it to a 1D list
            tensor_values = data["hidden.weight"].numpy().flatten()
            
            # Convert numeric values to ASCII characters if they fall in the printable range
            flag_string = "".join(chr(int(n)) for n in tensor_values if 32 <= n <= 126)
            print("\n[+] Decoded Hidden Weight as Text:")
            print(flag_string)
        else:
            print("\n[!] 'hidden.weight' tensor not found in model.")
    except Exception as e:
        print("\n[!] Error loading PyTorch model:", e)

if __name__ == "__main__":
    # Parse command-line arguments for the .pth file path
    parser = argparse.ArgumentParser(description="Extract hidden weight values from a PyTorch .pth file.")
    parser.add_argument("file", help="Path to the .pth file")
    args = parser.parse_args()
    analyze_pth(args.file)