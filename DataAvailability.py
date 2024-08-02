class Disk:
def __init__(self, name):
self.name = name
self.data = {}
def write_data(self, block_number, data):
self.data[block_number] = data
def read_data(self, block_number):
return self.data.get(block_number, None)
def is_available(self, block_number):
return block_number in self.data
class DiskArray:
def __init__(self, num_disks):
self.disks = [Disk(f"Disk_{i}") for i in range(num_disks)]
self.num_disks = num_disks
def write_data(self, block_number, data):
if len(data) != self.num_disks:
raise ValueError("Data length must match the number of disks")
for i in range(self.num_disks):
self.disks[i].write_data(block_number, data[i])
def read_data(self, block_number):
data = []
for i in range(self.num_disks):
data.append(self.disks[i].read_data(block_number))
Ex.No:09
Write the code for ensuring data availability indisks usingstripbased method. Date:
return data
def is_available(self, block_number):
for disk in self.disks:
if disk.is_available(block_number):
return True
return False
# Example usage:
disk_array = DiskArray(3) # Creating a disk array with 3 disks
# Writing data to disk array
data_to_write = ["Data1", "Data2", "Data3"]
disk_array.write_data(0, data_to_write)
# Checking availability of block 0
print("Block 0 availability:", disk_array.is_available(0)) # Output: Block 0 availability: True
# Reading data from disk array
read_data = disk_array.read_data(0)
print(read_data) # Output: ['Data1', 'Data2', 'Data3']

output:
Block 8 Availability : True
['Data 1', 'Data 2', 'Data 3']
