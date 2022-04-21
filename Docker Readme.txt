To build image from Dockerfile, run the below command:
docker build -t [name:tag] [DirectPath | .]

To build container from image, run the below command:
docker run -i -t -d -v ${PWD}:/home --name [ContainerName] [ImageName:ImageTag]


Argument reference (context : argument ~ description):
docker build :  -t  ~ name and tag the image that you're building
docker run :    -i  ~ make interactive
docker run :    -t  ~ make terminal
docker run :    -d  ~ make detached so it runs in the background and not in current terminal
docker run :    -v  ~ create mounted volume ${PWD} = current working directory where container created from (do not use local root folder!!)   