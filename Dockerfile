FROM alpine

RUN   apk update \
      && apk add --no-cache openssl git python2 bash py2-pip openssl \
      && git clone https://github.com/luflores/dcnmtoolkit.git \
      && echo 'PS1="\\h:\\w]#"' >> /root/.bashrc

WORKDIR /dcnmtoolkit
RUN python setup.py install

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

#RUN openssl s_client -showcerts -connect 10.0.7.99:443 </dev/null | openssl x509 -outform PEM > dcnm_cert_99.pem

WORKDIR /app

