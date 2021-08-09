# fastapi-autowire
POC autowiring for FastAPI

# What is this?

This is a proof of concept repository showing a way to decouple business logic from FastAPI's dependency injection. 
Only autowire.py and the code setting up dependencies know about FastAPI.

autowire.py provides a class Autowirer which contains methods for dependency registration and autowiring.
Registration maps keys (classes/callable signatures) to callables.
Autowiring consists of overriding the signature of callables in order to provide new "Depends" parameter defaults which are previously registered with the class.
After registering and wiring dependencies FastAPI's dependency resolution should do its magic.
