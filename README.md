# Steps Performed
  1-created a resource group.<br>
  2-created a storage group in East US region.<br>
  3-created a container inside the storage group and created 3 folders inside that container.<br>
  4-copied some files in each of the folders.<br>
  5-Created a flask app that get the folder name and lists the filename present in the corresponding.<br>
  6-Created a VNET with one subnet in East US region.<br>
  7- Created a VM(vm type:Standard_A2_v2) with public ip and 8GB disk in the above resource group and inside the vnet and subnet created.<br>
  8-Deployed the flask app to the vm using Putty.<br>
  9-Configured inbound traffic to the vm only from tiger vpn.<br>
  
  # Steps to execute the app<external Users>
  1- User should remain connected to tiger VPN.<br>
  2- make sure the VM should be in running condition.<br>
  3- Run the given URL.<br>
  
  # Screenshot of billing information
 ![costanalysis_charts (1)](https://user-images.githubusercontent.com/92777791/162890761-88887732-dfd3-4f0b-a4aa-af849c384131.png)
  
  # Flask app URL
  http://40.88.124.72:5000/
