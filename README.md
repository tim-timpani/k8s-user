#k8s_user
Script to create k8s users with cert based auth

**WARNING**: This script creates a Kubernetes user and will apply a default set of
permissions. It is intended for lab use where common shared resources
are controled by a limited group of individuals but used by many test
engineers that need to perform diagnostic tasks.
It mitigates risk of accidental mis-configuration/deletion
of shared resources.  Use at your own risk. Never blindly apply
someone else's security policy.

###The Problem
By default, the kubeconfig files generated allows full control over 
the cluster. Creating roles, rolebindings, certificates, and
generating kubeconfig files can be tedious.

###The Solution
Automate the process of creating users with limited access.

###Requirements
Besides the packages in the requirements/setup.py, kubectl
and openssl command line tools are required and must be in
the PATH variable.

###k8s_user.py
Does the tedious aforementioned work of creating kubeconfig
files with limited access to the cluster.  

Uses an existing kubeconfig to perform the following:
* Create a cluster role that has list/get/watch privileges on all resources
and api groups. (optionally uses a pre-existing role)
* Create a cluster user and role binding
* Create and approve a certificate for the user
* Create a new kubeconfig for the new user

If a --user is provided, that user will be created otherwise,
the script will create one using the default value.

If an existing role or rolebinding by the same name already
exists, the user will be prompted to replace it or quit. Any
existing certificates by the same name will be replaced and
any kubeconfigs previously generated with the old certificate
will no longer be valid.

