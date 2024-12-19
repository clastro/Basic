import argparse

def main():
    parser = argparse.ArgumentParser(description="Sample program with reduced arguments.")

    parser.add_argument('--input', type=str, help='Input file path', required=True)
    parser.add_argument('--output', type=str, help='Output file path', required=True)
    
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')
    
    parser.add_argument('--config', type=str, help='Path to configuration file')
    args = parser.parse_args()

    if args.verbose:
        print(f"Running in verbose mode...")

    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
    
    if args.config:
        print(f"Using config file: {args.config}")

if __name__ == "__main__":
    main()
