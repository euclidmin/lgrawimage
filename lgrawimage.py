
lgrawimg_ascii = bytearray("LGRAWIMG".encode('ascii'))

# print(type(lgrawimg_ascii))
# print(lgrawimg_ascii)

partition_count = 4
partition_count_byte = partition_count.to_bytes(1, byteorder='little', signed=True)
print(partition_count_byte)

dummy_3bytes = b'\x00\x00\x00'
dummy_8bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'
dummy_368bytes = dummy_8bytes * 46 # 8 X 46 = 368bytes
boot_area_use = 1
boot_area_use_byte = boot_area_use.to_bytes(1, byteorder='little', signed=True)

# imx-boot
imxboot_start_offset = 512
imxboot_start_offset_byte = imxboot_start_offset.to_bytes(8, byteorder='little', signed=True)
imxboot_size = 0x800000
imxboot_size_byte = imxboot_size.to_bytes(8, byteorder='little', signed=True)
imxboot_material_start_offset = 0x00
imxboot_material_start_offset_byte = imxboot_material_start_offset.to_bytes(8, byteorder='little', signed=True)

# kernel
partition1_start_offset = 0x800200
partition1_start_offset_byte = partition1_start_offset.to_bytes(8, byteorder='little', signed=True)
partition1_size = 0x04000000
partition1_size_byte = partition1_size.to_bytes(8, byteorder='little', signed=True)
partition1_material_start_offset = 0x800000
partition1_material_start_offset_byte = partition1_material_start_offset.to_bytes(8, byteorder='little', signed=True)

# rootfs
partition2_start_offset = 0x4800200
partition2_start_offset_byte = partition2_start_offset.to_bytes(8, byteorder='little', signed=True)
partition2_size = 0x7F000000
partition2_size_byte = partition2_size.to_bytes(8, byteorder='little', signed=True)
partition2_material_start_offset = 0x4800000
partition2_material_start_offset_byte = partition2_material_start_offset.to_bytes(8, byteorder='little', signed=True)

# backup
partition3_start_offset = 0x83800200
partition3_start_offset_byte = partition3_start_offset.to_bytes(8, byteorder='little', signed=True)
partition3_size = 0x40000000
partition3_size_byte = partition3_size.to_bytes(8, byteorder='little', signed=True)
partition3_material_start_offset = 0x83800000
partition3_material_start_offset_byte = partition3_material_start_offset.to_bytes(8, byteorder='little', signed=True)


lgimg_file = open("lgimg.bin", 'wb')

lgimg_file.write(lgrawimg_ascii)
lgimg_file.write(partition_count_byte)
lgimg_file.write(dummy_3bytes)
lgimg_file.write(boot_area_use_byte)
lgimg_file.write(dummy_3bytes)

lgimg_file.write(imxboot_start_offset_byte)
lgimg_file.write(imxboot_size_byte)
lgimg_file.write(imxboot_material_start_offset_byte)
lgimg_file.write(dummy_8bytes)

lgimg_file.write(partition1_start_offset_byte)
lgimg_file.write(partition1_size_byte)
lgimg_file.write(partition1_material_start_offset_byte)
lgimg_file.write(dummy_8bytes)

lgimg_file.write(partition2_start_offset_byte)
lgimg_file.write(partition2_size_byte)
lgimg_file.write(partition2_material_start_offset_byte)
lgimg_file.write(dummy_8bytes)

lgimg_file.write(partition3_start_offset_byte)
lgimg_file.write(partition3_size_byte)
lgimg_file.write(partition3_material_start_offset_byte)
lgimg_file.write(dummy_8bytes)
lgimg_file.write(dummy_368bytes)

# with open("D:\Ergo\imx-image-ergo-imx8mp-lpddr4-evk-v0.1.9-07181421.wic\imx-image-ergo-imx8mp-lpddr4-evk-v0.1.9-07181421.wic", "rb") as binary_file:
with open("/home/systemsw/work1/imx-yocto-ergo/build-ergo/tmp/deploy/images/imx8mp-lpddr4-evk/data", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    lgimg_file.write(data)
    binary_file.close()

lgimg_file.close()
