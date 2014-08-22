# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Thu Aug  7 16:45:45 2014
#

import wx
import os
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

def getProgramFolder():
    moduleFile = __file__
    moduleDir = os.path.split(os.path.abspath(moduleFile))[0]
    programFolder = os.path.abspath(moduleDir)
    return programFolder

class CozyError(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: CozyError.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_2 = wx.Panel(self, wx.ID_ANY)
        self.error_title = wx.StaticText(self.panel_2, wx.ID_ANY, _("Error:"))
        self.error_message = wx.StaticText(self.panel_2, wx.ID_ANY, _("Error message"))
        self.button_1 = wx.Button(self.panel_2, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.close_dialog, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: CozyError.__set_properties
        self.SetTitle(_("Error"))
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap(os.path.join(getProgramFolder(), "icon/icon.png"), wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((500, 110))
        self.Hide()
        self.error_title.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: CozyError.__do_layout
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_5.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_5.Add(self.error_title, 0, 0, 0)
        sizer_5.Add(self.error_message, 0, wx.EXPAND, 0)
        sizer_5.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_5.Add(self.button_1, 0, wx.ALIGN_RIGHT, 0)
        sizer_5.Add((20, 20), 0, wx.EXPAND, 0)
        self.panel_2.SetSizer(sizer_5)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND, 0)
        sizer_3.Add((20, 20), 0, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        self.Layout()
        # end wxGlade

    def close_dialog(self, event):  # wxGlade: CozyError.<event_handler>
        self.Destroy()

# end of class CozyError
