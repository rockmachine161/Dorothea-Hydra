FROM ubuntu:18.04

#Install the necessary packages 
RUN apt-get update && apt-get install -y python3.6
RUN apt-get install -y net-tools
RUN apt-get install -y iputils-ping traceroute nano tcpdump
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-nmap
RUN apt-get install -y hydra
RUN pip3 install pexpect
RUN pip3 install python3-nmap
RUN pip3 install celery
RUN pip3 install future
RUN apt-get install -y psmisc 

#Install ssh server and config
RUN apt-get update && apt-get install -y openssh-server
RUN apt-get install sshpass
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22

COPY rockyou_160000_1.txt .
COPY rockyou_160000_2.txt .
COPY rockyou_160000_3.txt .
COPY rockyou_160000_4.txt .
COPY rockyou_160000_5.txt .
COPY rockyou_160000_6.txt .
COPY rockyou_160000_7.txt .
COPY rockyou_160000_8.txt .
COPY rockyou_160000_9.txt .
COPY rockyou_160000_10.txt .
COPY rockyou_160000_11.txt .
COPY rockyou_160000_12.txt .
COPY rockyou_160000_13.txt .
COPY rockyou_160000_14.txt .
COPY rockyou_160000_15.txt .
COPY rockyou_160000_16.txt .
COPY rockyou_160000_17.txt .
COPY rockyou_160000_18.txt .
COPY rockyou_160000_19.txt .
COPY rockyou_160000_20.txt .
COPY rockyou_160000_21.txt .
COPY rockyou_160000_22.txt .
COPY rockyou_160000_23.txt .
COPY rockyou_160000_24.txt .
COPY rockyou_160000_25.txt .
COPY rockyou_160000_26.txt .
COPY rockyou_160000_27.txt .
COPY rockyou_160000_28.txt .
COPY rockyou_160000_29.txt .
COPY rockyou_160000_30.txt .
COPY rockyou_160000_31.txt .
COPY rockyou_160000_32.txt .
COPY rockyou_160000_33.txt .
COPY rockyou_160000_34.txt .
COPY rockyou_160000_35.txt .
COPY rockyou_160000_36.txt .
COPY rockyou_160000_37.txt .
COPY rockyou_160000_38.txt .
COPY rockyou_160000_39.txt .
COPY rockyou_160000_40.txt .


#Create the files with which we will check if the results have already been stored
RUN echo 0 > checkAttackerReceiver.txt
RUN echo 0 > checkAttackerRouter.txt
RUN echo 0 > checkAttackerNetflow.txt

#Launch start.sh
COPY start.sh .
RUN chmod +x start.sh
CMD ["./start.sh"]
