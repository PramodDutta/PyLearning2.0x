from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate a fake name
print(fake.name())
# Output might be something like: "John Doe"

# Generate a fake address
print(fake.address())