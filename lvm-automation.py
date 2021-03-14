import os
print("\n\n\n\t-----------------------------------------------------------------------------------------")
print("\t\t\t\t W E L C O M E   T O   T H E   P R O J E C T ")
print("\t-----------------------------------------------------------------------------------------\n\n")

while True:
      print("""
	Press 1: List the Disk Information
	Press 2: Create a Physical Volume 
	Press 3: List Physical Volumes
	Press 4: Create a Volume Group
	Press 5: List Volume Groups
	Press 6: Create a Logical Volume
	Press 7: List Logical Volumes
        Press 8: Format the disk
        Press 9: Mount the Volume
        Press 10: Unmount the Volume 
	Press 11: to exit
	""")

      print("Enter your choice: ", end=" ")

      ch=input()
      if int(ch) == 1:
          os.system("fdisk -l")
      elif int(ch) == 2:
          disk_name = input("Enter the Disk name: ")
          os.system("pvcreate {} ".format(disk_name))
      elif int(ch) == 3:
          os.system("pvdisplay")
      elif int(ch) == 4:
          group_name = input("Enter the Volume Group name: ")
          disks = input("Please enter all the DiskNames (seperate with a space): ")
          os.system("vgcreate {} {}".format(group_name, disks))
      elif int(ch) == 5:
          os.system("vgdisplay")
      elif int(ch) == 6:
          size = input("Enter the size of LV you want to create: ")
          lv_name = input("Enter a name to Logical Volume: ")
          group_name = input("Enter the Volume Group name: ")
          os.system("lvcreate --size {} --name {} {}".format(size, lv_name, group_name))
      elif int(ch) == 7:
          os.system("lvdisplay")
      elif int(ch) == 8:
          group_name = input("Enter the Volume Group name: ")
          lv_name = input("Enter a name to Logical Volume: ")
          os.system("mkfs.ext4 /dev/{}/{}".format(group_name, lv_name))
      elif int(ch) == 9:
          mount = input("Enter the path of disk which you want to mount: ")
          mount_point = input("Enter the mount point: ")
          os.system("mount {} {}".format(mount, mount_point))
      elif int(ch) == 10:
          unmount = input("Enter the path of disk which you want to unmount: ")
          mount_point = input("Enter the mount point: ")
          os.system("umount {} {}".format(unmount, mount_point))
      elif int(ch) == 11:
          print("\t-----------------------------------------------------------------------------------------")
          print("\t\t\t\t\tT H A N K - Y O U ! !")
          print("\t-----------------------------------------------------------------------------------------\n\n")
          exit()
      else:
          print("option not supported")
      input("\n\n Press ENTER to continue......")
      os.system("clear")
