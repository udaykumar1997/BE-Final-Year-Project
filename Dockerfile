@Date:   2019
@Email:  udaykumar.1997@gmail.com
@Last modified time: 2019
@License: apache-2.0
@Copyright: #
#  Copyright 2019 Uday Kumar Adusumilli
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
#
#	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.



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
