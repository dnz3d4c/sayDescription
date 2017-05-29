# -*- coding: utf-8 -*-
# sayDescritpion: 

#Copyright (C) 2017 Aheu

#This file is covered by the GNU General Public License.
#See the file COPYING for more details.


import addonHandler
import api
import globalPluginHandler
import scriptHandler
import ui

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_sayFocusObj(self, gesture):
		focusObj = api.getFocusObject()
		fOName = focusObj.name
		fODc = focusObj.description
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(u"Name: %s, Description: %s" % (fOName, fODc))

	def script_sayNavObj(self, gesture):
		focusObj = api.getNavigatorObject()
		fOName = focusObj.name
		fODc = focusObj.description
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(u"Name: %s, Description: %s" % (fOName, fODc))

	__gestures = {
		"kb:NVDA+Shift+LeftArrow":"sayFocusObj",
		"kb:NVDA+Shift+RightArrow":"sayNavObj"
	}
	
