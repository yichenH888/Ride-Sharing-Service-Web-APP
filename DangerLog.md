<h1 align="center">
    DangerLog
</h1>

1.  
- Bugs: Ride Sharers cannot receive notification e-mail when drivers confirm a ride, only ride owners can receive the e-mail.
- How To Handle: When the e-mail address is wrong or too much e-mails are sent, e-mails cannot be sent as expected. Thus, errors related to sending e-mails were caught, and set not to influence program running even if they actually existing.

2.  
- Bugs: The "Create Time" generated automatically does not match with time in Durham.
- How To Handle: The reason might be the time zone of server is not the time zone in Durham. It is not easy to handle the problem only if we can modify the setted time zone of server.

3.  
- Bugs: The system does not check the correctness of e-mail address, so user may not be able to receiver notification with wrong e-mail address.
- How To Handle: Add functionalities in authentification process to avoid missing notification.

4.  
- Bugs: Users can register for different accounts with the same e-mail address.
- How to Handle: This fact can lead to some chaos in identificaton management. More authentification about avoiding reusing of e-mail address should be added.
