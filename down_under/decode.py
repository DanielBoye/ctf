from ethereum_input_decoder import get_fn_sig
import sys

if len(sys.argv) != 2:
    print("Usage: python decode_signature.py <function_signature>")
    sys.exit(1)

function_signature = sys.argv[1]

decoded_function = get_fn_sig(function_signature)
print(decoded_function)
