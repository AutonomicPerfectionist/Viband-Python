# Viband-Python
Python source code implementing parts of the Viband functionality, requires the FastAccel driver. Currently only functional on a rooted LG G Watch running Android 5.0.1 under an Ubuntu chroot. Once proof-of-concept is complete a full Android app will be built.

# Setup and Installation

## Common
  1. Install the FastAccel kernel and SuperSu
  2. Sideload Linux Deploy and, if needed, change screen DPI to something more manageable.
  3. Install Ubuntu 16.04 LTS in Linux Deploy
  4. Start the container and SSH in
  5. Install Pip, and finally install viband-python

## On-Board Inference
  TODO
  
## Off-Board Inference
  1. Install viband-python on the host with pip
  2. TODO

# References
Gierad Laput, Robert Xiao, and Chris Harrison. 2016. ViBand: High-Fidelity Bio-Acoustic Sensing Using Commodity Smartwatch Accelerometers. In Proceedings of the 29th Annual Symposium on User Interface Software and Technology (UIST '16). ACM, New York, NY, USA, 321-333. DOI: https://doi.org/10.1145/2984511.2984582
