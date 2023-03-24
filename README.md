# Diffie-Hellman-Key-Exchange-Algorithm
A basic implementation for the Diffie Hellman key exchange algorithm. This implementation is **not intended** for production usage. This is simply an **educational script** for people who want to understand how the algorithm works.

## Features
This script provides the following features:

- A very basic implementation of Diffie-Hellman key exchange
- Useful for understanding how the Diffie-Hellman key exchange works

## Does not include:

- Private key generation, so it needs a separate key generator

## Usage

````python
alice = DiffieHellmanUser(private_key = 8, g = 7, q = 5)
bob = DiffieHellmanUser(private_key = 13)
k = KeyExchanger(alice, bob)
k.generateSecretKey()
````
