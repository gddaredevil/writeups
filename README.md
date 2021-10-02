#Pirates
---
(Forensics, 150, 225 Solves)

Mr.Reed and his pirating ring has finally been caught by the police but unfortunately we dont have enough evidence to indict him.
All we could get is a network capture of his private network. Can you find any evidence to be used against him ?

[network_listen.pcap](https://github.com/gddaredevil/writeups/network_listen.pcap)

---

###Investigation
---

The provided file is a packet capture file. Use Wireshark to analyse it with the command `wireshark network_listen.pcap`.

Scrolling through the different packets transmitted, you can find a few `HTTP` packets. 
Find the http packet with a GET request to `/i_COULD_have_the_flag.mp4.torrent' directory. Right-click on it and select Follow > HTTP Stream.
You can find the flag in the HTTP Stream.

`dsc{H3_1S_th3_83sT_p1r4t3_1_H4V3_3V3r_s33n}`

![HTTP Stream Screenshot](https://github.com/gddaredevil/writeups/HTTP_Stream.png)
