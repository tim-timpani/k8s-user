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

###k8s_user.py
Does the tedious aforementioned work of creating kubeconfig
files with limited access to the cluster.  If --role is not
provided, it will create a unique role for the new user that
only has _list, get, watch_ access to all resources.  Optionally,
an existing role name can be passed in as an agrument.

If a --user is provided, that user will be created otherwise,
the script will create one using the default value.

The k8s_user script requires an existing kubeconfig file
with sufficeint rights to create the role/rolebionding and
to request/authorize a cert request.

A new kubeconfig will be generated using the created user/role
and authenticating using the new cert.
