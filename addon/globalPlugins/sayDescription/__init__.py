# -*- coding: utf-8 -*-
# sayDescritpion: 

#Copyright 2018 dnz3d4c

#This file is covered by the GNU General Public License.
#See the file COPYING for more details.


import addonHandler
import api
import controlTypes
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
			if fOName == "" and fODc == "":
				ui.message(u"name과 description 값은 비어있음.")
			elif fOName == "":
				ui.message(u"Description: %s" % (fODc))
			elif fODc == "":
				ui.message(u"Name: %s" % (fOName))
			elif focusObj.role == controlTypes.ROLE_UNKNOWN:
				ui.message(u"알 수 없는 객체: 값을 확인할 수 없음.")
			else:
				ui.message(u"Name: %s, Description: %s" % (fOName, fODc))
		if scriptHandler.getLastScriptRepeatCount() == 1:
			if focusObj.role == controlTypes.ROLE_UNKNOWN:
				ui.message(u"알 수 없는 객체: 값을 확인할 수 없음.")
			else:
				convertName = unicode(fOName)
				convertDescription = unicode(fODc)
				cpText = u"Name: " + convertName + u"\t" + u"Description: " + convertDescription
				api.copyToClip(cpText)
				ui.message(u"복사됨")

	script_sayFocusObj.__doc__ = _(u"초점을 받은 객체의 description 값을 확인합니다.")

	def script_sayNavObj(self, gesture):
		navObj = api.getNavigatorObject()
		navOName = navObj.name
		navODc = navObj.description
		if scriptHandler.getLastScriptRepeatCount() == 0:
			if navOName == "" and navODc == "":
				ui.message(u"name과 description 값은 비어있음.")
			elif navOName == "":
				ui.message(u"Description: %s" % (navODc))
			elif navODc == "":
				ui.message(u"Name: %s" % (navOName))
			elif navObj.role == controlTypes.ROLE_UNKNOWN:
				ui.message(u"알 수 없는 객체: 값을 확인할 수 없음.")
			else:
				ui.message(u"Name: %s, Description: %s" % (navOName, navODc))
		if scriptHandler.getLastScriptRepeatCount() == 1:
			if navObj.role == controlTypes.ROLE_UNKNOWN:
				ui.message(u"알 수 없는 객체: 값을 확인할 수 없음.")
			else:
				convertName = unicode(navOName)
				convertDescription = unicode(navODc)
				cpText = u"Name: " + convertName + u"\t" + u"Description: " + convertDescription
				api.copyToClip(cpText)
				ui.message(u"복사됨")

	script_sayNavObj.__doc__ = _(u"탐색 객체의 description 값을 확인합니다.")
