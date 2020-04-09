# Security Information

When configuring both of the Pis, security is an important aspect especially in the context of guns. Given the emphasis on security, the following steps must be taken to help prevent unauthorised access:

- Configure both of the Pis to be connected onto a hidden, secured, wifi network
- Change the default password of the raspberry pi user
- Use local accounts rather than default root accounts
- Configure SSH to only allow certain users to access SSH (and disable root login)
- Enable SSH keys to prevent sending raw passwords over the network
- Enable a firewall to manage open communication ports
- Disable unneccessary programs
- Use SCP rather than FTP for file transfer