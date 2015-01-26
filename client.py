# -*- coding: utf-8 -*-
import sys
import os
import pprint
import json
import base64
from time import sleep

import jasperserver.core as jasper
from jasperserver.repo_search import Search
from jasperserver.resource_details import Details
from jasperserver.resource_download import DownloadBinary
from jasperserver.report import Report
from jasperserver.core.resource_search_param import ResourceSearchParameter as rsp

pp = pprint.PrettyPrinter(indent=4)

session = jasper.session('http://localhost:8090/jasperserver', 'jasperadmin', 'jasperadmin')

#s = Search(session)

#s.search(path="/reports/erpnext")

#pp.pprint(s.getDescriptor())

d = Details(session, "/reports/testFolder/Example")
pp.pprint(d.serverInfo())
#pp.pprint(d.details().getDescriptor())
#print "desc: {}".format(d.details().getDescriptor())

#/themes/default/buttons.css
#dl = DownloadBinary(session, "/reports/testFolder/Example_files/main_jrxml")
#dl.downloadBinary()
#pp.pprint(dl.downloadBinary().getDescriptor().getContent(dl.downloadBinary().getDescriptor().getLabels()[0]))
#pp.pprint(dl.downloadBinary().getDescriptor().getType(dl.downloadBinary().getDescriptor().getLabels()[0]))

#r = Report(session, "/reports/testFolder/Example")
#r = Report(session, "/reports/testFolder/Silhouette")
#r = Report(session, "/reports/testFolder/Flower")
#r = Report(session, "/reports/testFolder/Cherry_Table_Based")
#r.parameter("Cascading_name_single_select", "A & U Stalker Telecommunications, Inc")
r = Report(session, "/reports/erpnext/Leaf_Red_Table_Based")
print r.run().getReportContent()
#print "details {}".format(r.details().getDescriptor().json_descriptor())
#r.updateField('query', '/reports/testFolder/Silhouette_files/query1_4').runUpdateReportDescriptor()
#pp.pprint(r.details().getDescriptor().json_descriptor())
#print "details {}".format(r.downloadJRXML().getJrxmlProperties())
#print "details {}".format(r.inputControlsValues())
#print "details {}".format(r.parameter("Title", "Luis Fernandes").parameter('subTitle', "Marques").updateInputControls())
#r.createQueryResource('select name, email from tabUser where name="administrator"', 'query1')
#não deu
#print "details {}".format(r.parameter("is_name", "where name='administrator'").updateInputControls())
#print r.run()
#pp.pprint(r.inputControlsRef())
#print "attach: {}".format(r.getAttachments())
#r.downloadJRXML()
#print "conten report {}"\
#   .format(r.downloadJRXML().getJrxmlDescriptor().json_descriptor()[0].get('content'))

#r.downloadJRXML()
#print "properties {}".format(r.getJrxmlDescriptor())

