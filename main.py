import argparse
import sys



def main(text, decode):
    print("do something")

def str2bool(value):
    if value.lower() in ('true', '1'):
        return True
    elif value.lower() in ('false', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError(f"Invalid boolean value: {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Probetag Tool")
    parser.add_argument("text", type=str, help="Der Text, der decodiert bzw. encodiert werden soll")
    parser.add_argument("decode", type=str2bool, help="Ein boolescher Wert (true/false)")

    if len(sys.argv) < 3:
        print("Fehler: Bitte gebe sowohl einen Text der decodiert bzw. encodiert werden soll, als auch einen booleschen Wert an.")
        print("Beispiel: python main.py \"abcd\" true")
        print("Beispiel: python main.py \"fhjl\" false")
        sys.exit(1)
    
    args = parser.parse_args()
    
    main(args.text, args.decode)
