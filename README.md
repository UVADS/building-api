# building-api
Unified API for building systems and infrastructure.

## Documentation

FastAPI creates documentation automatically. Go to the `/docs` path of your running deployment.

Or visit https://ids.pods.uvarc.io/docs

## Endpoints

TBD.

## Development

With FastAPI development, you can run a local server as you code:
```
# cd into the app/ directory
cd app

# run the local uvicorn server (install locally first)
uvicorn main:app --reload
```
Your dev site is now running locally at [http://localhost:8000/](http://localhost:8000/)


## Build the Container

Build locally with the `docker build` command:
```
docker build -t some_org/some_image:some_tag .
```

## Build the Container using GitHub Actions

Build remotely by applying a `git tag` to the commit:
```
git tag 1.NN
```

## Run the Container Locally

Run the image locally and map the container port (80) to some host port (8080):
```
docker run -d -p 8080:80 --rm some_org/some_image:some_tag
```

## Build + Deploy

Tagged pushes (`1.5`, `2.13`) of this container build and deploy directly to K8S.
More information on the build-deploy pipeline can be found in [`.github/workflows/build.yml`](https://github.com/uvarc/id-generator/blob/main/.github/workflows/build.yml)

    https://ids.pods.uvarc.io/
