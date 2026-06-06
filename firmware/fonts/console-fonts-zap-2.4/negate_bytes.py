import os
import sys

def negate_bytes_in_file(input_filename, output_filename):
    """
    Reads a binary file, negates (bitwise NOT) all bytes,
    and writes the result to a new file.
    
    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write the negated bytes to.
    """
    try:
        # 1. Read the binary data from the input file
        with open(input_filename, 'rb') as f:
            # Read all bytes and convert to a mutable bytearray
            data = bytearray(f.read())
            
        # 2. Negate each byte using a list comprehension with bitwise XOR
        # The expression `b ^ 0xFF` performs a bitwise NOT operation on each byte
        # ensuring the result stays within the 0-255 range
        negated_data = bytearray([b ^ 0xFF for b in data])

        # 3. Write the negated data to the output file
        with open(output_filename, 'wb') as f:
            f.write(negated_data)
            
        print(f"Successfully negated bytes from '{input_filename}' and saved to '{output_filename}'.")
        print(f"Original size: {len(data)} bytes, New size: {len(negated_data)} bytes.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
if __name__ == "__main__":

    infile = sys.argv[1]
    print(f'Input file is {infile}')
    outfile = sys.argv[2]
    print(f'Output file is {outfile}')
    negate_bytes_in_file(infile, outfile)



