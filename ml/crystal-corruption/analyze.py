import torch
import argparse

def main(file_path):
    print("[+] Loading PyTorch model...")
    try:
        model_data = torch.load(file_path, map_location="cpu", weights_only=False)
        print("[+] Model loaded successfully.")
    except Exception as e:
        print(f"[!] Error loading model: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load a PyTorch .pth file to execute any hidden payloads.")
    parser.add_argument("file", help="Path to the .pth file")
    args = parser.parse_args()
    main(args.file)