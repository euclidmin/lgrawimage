import io

# byte type

empty_bytes = bytes(4)
print(type(empty_bytes))
print(empty_bytes)

# bytearray
mutable_bytes = bytearray(b'\x00\x0F')
mutable_bytes[0] = 255
mutable_bytes.append(255)
print(mutable_bytes)

binary_stream = io.BytesIO()
binary_stream.write("Hello, world!\n".encode('ascii'))
binary_stream.write("Hello, world!\n".encode('utf-8'))

binary_stream.seek(0)
stream_data = binary_stream.read()

print(type(stream_data))
print(stream_data)

mutable_buffer = binary_stream.getbuffer()
print(type(mutable_buffer))
mutable_buffer[0] = 0xff
print(binary_stream.read())

with open("text.txt", "wb") as binary_file:
    binary_file.write("write text by encoding\n".encode('utf8'))
    num_bytes_written = binary_file.write(b'\xDE\xAD\xBE\xEF')
    print("wrote %d bytes" % num_bytes_written)

binary_file = open("text.txt", 'wb')
binary_file.write(b'\x00')
binary_file.close()

# with open("test_file.dat", "rb") as binary_file:
#     # Read the whole file at once
#     data = binary_file.read()
#     print(data)
import os

file_length_in_bytes = os.path.getsize("text.txt")
print(file_length_in_bytes)

# Seek can be called one of two ways:
#   x.seek(offset)
#   x.seek(offset, starting_point)

# starting_point can be 0, 1, or 2
# 0 - Default. Offset relative to beginning of file
# 1 - Start from the current position in the file
# 2 - Start from the end of a file (will require a negative offset)

# with open("test_file.dat", "rb") as binary_file:
#     # Seek a specific position in the file and read N bytes
#     binary_file.seek(0, 0)  # Go to beginning of the file
#     couple_bytes = binary_file.read(2)
#     print(couple_bytes)

i = 16
single_byte = i.to_bytes(1, byteorder='big', signed=True)
print(single_byte)

four_bytes = i.to_bytes(4, byteorder='big', signed=True)
print(four_bytes)
four_bytes_little = i.to_bytes(4, byteorder='little', signed=True)
print(four_bytes_little)

bytes_from_list = bytes([255, 255, 253, 252 ])
print(bytes_from_list)

import struct
binary_data = struct.pack("icc", 8499000, b'A', b'Z')
print(binary_data)

import sys
print("native byteorder: ", sys.byteorder)

# read_boot_sector.py - Inspect the first 512 bytes of a file

#
# in_file = open(sys.argv[1], 'rb')  # Provide a path to disk or ISO image
# chunk_size = 512
# data = in_file.read(chunk_size)
# print(data)

# extract_pngs.py
# Extract PNGs from a file and put them in a pngs/ directory
# import sys
#
# with open(sys.argv[1], "rb") as binary_file:
#     binary_file.seek(0, 2)  # Seek the end
#     num_bytes = binary_file.tell()  # Get the file size
#
#     count = 0
#     for i in range(num_bytes):
#         binary_file.seek(i)
#         eight_bytes = binary_file.read(8)
#         if eight_bytes == b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a":  # PNG signature
#             count += 1
#             print("Found PNG Signature #" + str(count) + " at " + str(i))
#
#             # Next four bytes after signature is the IHDR with the length
#             png_size_bytes = binary_file.read(4)
#             png_size = int.from_bytes(png_size_bytes, byteorder='little', signed=False)
#
#             # Go back to beginning of image file and extract full thing
#             binary_file.seek(i)
#             # Read the size of image plus the signature
#             png_data = binary_file.read(png_size + 8)
#             with open("pngs/" + str(i) + ".png", "wb") as outfile:
#                 outfile.write(png_data)


