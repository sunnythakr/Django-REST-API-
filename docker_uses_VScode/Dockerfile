# use the ubuntu base image
FROM ubuntu

# set the working directory inside the container 
WORKDIR /app

# copy a script file to the container 
COPY script.sh .

# make the script executable 
RUN chmod +x script.sh

# run the scripts when the container starts 
CMD ["./script.sh"]