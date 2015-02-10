Title: [Misc] Print pcap file in friendly format
Date: 2014-11-06 01:16
Author: m157q
Category: Misc
Tags: WireShark, pcap, tcpdump, tcpick, tcpxtract
Slug: misc-print-pcap-file-in-friendly-format

<!--more-->  
  
# Usage  
  
1. [Wireshark](https://www.wireshark.org/) (GUI)  
2. [tcpdump](http://www.tcpdump.org/) (CLI)  
    + `$ tcpdump -qns 0 -X -r ${pcap_file}` (Better for me)  
    + `$ tcpdump -qns 0 -A -r ${pcap_file}`   
3. [tcpick](http://tcpick.sourceforge.net/) (CLI)  
    + `$ tcpick -C -yP -r ${pcap_file}`  
4. [tcpxtract](http://tcpxtract.sourceforge.net/) (CLI)  
    + `$ tcpxtract -f ${pcap_file} -o {output_path}`  
  
# References  
  
+ [serverfault - How can I read pcap files in a friendly format?](http://serverfault.com/questions/38626/how-can-i-read-pcap-files-in-a-friendly-format)  
+ [Hack3rcon^3: A PCAP Workshop](http://sickbits.net/other/pcapworksheet.txt)  