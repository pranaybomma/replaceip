#!/usr/in/python
import string

i = open ("f.txt", "r")
o = open ("output.txt","w+")
for ip in i:
	oldip = ip.strip()
	if "8.18.96." in oldip:
		natip = oldip.replace('8.18.96','10.61.120')
		o.write("\n""set shared address H-"+natip+" ip-netmask "+natip)
		o.write("\n""set shared address H-"+oldip+" ip-netmask "+oldip)
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" to INTERNETDMZ")
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" from outside")
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" destination H-"+oldip)
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" destination-translation translated-address H-"+natip)
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" service any")
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" source any")
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" target negate no")
		o.write("\n""move device-group TCX-DMZ pre-rulebase nat rules "+natip+" top""\n")
		print ""
	else:
		natip = oldip.replace('8.18.97','10.61.121')
		o.write("\n""set shared address H-"+natip+" ip-netmask "+natip)
		o.write("\n""set shared address H-"+oldip+" ip-netmask "+oldip)
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" to INTERNETDMZ")
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" from outside")
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" destination H-"+oldip)
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" destination-translation translated-address H-"+natip)
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" service any")
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" source any")
		o.write("\n""set device-group TCX-DMZ pre-rulebase nat rules "+natip+" target negate no")
		o.write("\n""move device-group TCX-DMZ pre-rulebase nat rules "+natip+" top""\n")
		print ""
#	print ipaddress[0:9]
i.close()
o.close()
