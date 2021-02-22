import shutil
entire, worn, available = shutil.disk_usage("/")
print ("Entire: %d GiB " % (entire // (2**30)))
print ("Worn: %d GiB " %  (worn // (2**30)))
print ("Available: %d GiB " %(available //   (2**30)))