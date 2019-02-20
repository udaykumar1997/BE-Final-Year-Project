FROM gcr.io/cloudshell-images/cloudshell:latest

RUN CUSTOM_ENV_PROJECT_ID=my-project-1537287712870
RUN CUSTOM_ENV_REPO_ID=fileOneTesting

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y build-essential

# Add your content here

# To trigger a rebuild of your Cloud Shell image:
# 1. Commit your changes locally: git commit -a
# 2. Push your changes upstream: git push origin master

# This triggers a rebuild of your image hosted at gcr.io/my-project-1537287712870/fileOneTesting.
# You can find the Cloud Source Repository hosting this file at https://source.developers.google.com/p/my-project-1537287712870/r/fileOneTesting
