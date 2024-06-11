import random

def generate_private_key(prime):
    """Generate a private key less than the prime."""
    return random.randint(2, prime - 2)

def generate_public_key(prime, base, private_key):
    """Generate a public key using the private key."""
    return pow(base, private_key, prime)

def compute_shared_secret(public_key, private_key, prime):
    """Compute the shared secret."""
    return pow(public_key, private_key, prime)

def main():
    # Define the prime number and the base (both public)
    prime = 23  # Example small prime number
    base = 5    # Example base

    # Alice generates her private and public keys
    alice_private_key = generate_private_key(prime)
    alice_public_key = generate_public_key(prime, base, alice_private_key)
    print(f"Alice's private key: {alice_private_key}")
    print(f"Alice's public key: {alice_public_key}")

    # Bob generates his private and public keys
    bob_private_key = generate_private_key(prime)
    bob_public_key = generate_public_key(prime, base, bob_private_key)
    print(f"Bob's private key: {bob_private_key}")
    print(f"Bob's public key: {bob_public_key}")

    # Alice and Bob exchange their public keys and compute the shared secret
    alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, prime)
    bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, prime)
    print(f"Alice's shared secret: {alice_shared_secret}")
    print(f"Bob's shared secret: {bob_shared_secret}")

    # Both shared secrets should be the same
    assert alice_shared_secret == bob_shared_secret, "Shared secrets do not match!"
    print("Shared secrets match!")

if __name__ == "__main__":
    main()
