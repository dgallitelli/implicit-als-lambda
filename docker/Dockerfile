FROM public.ecr.aws/lambda/python:3.8

# Install dependencies
COPY requirements.txt /tmp/
RUN yum -y update 
RUN yum -y install gcc-c++
RUN pip3 install -r /tmp/requirements.txt --no-cache

# Copy inference code
COPY predict.py utils.py model.sav ${LAMBDA_TASK_ROOT}/

CMD [ "predict.handler" ]
