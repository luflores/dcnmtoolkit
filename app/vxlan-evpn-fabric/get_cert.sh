openssl s_client -showcerts -connect $1:443 </dev/null | openssl x509 -outform PEM > dcnm_cert.pem
