# -*- coding: utf-8 -*-
# sayDescritpion: 

#Copyright 2018 dnz3d4c

#This file is covered by the GNU General Public License.
#See the file COPYING for more details.


import addonHandler
import api
import globalPluginHandler
import scriptHandler
import ui

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = u"sayDescription"

	def script_sayFocusObj(self, gesture):
		focusObj = api.getFocusObject()
		fOName = focusObj.name
		fODc = focusObj.description
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(u"Name: %s, Description: %s" % (fOName, fODc))

	script_sayFocusObj.__doc__ = _(u"초점을 받은 객체의 description 값을 확인합니다.")

	def script_sayNavObj(self, gesture):
		navObj = api.getNavigatorObject()
		navOName = navObj.name
		navODc = navObj.description
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(u"Name: %s, Description: %s" % (navOName, navODc))

	script_sayNavObj.__doc__ = _(u"탐색 객체의 description 값을 확인합니다.")
