import re

with open("README.md", "r") as f:
    readme = f.read()

# Fix "production" mention for Docker Compose
readme = readme.replace("Orchestration**: Concurrently for development, Docker Compose for production", "Orchestration**: Concurrently for local development, Docker Compose for containerized environment")

# Add /admin to the project structure docs
if "/admin" not in readme:
    readme = readme.replace("routes/       auth, products, cart, reviews, orders, payment, ctf, system", "routes/       auth, products, cart, reviews, orders, payment, ctf, system, admin")

# Fix repeating Panic Button. 
# "If you break the database, hit the Panic Button in the SOC to reset everything." is good, but maybe it's mentioned twice?
# Let's check mentions of Panic Button.

with open("README.md", "w") as f:
    f.write(readme)
