FROM python:3.9-slim-buster

# move to temporary packages
WORKDIR /Users/emile/Documents/toy-infra
# create a virtual environment where to fit in the package and its dependencies
RUN bash -c "python3 -m venv env"
# activate
RUN bash -c "source env/bin/activate"
# install dependencies first
RUN bash -c "python -m pip install pendulum black pytest pyyaml click ordered-set custom_inherit"
# then install your package from TestPyPi, without the dependencies because TestPyPi messes it up.
RUN bash -c "python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps freebilly"

# environment is almost set up.

# declare a command
CMD ["freebilly", "--help"]