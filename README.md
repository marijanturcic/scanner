# Scanner
a simple Python app for scanning ports, and a Kubernetes manifest for running the scans regularly in your cluster.

## Requirements

* Docker

* Kubernetes or a local Kubernetes application (Minikube, kind, etc..)

* kubectl
## Instructions

First, download the docker image by running the command:

    sudo docker pull marijanturcic/scanner

Alternatively, we can also build the image ourselves.
First, clone this repository and change to it as your working directory

Then run the following command to build the image:

    sudo docker build . -t marijanturcic/scanner

After getting access to a working image, start your Kubernetes cluster, and then apply the cronjob manifest with the following command:

    sudo kubectl apply -f scanner.yaml

Now our cluster will run the image every 5 minutes and scan all ports on our home IP

We can change the IP addresses that will be scanned by editing the scanner.yaml file:

    - python3 scanner.py 127.0.0.1

Replacing the IP address argument with the address of our choice, or even a range of addresses, for example:

    - python3 scanner.py 127.0.0.1-127.0.1.10

This will scan the specified range, however it is NOT advised to scan ports not belonging to your computers/machines, unless when given the owner's permission.

## Conclusion

This python network scanner app is a simple way to regularly scan the specified network, while also being a great developing experience!